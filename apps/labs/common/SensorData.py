'''
Created on Jan 22, 2020

@author: pallaksingh
'''
from datetime import datetime
import logging

#set the basic configuration to display time, level and the message
logging.getLogger("sensor data logger")
logging.basicConfig(format='%(message)s', level=logging.DEBUG)

class SensorData(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        #set the attributes for the sensor data
        self.currentValue = float(0)
        self.average = float(0)
        self.totalCount = int(0)
        self.totalValue = float(0)
        self.maxValue = None
        self.minValue = None
        self.sensorName = 'Not Set'
        self.timeStamp = str(datetime.now())
        pass
    
    #add value to the sensor data
    def addValue(self, val: float):
        
        #if value passed is not None
        try: 
            
            #convert to float
            val = float(val)
            
            #add to the aggregate value of the readings
            self.totalValue += val
            
            #increment the count
            self.totalCount += 1
            
            #change the current value to this new value
            self.currentValue = val
            
            #update the timestamp
            self.timeStamp = str(datetime.now())
            
            #if the value is the first one, or if greater than previous maxValue, update maxValue
            if self.maxValue == None or val > self.maxValue :
                self.maxValue = val
                
            #if the value is the first one, or if less than previous minValue, update minValue    
            if self.minValue == None or val < self.minValue:
                self.minValue = val
        
        #if value is None        
        except Exception as e:
            logging.info(e)        
     
    #get the average value of all the sensorData readings till now        
    def getAverageValue(self) -> float:
        
        #average = totalValue/Count
        return self.totalValue/self.getCount()
    
    #get total number of readings till now
    def getCount(self) -> int:
        return self.totalCount
    
    #get the current value
    def getCurrentValue(self) -> float:
        return self.currentValue
    
    #get the max value
    def getMaxValue(self) -> float:
        
        #if there are no readings till now, return None
        if self.getCount() == 0:
            return None
        else:
            
            #return the maxValue if readings exist
            return self.maxValue
    
    #get the min value
    def getMinValue(self) -> float:
        
        #if there are no readings till now, return None
        if self.getCount() == 0:
            return None
        else:
            
            #return the minValue if readings exist
            return self.maxValue
    
    #get the name of the sensor
    def getName(self) -> str:
        return self.sensorName
    
    #set the name of the sensor
    def setName(self, sensor_name: str):
        
        #if name passed is not None
        if sensor_name:
            self.sensorName = sensor_name
        else:
            
            #if the name passed is NoneType, simply set it to 'Not Set'
            self.sensorName = 'Not Set'
    
        
        