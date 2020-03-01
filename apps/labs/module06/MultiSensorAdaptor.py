'''
Created on Feb 24, 2020

@author: pallaksingh
'''
import threading
from time import sleep
from labs.module06.TempSensorAdaptorTask import TempSensorAdaptorTask
from labs.module06.MqttClientConnector import MqttClientConnector


class MultiSensorAdaptor(threading.Thread):
    '''
    classdocs
    '''
    
    #initialize TempSensorAdaptorTask
    tempSensorAdaptorTask = TempSensorAdaptorTask()
    
    #initialize MqttClientConnector
    mqttClientConnector = MqttClientConnector()
    
    #disable the fetcher initially
    enableFetcher = False

    #this method is used to set the readings and the frequency of readings if provided, else defaults to 10 and 5 respectively
    def __init__(self, numReadings = 10, rateInSec = 5):

        '''
        Constructor
        '''
        
        #initialize the thread
        threading.Thread.__init__(self)
        
        #if provided numReadings and rateInSec
        self.numReadings = numReadings
        self.rateInSec = rateInSec
        
    #set the mqttClient reference
    def setMqttClient(self, mqttClientConnector):
        
        #if the parameter passed is of the appropriate type only set then
        if(type(mqttClientConnector) == MqttClientConnector):
    
            #set the reference of mqttClientConnector
            self.mqttClientConnector = mqttClientConnector
            
            #return True
            return True
        
        #if its of any other type besides MqttClientConnector
        else:
            
            #return False
            return False
        
    def start(self):
        
        #only run if there is a valid reference to mqttClientConnector and setMqttClientConnector has been called first
        if(self.mqttClientConnector!=None):
        
            #connect mqtt client
            self.mqttClientConnector.connect("broker.mqttdashboard.com", 1883)
            
            sleep(1)
        
            #data is not f doesn't run if 0 readings set:
            if self.numReadings == 0:
                    
                #return false because fetcher didn't run 
                return False
                
            #run the loop as many times as indicated in the numReadings variable
            while self.numReadings > 0:
                    
                #if the fetcher is enabled
                if self.enableFetcher:
                        
                    #get the sensorData from the task
                    sensorData = self.tempSensorAdaptorTask.getTemperature()
                            
                    #publish data to mqtt
                    self.mqttClientConnector.publishSensorCommand(sensorData, 2)
                        
                    #decrement the number of readings by 1
                    self.numReadings -= 1
                    
                    #sleep for time specified by user
                    sleep(self.rateInSec)
                        
                #if disabled    
                else: 
                        
                    #return false
                    return False
                 
            #disconnect from mqtt once done publishing   
            self.mqttClientConnector.client.disconnect()
                
            #stop the loop
            self.mqttClientConnector.client.loop_stop()
                
            #fetcher is done running, return true    
            return True
            
        #if mqtt client not connected        
        else:
                
            #return false
            return False
        
        
        
        
        
        
        
    
        
        