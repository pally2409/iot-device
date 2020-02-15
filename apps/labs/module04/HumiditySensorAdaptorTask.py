'''
Created on Feb 14, 2020

@author: pallaksingh
'''
#import libraries and modules
import sense_hat 
import logging
from time                                           import sleep
from labs.common.SensorData                         import SensorData
from labs.module04.SensorDataManager                import SensorDataManager

#set the basic configuration to display time, level and the message
logging.getLogger("humidity api fetcher logger")
logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.DEBUG)

class HumiditySensorAdaptorTask(object):
    '''
    classdocs
    '''

    #initialize the sense hat class from the library
    sense = sense_hat.SenseHat()
    
    #initialize the fetcher 
    enableFetcher = True
    
    #instantiate the SensorData class
    sensorData = SensorData()
    
    #set the sensorData name to humidity via sense_hat api
    sensorData.setName("sense_hat API humidity")
    
    #instantiate the SensorDataManager
    sensorDataManager = SensorDataManager()

    #this method is used to set the readings and the frequency of readings if provided, else defaults to 10 and 5 respectively
    def __init__(self, numReadings = 10, rateInSec = 3):
        '''
        Constructor
        '''
        
        #set the number of readings you want to get
        self.numReadings = numReadings
        
        #set the rate at which you want to get the readings
        self.rateInSec = rateInSec
        
    #get the humidity data using the sense hat library
    def getHumidityData(self):
        
        #data is not f doesn't run if 0 readings set:
        if self.numReadings == 0:
            return False
        
        #run the loop as many times as indicated in the numReadings variable
        while True:
            
            #if the fetcher is enabled
            if True:

                #clear the sense hat 
                self.sense.clear()

                #get the humidity from the sense hat
                temp = self.sense.get_humidity()
                
                #add it to the sensorData
                self.sensorData.addValue(temp)
                
                logging.info(temp)
                
                #store the updated values from sensorData object
                time = '            Time: ' + self.sensorData.timeStamp
                current = '            Current: ' + str(self.sensorData.getCurrentValue())
                average = '            Average: ' + str(self.sensorData.getAverageValue())
                samples = '            Samples: ' + str(self.sensorData.getCount())
                min_temp = '            Min: ' + str(self.sensorData.getMinValue())
                max_temp = '            Max: ' + str(self.sensorData.getMaxValue())
                data = 'Temperature' + '\n' + time + '\n' + current + '\n' + average + '\n' + samples + '\n' + min_temp + '\n' + max_temp
                
                #create the concatenation for logging
                logData = "SenseHAT API Humidity" + self.sensorData.getCurrentValue()
                
                #log the current sensorData values 
                logging.info(logData)
                self.sensorData.loggingData = data
                
                #send it to the SensorDataManager who will check if it needs actuation
                self.sensorDataManager.handleSensorData(self.sensorData)
                
                #decrement as the number of readings by 1 to keep count of how many readings left
                self.numReadings -= 1
                    
                #sleep for time indicated in rateInSec
                sleep(self.rateInSec)
            
            #if fetcher is not enabled
            else:
                
                #fetch didn't run
                return False
            
        #the fetcher is done running
        return True
        
        pass
    
    #method to return the current instance of the sensor data
    def getSensorDara(self):
        
        #return the reference to the sensor data
        return self.sensorData