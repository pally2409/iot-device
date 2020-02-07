'''
Created on Feb 6, 2020

@author: pallaksingh
'''


#import libraries and modules

class ActuatorData(object):
    '''
    classdocs
    '''
    
    #define the variables
    name = 'Not Set'
    
    #current value is zero
    value = 0
    
    
    def __init__(self):
        '''
        Constructor
        '''
        pass
    
    #this method returns the command as a string
    def getCommand(self) -> str:
        return 
    
    #returns the most recently added value
    def getValue(self) -> float:
        
        return self.value
    
    #returns the name of the sensor
    def getName(self) -> str:
        pass
    
    #set the command
    def setCommand(self, command):
        pass
    
    #set the name of the sensor
    def setName(self, name):
        pass
        
    
        
        
    
        