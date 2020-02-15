'''
Created on Feb 14, 2020

@author: pallaksingh
'''

#import libraries and modules
import logging
import numpy as np
import threading
from time                                           import sleep
from labs.common.SensorData                         import SensorData
from labs.module04.SensorDataManager                import SensorDataManager
from smbus2.smbus2                                  import SMBus
                                

#set the basic configuration to display time, level and the message
logging.getLogger("humidity i2c fetcher logger")
logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.DEBUG)


class HI2CSensorAdaptorTask(threading.Thread):
    '''
    classdocs
    '''
    #initialize the bus no.1 of i2c bus of raspberrypi
    i2cBus = SMBus(1)
    
    #initialize the address for the humidity sensor
    humidAddr = 0x5F 
    
    #initialize the fetcher 
    enableFetcher = True
    
    #instantiate the SensorData class
    sensorData = SensorData()
    
    #set the sensorData name to humidity via i2c bus
    sensorData.setName("i2c humidity")
    
    #instantiate the SensorDataManager
    sensorDataManager = SensorDataManager()
    
    #number of bits to shift when concatenating two 8 bit register values to 1 16 bit value
    bits = 8

    #this method is used to set the readings and the frequency of readings if provided, else defaults to 10 and 5 respectively
    def __init__(self, numReadings = 10, rateInSec = 5):
        '''
        Constructor
        '''
        threading.Thread.__init__(self)
        
        #set the number of readings you want to get
        self.numReadings = numReadings
        
        #set the rate at which you want to get the readings
        self.rateInSec = rateInSec
        
    def run(self):
        
        self.getHumidityData()
        
        
    def getHumidityData(self):
        
        logging.info("Initializing I2C bus and enabling I2C addresses")
        
        #data is not f doesn't run if 0 readings set:
        if self.numReadings == 0:
            return False
        
        #run the loop as many times as indicated in the numReadings variable
        while self.numReadings > 0:
            
            #if the fetcher is enabled
            if self.enableFetcher:
                
                #reading the value of coefficients H0_rh_x2 and H1_rh_x2 from 0x30 and 0x31
                coeffH0 = np.uint8(self.i2cBus.read_byte_data(self.humidAddr, 0x30))
                coeffH1 = np.uint8(self.i2cBus.read_byte_data(self.humidAddr, 0x31))
                
                #dividing by 2 by shifting right to obtain H0_rh and H1_rh
                h0_rh = float(coeffH0/2.0)
                h1_rh = float(coeffH1/2.0)
                
                #reading the value from h0_t0_out from 0x36 and 0x37
                h0_t0_out_0 = np.uint8(self.i2cBus.read_byte_data(self.humidAddr, 0x36))
                h0_t0_out_1 = np.uint8(self.i2cBus.read_byte_data(self.humidAddr, 0x37))
                
                #concatenate them
                h0_t0_out = np.int16((h0_t0_out_1 << self.bits) | h0_t0_out_0)
                
                #reading the value from h1_t0_out from 0x3A and 0x3B 
                h1_t0_out_0 = np.uint8(self.i2cBus.read_byte_data(self.humidAddr, 0x3A))
                h1_t0_out_1 = np.uint8(self.i2cBus.read_byte_data(self.humidAddr, 0x3B))
                
                #concatenate them
                h1_t0_out = np.int16((h1_t0_out_1 << self.bits) | h1_t0_out_0)
                
                #read humidity value in raw counts from 0x28 and 0x29
                h_t_out_0 = np.uint8(self.i2cBus.read_byte_data(self.humidAddr, 0x28))
                h_t_out_1 = np.uint8(self.i2cBus.read_byte_data(self.humidAddr, 0x29))
                
                #concatenate them
                h_t_out = np.int16((h_t_out_1 << self.bits) | h_t_out_0)
                
                #find the relative humidity
                rel_hum = float(((h1_rh - h0_rh) * (h_t_out - h0_t0_out)/(h1_t0_out - h0_t0_out)) + h0_rh)
                
                #add to sensor data
                self.sensorData.addValue(rel_hum)
                
                #store the updated values from sensorData object
                time = '            Time: ' + self.sensorData.timeStamp
                current = '            Current: ' + str(self.sensorData.getCurrentValue())
                average = '            Average: ' + str(self.sensorData.getAverageValue())
                samples = '            Samples: ' + str(self.sensorData.getCount())
                min_temp = '            Min: ' + str(self.sensorData.getMinValue())
                max_temp = '            Max: ' + str(self.sensorData.getMaxValue())
                data = 'Temperature' + '\n' + time + '\n' + current + '\n' + average + '\n' + samples + '\n' + min_temp + '\n' + max_temp
                
                #create the concatenation for logging
                logData = "I2C Direct Humidity" + str(self.sensorData.getCurrentValue())
                
                #log the current sensorData values 
                logging.info(logData)
#                 self.sensorData.loggingData = data
                
                #send it to the SensorDataManager who will check if it needs actuation
                self.sensorDataManager.handleSensorData(self.sensorData)
                
                #decrement as the number of readings by 1 to keep count of how many readings left
                self.numReadings -= 1
                    
                #sleep for time indicated in rateInSec
                sleep(self.rateInSec)
            
            #if fetcher is not enabled
            else:
                logging.info("false")
                #fetch didn't run
                return False
        logging.info("Did not run")    
        #the fetcher is done running
        return True
    
    
    #method to return the current instance of the sensor data
    def getSensorDara(self):
        
        #return the reference to the sensor data
        return self.sensorData
    
    
        
        
        



        