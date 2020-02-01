'''
Created on Jan 22, 2020

@author: pallaksingh
'''
#import libraries
from labs.common    import SensorData
from labs.module02  import SmtpClientConnector
from time           import sleep
import random
import logging

#set the basic configuration to display time, level and the message
logging.getLogger("temperature emulator logger")
logging.basicConfig(format='%(message)s', level=logging.DEBUG)

#print the initial message
logging.info("Starting Temperature Sensor Emulator Thread")

class TempSensorEmulatorTask(object):
    '''
    classdocs
    '''
    
    #initialize sensor data to hold the aggregate and current temp values
    sensorData = SensorData.SensorData()
    
    #intialize smtp connector for sending notifications
    smtpConnector = SmtpClientConnector.SmtpClientConnector()
    
    #disable the emulator initially
    enableEmulator = False

    '''
    constructor takes in the lower and upper bound on temperature generator, 
    how often it should generate temp and the threshold for difference between 
    average and current temp
    '''
    def __init__(self, minTemp = 0.0, maxTemp = 30.0, rateInSec = 10, threshold = 5.0, numReadings = 10):
        '''
        Constructor
        '''
        
        #set the values to the default values or the one sent while instantiating
        self.rateInSec = rateInSec
        self.minTemp = minTemp
        self.maxTemp = maxTemp
        self.threshold = float(threshold)
        self.numReadings = numReadings
    
    #method to generate a random temperature between the lower and upper bound
    def generateRandomTemperature(self):
        
        #generator doesn't run if 0 readings set:
        if self.numReadings == 0:
            return False
        
        #run the loop as many times as indicated in the numReadings variable
        while self.numReadings > 0:
            
            #if the emulator is enabled
            if self.enableEmulator:

                #generate a random temperature 
                self.sensorData.addValue(random.uniform(float(self.minTemp), float(self.maxTemp)))
                
                #store the updated values from sensorData object
                time = '                                Time: ' + self.sensorData.timeStamp
                current = '                                Current: ' + str(self.sensorData.getCurrentValue())
                average = '                                Average: ' + str(self.sensorData.getAverageValue())
                samples = '                                Samples: ' + str(self.sensorData.getCount())
                min_temp = '                                Min: ' + str(self.sensorData.getMinValue())
                max_temp = '                                Max: ' + str(self.sensorData.getMaxValue())
                data = 'Temperature' + '\n' + time + '\n' + current + '\n' + average + '\n' + samples + '\n' + min_temp + '\n' + max_temp
                
                #log the current sensorData values 
                logging.info(data)
                
                #check if the current value and the average value differ by more than the threshold
                if abs(self.sensorData.getCurrentValue() - self.sensorData.getAverageValue()) > self.threshold:
                    
                    #send notfication if so
                    self.sendNotification(data)
                
                #decrement as the number of readings by 1 to keep count of how many readings left
                self.numReadings -= 1
                    
                #sleep for time indicated in rateInSec
                sleep(self.rateInSec)
            
            #if emulator is not enabled
            else:
                
                #generator didn't run
                return False
            
        #the generator is done running
        return True
                
                
            
    #method that returns the reference to the sensorData
    def getSensorData(self) -> SensorData.SensorData:   
        return self.sensorData
    
    #method for sending the notification via e-mail
    def sendNotification(self, data):
        
        #if the currentValue is greater than or equal to the average by more than the threshold
        if self.getSensorData().getCurrentValue() >= self.getSensorData().getAverageValue():
            
            #log the difference 
            logging.info('\n Current temperature exceeds average by > ' + str(self.threshold) + '. Triggering alert ')
            
            #send email with topic indicating excessive temperature
            self.smtpConnector.publishMessage("Excessive Temperature", data)
        
        #if current value is less than the average by more than the threshold
        elif self.getSensorData().getCurrentValue() < self.getSensorData().getAverageValue(): 
            
            #log the difference
            logging.info('\n Average temperature exceeds current value by >' + str(self.threshold) + '. Triggering alert ')
            
            #send email with topic indicating excessive temperature
            self.smtpConnector.publishMessage("Too low temperature", data)
        
        return True

            
            
        