'''
Created on Feb 6, 2020

@author: pallaksingh
'''
#import libraries and modules
from sense_hat                              import SenseHat
from labs.common.SensorData                 import SensorData
from time                                   import sleep
from labs.module03.SensorDataManager        import SensorDataManager
import logging

#set the basic configuration to display time, level and the message
logging.getLogger("temperature emulator logger")
logging.basicConfig(format='%(message)s', level=logging.DEBUG)

#this is a threaded class
class TempSensorAdaptorTask(object):
    '''
    classdocs
    '''

    #instantiate the SenseHat class
    sense = SenseHat()
    
    #disable the emulator initially
    enableFetcher = False
    
    #instantiate the SensorData class
    sensorData = SensorData()
    
    #instantiate the SensorDataManager
    sensorDataManager = SensorDataManager()

    def __init__(self, numReadings = 10, rateInSec = 5):
        '''
        Constructor
        '''
        
        #set the number of readings you want to get
        self.numReadings = numReadings
        
        #set the rate at which you want to get the readings
        self.rateInSec = rateInSec
        
    #get the temperature
    def getTemperature(self):
        
        #data is not f doesn't run if 0 readings set:
        if self.numReadings == 0:
            return False
        
        #run the loop as many times as indicated in the numReadings variable
        while self.numReadings > 0:
            
            #if the fetcher is enabled
            if self.enableFetcher:

                #clear the sense hat
                self.sense.clear()
                
                print("Getting temp")

                #get the temperature from the sense hat
                temp = self.sense.get_temperature()
                
                #add it to the sensorData
                self.sensorData.addValue(temp)
                
                
                #store the updated values from sensorData object
                time = '                    Time: ' + self.sensorData.timeStamp
                current = '                    Current: ' + str(self.sensorData.getCurrentValue())
                average = '                    Average: ' + str(self.sensorData.getAverageValue())
                samples = '                    Samples: ' + str(self.sensorData.getCount())
                min_temp = '                    Min: ' + str(self.sensorData.getMinValue())
                max_temp = '                    Max: ' + str(self.sensorData.getMaxValue())
                data = 'Temperature' + '\n' + time + '\n' + current + '\n' + average + '\n' + samples + '\n' + min_temp + '\n' + max_temp
                
                #log the current sensorData values 
                logging.info(data)
                
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
        
        
        
        
        
    