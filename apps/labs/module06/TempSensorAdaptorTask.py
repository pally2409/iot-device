'''
Created on Feb 24, 2020

@author: pallaksingh
'''
#Import libraries and modules
from labs.common.SensorData import SensorData
import sense_hat

class TempSensorAdaptorTask(object):
    '''
    The TempSensorAdaptorTask reads the temperature from the SenseHAT, creates a
    SensorData object using that value and returns it
    '''
    #Initialize sense_hat
    sense = sense_hat.SenseHat()
    
    #Initialize SensorData
    sensorData = SensorData()
    
    #Set the name of the Sensor 
    sensorData.setName("Temperature Sensor")
    
    #Empty constructor as we do not want to initialize anything during instantiation
    def __init__(self):
        '''
        Constructor
        '''
   
    """
    Method to return the SensorData reference after getting the temperature from SenseHAT API    
    """
    def getTemperature(self):
        
        #Get the temperature and add it to SensorData
        self.sensorData.addValue(self.sense.get_temperature())
        
        #Return the SensorData reference
        return self.sensorData