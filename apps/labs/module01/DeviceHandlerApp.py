'''
Created on Jan 14, 2020

@author: pallaksingh
'''

#import the libraries and modules
from labs.module01                          import SystemPerformanceAdaptor
from labs.module02.TempEmulatorAdaptor      import TempEmulatorAdaptor
import threading


if __name__ == '__main__':
    
    '''
        Module 1: System Performance App
    '''
    
    #instantiate system performance adaptor
    systemPerformanceAdaptor = SystemPerformanceAdaptor.SystemPerformanceAdaptor()
    
    #set the system performance adaptor daemon to true (enable main thread to exit when done)
    systemPerformanceAdaptor.daemon = True
    
    #set the system performance adaptor to true
    systemPerformanceAdaptor.enableAdaptor = False
    
    #create the thread that runs the run method of system performance adaptor
    threadSystemPerformanceAdaptor = threading.Thread(target = systemPerformanceAdaptor.run)
    
    #start the thread
    threadSystemPerformanceAdaptor.start()


    '''
        Module 2: Temperature Emulator
    '''
    
    #instantiate adaptor for temperature emulator
    tempEmulatorAdaptor = TempEmulatorAdaptor()
    
    #create the thread that runs the generaterandomTemperature() method of the tempSensorEmulatorTask
    threadTempEmulatorAdaptor = threading.Thread(target = tempEmulatorAdaptor.run())
        
    #set the emulator adaptor daemon to true (enable main thread to exit when done)
    tempEmulatorAdaptor.daemon = True
        
    #start the thread
    threadTempEmulatorAdaptor.start()
    
    while True:
        pass

    