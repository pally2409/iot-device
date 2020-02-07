'''
Created on Feb 6, 2020

@author: pallaksingh
'''


#import libraries and modules

class ActuatorData(object):
    '''
    classdocs
    '''
    
    #initialize name to 'Not Set
    name = 'Not set'
    
    #initialize command to 'Not Set
    command = 'Not set'
    
    #current value is an invalid value of -100
    value = -100
    
    
    def __init__(self):
        '''
        Constructor
        '''
        pass
    
    #this method returns the command as a string
    def getCommand(self) -> str:
        return self.command
    
    #returns the most recently added value
    def getValue(self) -> float:
        return self.value
    
    #returns the name of the sensor
    def getName(self) -> str:
        return self.name
    
    #set the command
    def setCommand(self, command):
        
        #if the parameter sent is None
        if command == None:
            
            #set the command to 'Not Set
            self.command = 'Not set'
        
        #if parameter is not none    
        else: 
            
            #set the command
            self.command = command
    
    #set the name of the sensor
    def setName(self, name):
        
        #if the parameter sent is None
        if name == None:
            
            #set the name to 'Not Set
            self.name = 'Not set'
        
        #if parameter is not none        
        else:
            
            #set the command
            self.name  = name
        
    
        
        
    
        