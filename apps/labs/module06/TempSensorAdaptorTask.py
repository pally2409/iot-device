'''
Created on Feb 24, 2020

@author: pallaksingh
'''
from labs.common.SensorData import SensorData
import sense_hat

class TempSensorAdaptorTask(object):
    '''
    classdocs
    '''

    #initialize sense_hat
    sense = sense_hat.SenseHat()
    
    #initialize SensorData
    sensorData = SensorData()
    
    #set the name of the Sensor
    sensorData.setName("Temperature Sensor")
    
    def __init__(self):
        '''
        Constructor
        '''
        
     
        
    #method to return the SensorData reference after getting the temperature from SenseHAT api    
    def getTemperature(self):
        
        #get the temperature and add it to SensorData
        self.sensorData.addValue(self.sense.get_temperature())
        
        #return the SensorData reference
        return self.sensorData
    
        
        