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
logging.getLogger("humidity_i2c_fetcher_logger")
logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.DEBUG, datefmt='%Y-%m-%d %H:%M:%S')

class HI2CSensorAdaptorTask():
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
    def __init__(self):
        '''
        Constructor
        '''
        logging.info("Initializing I2C bus and enabling I2C addresses")
        
        
    def run(self):
        
        self.getHumidityData()
        
    def getHumidityData(self):
                
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
                
            #create the concatenation for logging
            logData = self.sensorData.timeStamp + ",INFO:I2C Direct Humidity: " + str(self.sensorData.getCurrentValue())
                
            #log the current sensorData values 
            logging.info(logData)
                
    
    #method to return the current instance of the sensor data
    def getSensorData(self):
        
        #return the reference to the sensor data
        return self.sensorData
    
    
        
        
        



        