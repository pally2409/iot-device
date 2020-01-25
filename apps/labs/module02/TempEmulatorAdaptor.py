'''
Created on Jan 22, 2020

@author: pallaksingh
'''
from labs.module02.TempSensorEmulatorTask import TempSensorEmulatorTask
import threading

class TempEmulatorAdaptor(object):
    '''
    classdocs
    '''

    tempSensorEmulator = TempSensorEmulatorTask()
    def __init__(self):
        '''
        Constructor
        '''
        pass
    
    def run(self):
        threadTempSensorEmulator = threading.Thread(target = self.tempSensorEmulator.generateRandomTemperature())
        self.tempSensorEmulator.daemon = True
        threadTempSensorEmulator.start()
        
        
             