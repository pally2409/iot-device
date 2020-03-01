'''
Created on Feb 24, 2020

@author: pallaksingh
'''
import paho.mqtt.client as mqtt
from labs.common.DataUtil import DataUtil
import logging
import json

#set the basic configuration to display time, level and the message
logging.getLogger("humidity_api_fetcher_logger")
logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.DEBUG, datefmt='%Y-%m-%d %H:%M:%S')

class MqttClientConnector(object):
    '''
    classdocs
    '''
    #initialize mqtt client as publisher
    client = mqtt.Client("Publisher_Pallak")
    
    #initialize DataUtil 
    dUtil = DataUtil()

    def __init__(self):
        '''
        Constructor
        '''
        #set the callback functions for the client
        self.client.on_connect = self.onConnect
        self.client.on_message = self.messageReceived
        
    #method for connecting to host and port 
    def connect(self, host = "broker.hivemq.com", port = 1883):
        
        #try to connect to sent 
        try: 
             
            #setup mqtt connection
            self.client.connect(host, port)
            self.client.loop_start()
        
        #if error occured  
        except Exception as e:
            
            #log the error
            logging.info(e)
             
    #this method is the callback function when the client connects to MQTT
    def onConnect(self, client, userdata, rc):
        
        logging.info("MQTT:Connected with" + str(rc))
        
        #if connected    
        self.isConnected = True
        
    #this method takes in actuatorData, converts it to JSON string and publishes
    def publishActuatorCommand(self, actuatorData, qos) -> bool:
        
        #publish only if the client is connected
        if(self.client.is_connected() == True):
        
            #try to publish the actuatorData
            try:
            
                #get the json String from actuatorData
                jsonStr =  self.dUtil.toJsonFromActuatorData(actuatorData)
                
                #log the JSON
                #format it to pretty printed JSON string
                jsonFormatted = json.loads(jsonStr)
                prettyJson = json.dumps(jsonFormatted, indent = 2)
                logging.info("Publishing ActuatorData to MQTT Topic Connected-Devices/Actuator_Data")
                logging.info(prettyJson)
                logging.info("-----------------------------------------------------------------------------")
        
                #publish sensor Data
                self.client.publish("Connected-Devices/Actuator_Data", jsonStr, qos=2)
              
            #if error occurred  
            except Exception as e:
                
                #return false
                return False
            
            #if run successfully return True
            return True
        
        #if the client is not connected
        else:
            
            #return False
            return False
    
    def publishSensorCommand(self, sensorData, qos) -> bool:

        #publish only if the client is connected
        if(self.client.is_connected() == True):

            #try to publish the actuatorData
            try: 
                
                #get the json String from sensorData
                jsonStr =  self.dUtil.toJsonFromSensorData(sensorData)
                
                #log the JSON
                #format it to pretty printed JSON string
                jsonFormatted = json.loads(jsonStr)
                prettyJson = json.dumps(jsonFormatted, indent = 2)
                
                #log the JSON
                logging.info("Publishing SensorData to MQTT Topic Connected-Devices/Sensor_Data")
                logging.info(prettyJson)
                logging.info("-----------------------------------------------------------------------------")
        
                #publish sensor Data
                self.client.publish("Connected-Devices/Sensor_Data", jsonStr, qos=2)
            
            #if error occurred  
            except Exception as e:
                
                #return false
                return False
            
            #if run successfully return True
            return True
        
        #if client is not connected
        else:
            
            #return false
            return False    

    def subscribeToActuatorCommands(self, topic, qos):
        
        #subscribe only if the client is connected
        if(self.client.is_connected() == True):
            
            #subscribe to topic
            self.client.subscribe(topic, qos)
        
        #if client is not connected    
        else:
            
            #return false
            return False
        
        #return true for successful subscription
        return True
    
    def subscribeToSensorCommands(self, topic, qos):
        
        #subscribe only if the client is connected
        if(self.client.is_connected() == True):
            
            #subscribe to topic
            self.client.subscribe(topic, qos)
        
        #if client is not connected    
        else:
            
            #return false
            return False
        
        #return true for successful subscription
        return True

    
    def messageReceived(self, client, userdata, msg):
        
        #check whether it is coming from SensorData topic
        if msg.topic == "Connected-Devices/Sensor_Data":
            
            #convert to SensorData
            sensorData = self.dUtil.toSensorDataFromJson(msg.payload)
            
            #do something with it
            
            
        #check if it is coming from ActuatorData topic
        elif msg.topic == "Connected-Devices/Actuator_Data":
            
            #convert to ActuatorData
            actuatorData = self.dUtil.toActuatorDataFromJson(msg.payload)
            
            #do something with it
        
            
    