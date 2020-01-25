'''
Created on Jan 22, 2020

@author: pallaksingh
'''
from datetime import datetime
class SensorData(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.currentValue = float(0)
        self.average = float(0)
        self.totalCount = int(0)
        self.totalValue = float(0)
        self.maxValue = None
        self.minValue = None
        self.sensorName = 'Not Set'
        self.timeStamp = str(datetime.now())
        pass
    
    def addValue(self, val: float):
        self.totalValue += val
        self.totalCount += 1
        self.currentValue = val
        self.timeStamp = str(datetime.now())
        if self.maxValue == None or val > self.maxValue :
            self.maxValue = val
        if self.minValue == None or val < self.minValue:
            self.minValue = val
    
    def getAverageValue(self) -> float:
        return self.totalValue/self.getCount()
    
    def getCount(self) -> int:
        return self.totalCount
    
    def getCurrentValue(self) -> float:
        return self.currentValue
    
    def getMaxValue(self) -> float:
        if self.getCount() == 0:
            return None
        else:
            return self.maxValue
    
    def getMinValue(self) -> float:
        if self.getCount() == 0:
            return None
        else:
            return self.maxValue
    
    def getName(self) -> str:
        return self.sensorName
    
    def setName(self, sensor_name: str):
        self.sensorName = sensor_name
    
        
        