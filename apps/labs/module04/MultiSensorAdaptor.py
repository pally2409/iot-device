'''
Created on Feb 14, 2020

@author: pallaksingh
'''

#import modules and libraries
import logging
import threading 
from time import sleep
from labs.module04.HI2CSensorAdaptorTask                    import HI2CSensorAdaptorTask
from labs.module04.HumiditySensorAdaptorTask                import HumiditySensorAdaptorTask
from labs.module03.SensorDataManager import SensorDataManager


#set the basic configuration to display time, level and the message
logging.getLogger("temperature sensor adaptor")
logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.DEBUG)

class MultiSensorAdaptor(object):
    '''
    classdocs
    '''

    #initialize H12CAdaptorTask and HumiditySensorAdaptorTask  
    hI2CSensorAdaptorTask = HI2CSensorAdaptorTask()
    humiditySensorAdaptorTask = HumiditySensorAdaptorTask()
    sensorDataManager = SensorDataManager()

    #this method is used to set the readings and the frequency of readings if provided, else defaults to 10 and 5 respectively
    def __init__(self, numReadings = 10, rateInSec = 1):
        '''
        Constructor
        '''
        threading.Thread.__init__(self)
        
        #set the number of readings you want to get
        self.numReadings = numReadings
        
        #set the rate at which you want to get the readings
        self.rateInSec = rateInSec
        
    #method for creating and running the thread    
    def run(self):
        
        #log the initial message
        logging.info("Starting sensor reading daemon threads")
        
        #enable the fetchers
        self.hI2CSensorAdaptorTask.enableFetcher = True
        self.humiditySensorAdaptorTask.enableFetcher = True
        
        #data is not f doesn't run if 0 readings set:
        if self.numReadings == 0:
            return False
        
        #run the loop as many times as indicated in the numReadings variable
        while self.numReadings > 0:
            
            #initialize their sensor data as none
            sensorDataHumidity = None
            sensorDataI2C = None
            
            
            if self.hI2CSensorAdaptorTask.enableFetcher:
                
                sensorDataI2C = self.hI2CSensorAdaptorTask.getHumidityData()
                
            sleep(self.rateInSec)
                
            if self.humiditySensorAdaptorTask.enableFetcher:
                
                sensorDataHumidity = self.humiditySensorAdaptorTask.getHumidityData()
            
            if sensorDataHumidity:
                
                self.sensorDataManager.handleSensorData(sensorDataHumidity)
                
            if sensorDataI2C:
                
                self.sensorDataManager.handleSensorData(sensorDataI2C)
                
            
                
            
            
                
            
            
               
        
               

           