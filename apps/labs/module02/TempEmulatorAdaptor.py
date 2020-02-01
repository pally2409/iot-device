'''
Created on Jan 22, 2020

@author: pallaksingh
'''

#import libraries
from labs.module02.TempSensorEmulatorTask import TempSensorEmulatorTask
import threading

class TempEmulatorAdaptor(object):
    '''
    classdocs
    '''

    #instantiate the emulator task
    tempSensorEmulator = TempSensorEmulatorTask()
    
    def __init__(self):
        '''
        Constructor
        '''
        pass
    
    def run(self):
        
        #create the thread that runs the generaterandomTemperature() method of the tempSensorEmulatorTask
        threadTempSensorEmulator = threading.Thread(target = self.tempSensorEmulator.generateRandomTemperature())
        
        #set the system performance adaptor daemon to true (enable main thread to exit when done)
        self.tempSensorEmulator.daemon = True
        
        #start the thread
        threadTempSensorEmulator.start()
        
        #return true for running successfully
        return True    