'''
Created on Jan 14, 2020

@author: pallaksingh
'''

#import the libraries
from labs.module01  import SystemPerformanceAdaptor
import threading
from labs.module02.TempEmulatorAdaptor import TempEmulatorAdaptor


if __name__ == '__main__':
    
    '''
        Module 1: System Performance App
    '''
    
    #instantiate system performance adaptor
    systemPerformanceAdaptor = SystemPerformanceAdaptor.SystemPerformanceAdaptor()
    
    #set the system performance adaptor daemon to true (enable main thread to exit when done)
    systemPerformanceAdaptor.daemon = True
    
    #set the system performance adaptor to true
    systemPerformanceAdaptor.enableAdaptor = True
    
    #create the thread that runs the run method of system performance adaptor
    threadSystemPerformanceAdaptor = threading.Thread(target = systemPerformanceAdaptor.run)
    
    #start the thread
    threadSystemPerformanceAdaptor.start()


    '''
        Module 2: Temperature Emulator
    '''
    
    #instantiate adaptor for temperature emulator
    tempEmulatorAdaptor = TempEmulatorAdaptor()
    
    #set the emulator adaptor to true
    tempEmulatorAdaptor.tempSensorEmulator.enableEmulator = True
    
    #run the adaptor
    tempEmulatorAdaptor.run()
    