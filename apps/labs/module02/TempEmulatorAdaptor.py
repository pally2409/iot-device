'''
Created on Jan 22, 2020

@author: pallaksingh
'''

#import libraries and modules
from labs.module02.TempSensorEmulatorTask import TempSensorEmulatorTask

class TempEmulatorAdaptor(object):
    '''
    classdocs
    '''

    #instantiate the emulator task
    tempSensorEmulator = TempSensorEmulatorTask()
    
    #empty constructor because no extra params need to be passed during instantiation
    def __init__(self):
        '''
        Constructor
        '''
        pass
    
    #method for creating and running the emulator thread
    def run(self):
        
        #enable the emulator 
        self.tempSensorEmulator.enableEmulator = True
        
        #call the generateRandomTemperature
        self.tempSensorEmulator.generateRandomTemperature()
        
        #return true for running successfully
        return True    