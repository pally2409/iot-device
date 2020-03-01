'''
Created on Feb 24, 2020

@author: pallaksingh
'''
#Import libraries and modules
import paho.mqtt.client as mqtt
import logging
import json
from labs.common.DataUtil  import DataUtil

#Set the basic configuration to display time, level and the message
logging.getLogger("MQTTClientConnector")
logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.DEBUG, datefmt='%Y-%m-%d %H:%M:%S')

class MqttClientConnector(object):
    '''
    MqttClientConnector class provides abstraction for all MQTT related tasks such as
    subscribing, publishing various Sensor Data. It also holds the callback methods
    for when message is received, connection is created
    '''
    #Initialize MQTT client as publisher
    client = mqtt.Client("Publisher_Pallak")
    
    #Initialize DataUtil 
    dUtil = DataUtil()

    #The constructor sets the callback methods to be called when a certain event happens 
    def __init__(self):
        '''
        Constructor
        '''
        #Set the callback functions for the client
        self.client.on_connect = self.onConnect
        self.client.on_message = self.messageReceived
    
    """    
    Method for setting up the MQTT connection using the host and port provided.
    Host defaults to "broker.hivemq.com" and port defaults to 1883
    """
    def connect(self, host = "broker.hivemq.com", port = 1883):
        
        #Try to set up the connection with given host and port
        try: 
             
            #Setup the MQTT connection
            self.client.connect(host, port)
            
            #Start the loop that will keep listening for events like connection done or new message
            self.client.loop_start()
        
        #If error occurred while setting up the connection
        except Exception as e:
            
            #Log the error
            logging.info(e)
    
    """         
    This method is the callback for when the client connects to MQTT
    """
    def onConnect(self, client, userdata, rc):
        
        #Log the return code
        logging.info("MQTT:Connected with" + str(rc))
     
    """   
    This method takes in Actuator Data and the Quality of Service level, 
    converts Actuator Data to JSON string and publishes
    it to the standard Actuator Data topic with the particular QoS level
    """
    def publishActuatorCommand(self, actuatorData, qos) -> bool:
        
        #Publish only if the client is connected
        if(self.client.is_connected() == True):
        
            #Try to publish the actuatorData 
            try:
            
                #Get the json String from actuatorData
                jsonStr =  self.dUtil.toJsonFromActuatorData(actuatorData)
            
                #Format it to pretty printed JSON string (properly indented)
                jsonFormatted = json.loads(jsonStr)
                prettyJson = json.dumps(jsonFormatted, indent = 2)
                
                #Log the JSON
                logging.info("Publishing ActuatorData to MQTT Topic Connected-Devices/Actuator_Data")
                logging.info(prettyJson)
                logging.info("-----------------------------------------------------------------------------")
        
                #Publish the ActuatorData 
                self.client.publish("Connected-Devices/Actuator_Data", jsonStr, qos=2)
              
            #If error occurred while publishing
            except Exception as e:
                
                #Log the error
                logging.info(e)
                
                #Return false to indicate failure to publish
                return False
            
            #If run successfully return True
            return True
        
        #If the client is not connected
        else:
            
            #Return False to indicate failure to publish
            return False
    
    """   
    This method takes in Sensor Data and the Quality of Service level, 
    converts Sensor Data to JSON string and publishes
    it to the standard Sensor Data topic with the particular QoS level
    """
    def publishSensorCommand(self, sensorData, qos) -> bool:

        #Publish only if the client is connected
        if(self.client.is_connected() == True):

            #Try to publish the Sensor Data
            try: 
                
                #Get the json String from Sensor Data
                jsonStr =  self.dUtil.toJsonFromSensorData(sensorData)
                
                #Format it to pretty printed JSON string (properly indented)
                jsonFormatted = json.loads(jsonStr)
                prettyJson = json.dumps(jsonFormatted, indent = 2)
                
                #Log the JSON
                logging.info("Publishing SensorData to MQTT Topic Connected-Devices/Sensor_Data")
                logging.info(prettyJson)
                logging.info("-----------------------------------------------------------------------------")
        
                #Publish Sensor Data
                self.client.publish("Connected-Devices/Sensor_Data", jsonStr, qos=2)
            
            #If error occurred while publishing
            except Exception as e:
                
                #Log the error
                logging.info(e)
                
                #Return false to indicate failure to publish
                return False
            
            #if run successfully return True
            return True
        
        #If client is not connected
        else:
            
            #return false to indicate failure to publish
            return False    

    """   
    This method takes in a topic and the Quality of Service level, 
    and subscribes to the topic using the given QoS level. The topic
    defaults to the standard topic for ActuatorData data
    """
    def subscribeToActuatorCommands(self, topic = "Connected-Devices/Actuator_Data", qos):
        
        #Subscribe only if the client is connected
        if(self.client.is_connected() == True):
            
            #Subscribe to topic
            self.client.subscribe(topic, qos)
        
        #If client is not connected    
        else:
            
            #Return false to indicate failure to subscribe
            return False
        
        #Return true for successful subscription
        return True
    
    """   
    This method takes in a topic and the Quality of Service level, 
    and subscribes to the topic using the given QoS level. The topic
    defaults to the standard topic for SensorData data
    """
    def subscribeToSensorCommands(self, topic = "Connected-Devices/Sensor_Data", qos):
        
        #Subscribe only if the client is connected
        if(self.client.is_connected() == True):
            
            #Subscribe to topic
            self.client.subscribe(topic, qos)
        
        #If client is not connected    
        else:
            
            #Return false to  indicate failure to subscribe
            return False
        
        #Return true for successful subscription
        return True

    """         
    This method is the callback for when the there is a new message from the
    topic to which the client is subscribed to. It checks whether the message is 
    from either of the standard topics. The module doesn't indicate the course of 
    action for subscription on iot-device, hence we have kept a placeholder for
    any future actions
    """
    def messageReceived(self, client, userdata, msg):
        
        #Check whether it is coming from SensorData topic
        if msg.topic == "Connected-Devices/Sensor_Data":
            
            #Convert to SensorData
            sensorData = self.dUtil.toSensorDataFromJson(msg.payload)
            
            #do something with it
            
        #Check if it is coming from ActuatorData topic
        elif msg.topic == "Connected-Devices/Actuator_Data":
            
            #Convert to ActuatorData
            actuatorData = self.dUtil.toActuatorDataFromJson(msg.payload)
            
            #do something with it