'''
Created on Feb 24, 2020

@author: pallaksingh
'''
#Import libraries and modules
import threading
from time                                   import sleep
from labs.module06.TempSensorAdaptorTask    import TempSensorAdaptorTask
from labs.module06.MqttClientConnector      import MqttClientConnector


class MultiSensorAdaptor(threading.Thread):
    '''
    The MultiSensorAdaptor gets the temperature from the TempSensorAdaptorTask. It
    gets the amount of reading at a frequency indicated during instantiation
    '''
    #Instantiate TempSensorAdaptorTask
    tempSensorAdaptorTask = TempSensorAdaptorTask()
    
    #Instantiate MqttClientConnector
    mqttClientConnector = MqttClientConnector()
    
    #Disable the fetcher initially
    enableFetcher = False

    """
    The constructor is used to set the readings (numReadings) and the 
    frequency of readings (rateInSec) if provided, else defaults to 10 and 5 respectively
    """
    def __init__(self, numReadings = 10, rateInSec = 5):
        '''
        Constructor
        '''
        #Initialize the thread
        threading.Thread.__init__(self)
        
        #If provided numReadings and rateInSec
        self.numReadings = numReadings
        self.rateInSec = rateInSec
    
    """    
    This method takes in a MqttClientConnector reference and assigns it to its own
    MqttClientConnector
    """
    def setMqttClient(self, mqttClientConnector):
        
        #Check if the parameter passed is of the type mqttClientConnector, only set it then
        if(type(mqttClientConnector) == MqttClientConnector):
    
            #Set the reference of mqttClientConnector
            self.mqttClientConnector = mqttClientConnector
            
            #Return True for successful assignment
            return True
        
        #if its of any other type besides MqttClientConnector
        else:
            
            #return False for failure to assign
            return False
    
    """    
    This method polls the TempSensorAdaptor task to get the SensorData from it,
    it then calls the MQTTClientConnector to publish it MQTT
    """    
    def start(self):
        
        #Only run if there is a valid reference to mqttClientConnector and setMqttClientConnector has been called first
        if(self.mqttClientConnector!=None):
        
            #Connect the MQTT client
            self.mqttClientConnector.connect("broker.mqttdashboard.com", 1883)
            
            #Sleep for 1 second to let it connect
            sleep(1)
        
            #Data is not fetched if only 0 readings set:
            if self.numReadings == 0:
                    
                #Return false because fetcher didn't run 
                return False
                
            #Run the loop as many times as indicated in the numReadings variable
            while self.numReadings > 0:
                    
                #If the fetcher is enabled
                if self.enableFetcher:
                        
                    #Get the sensorData from the task
                    sensorData = self.tempSensorAdaptorTask.getTemperature()
                            
                    #Publish data to MQTT
                    self.mqttClientConnector.publishSensorCommand(sensorData, 2)
                        
                    #Decrement the number of readings by 1
                    self.numReadings -= 1
                    
                    #Sleep for time specified by user
                    sleep(self.rateInSec)
                        
                #If fetcher is disabled    
                else: 
                        
                    #Return false to indicate no readings taken
                    return False
                 
            #Disconnect from MQTT once done publishing all SensorData
            self.mqttClientConnector.client.disconnect()
                
            #Stop the MQTT loop that listens for MQTT events
            self.mqttClientConnector.client.loop_stop()
                
            #Fetcher is done running, return true to indicate readings were taken   
            return True
            
        #If MQTT client not connected        
        else:
                
            #Return false to indicate no readings were taken
            return False     