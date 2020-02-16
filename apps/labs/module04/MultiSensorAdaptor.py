'''
Created on Feb 14, 2020

@author: pallaksingh
'''

#import modules and libraries
import logging
import threading 
from datetime                                               import datetime
from time                                                   import sleep
from labs.module04.HI2CSensorAdaptorTask                    import HI2CSensorAdaptorTask
from labs.module04.HumiditySensorAdaptorTask                import HumiditySensorAdaptorTask
from labs.module04.SensorDataManager                        import SensorDataManager


#set the basic configuration to display time, level and the message
logging.getLogger("temperature sensor adaptor")
logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.DEBUG)

class MultiSensorAdaptor(threading.Thread):
    '''
    classdocs
    '''

    #initialize H12CAdaptorTask, HumiditySensorAdaptorTask and SensorDataManager
    hI2CSensorAdaptorTask = HI2CSensorAdaptorTask()
    humiditySensorAdaptorTask = HumiditySensorAdaptorTask()
    sensorDataManager = SensorDataManager()

    #the constructor used to set the readings and the frequency of readings if provided, else defaults to 10 and 5 respectively
    def __init__(self, numReadings = 10, rateInSec = 4):
        '''
        Constructor
        '''
        threading.Thread.__init__(self)
        
        #set the number of readings you want to get
        self.numReadings = numReadings
        
        #set the rate at which you want to get the readings
        self.rateInSec = rateInSec
        
    #method for running the thread    
    def run(self):
        
        #log the initial message
        logging.info("Starting sensor reading daemon threads")
        logging.info("Initializing I2C bus and enabling I2C addresses")
        
        #enable the fetchers for both the tasks
        self.hI2CSensorAdaptorTask.enableFetcher = True
        self.humiditySensorAdaptorTask.enableFetcher = True
        
        #data is not false doesn't run if 0 readings set:
        if self.numReadings == 0:
            
            return False
        
        #this try-except block checks whether a keyboard interrupt exception occurs and clears the sensehat if yes
        try: 
            
            #run the loop as many times as indicated in the numReadings variable
            while self.numReadings > 0:
                
                #initialize the sensor data list that will store both sensorData from I2C bus and senseHat API
                sensorDataHumidity = []
                
                #check if fetcher is enabled for hi2cSensorAdaptorTask
                if self.hI2CSensorAdaptorTask.enableFetcher:
                    
                    #store the sensorData value from the current reading 
                    sensorDataHumidity.append(self.hI2CSensorAdaptorTask.getHumidityData())
                 
                #sleep for few seconds between getting these two values  
                sleep(0.05)
                    
                #check if fetcher is enabled for humiditySensorAdaptorTask
                if self.humiditySensorAdaptorTask.enableFetcher:
                    
                    #store the sensor data value from the current reading to the list
                    sensorDataHumidity.append(self.humiditySensorAdaptorTask.getHumidityData())
                
                #if there was valid sensorData in sensorDataHumidity
                if len(sensorDataHumidity) != 0:
                    
                    #handle the sensor data using the manager
                    self.sensorDataManager.handleSensorData(sensorDataHumidity)
                    
                else:
                    
                    #return false
                    return False
                
                #log the difference
                logData = str(datetime.now()) + ",INFO:Difference: " + str(abs(sensorDataHumidity[0] - sensorDataHumidity[1]))
                logging.info(logData)    
    
                #sleep for few seconds
                sleep(self.rateInSec)  
        
        #if keyboard interrupt occurs        
        except (KeyboardInterrupt):
            
            #clear the sensorData    
            self.sensorDataManager.multiActuatorAdaptor.sense.clear()
            
        return True        
            
            
                
            
            
               
        
               

           