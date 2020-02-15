'''
Created on Feb 14, 2020

@author: pallaksingh
'''
#import libraries and modules
import sense_hat 
import logging
import threading
from time                                           import sleep
from labs.common.SensorData                         import SensorData
from labs.module04.SensorDataManager                import SensorDataManager

#set the basic configuration to display time, level and the message
logging.getLogger("humidity_api_fetcher_logger")
logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.DEBUG, datefmt='%Y-%m-%d %H:%M:%S')

class HumiditySensorAdaptorTask():
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
    def __init__(self):
        '''
        Constructor
        '''
        
    #get the humidity data using the sense hat library
    def getHumidityData(self):

        #get the humidity from the sense hat
        humidity = self.sense.get_humidity()
                
        #add it to the sensorData
        self.sensorData.addValue(humidity)
        
        #store the updated values from sensorData object
        time = '            Time: ' + self.sensorData.timeStamp
        current = '            Current: ' + str(self.sensorData.getCurrentValue())
        average = '            Average: ' + str(self.sensorData.getAverageValue())
        samples = '            Samples: ' + str(self.sensorData.getCount())
        min_temp = '            Min: ' + str(self.sensorData.getMinValue())
        max_temp = '            Max: ' + str(self.sensorData.getMaxValue())
        data = 'Humidity' + '\n' + time + '\n' + current + '\n' + average + '\n' + samples + '\n' + min_temp + '\n' + max_temp
             
        #add to data section of sensorData
        self.sensorData.loggingData = data
                
        #create the concatenation for logging
        logData = self.sensorData.timeStamp + ",INFO:SenseHAT API Humidity: " + str(self.sensorData.getCurrentValue())
                
        #log the current sensorData values 
        logging.info(logData)
        
        #return the sensor data
        return self.sensorData
                
    #method to return the current instance of the sensor data
    def getSensorData(self):
        
        #return the reference to the sensor data
        return self.sensorData