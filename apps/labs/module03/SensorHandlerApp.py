'''
Created on Feb 6, 2020

@author: pallaksingh
'''
#import libraries and modules
from labs.module03.TempSensorAdaptor import TempSensorAdaptor

if __name__ == '__main__':
    
    """
    Module 3: Using SenseHat to read temperature and trigger an event
    """
    
    #instantiate the temp sensor adaptor
    tempSensorAdaptor = TempSensorAdaptor()
    
    #call the run function of the adaptor that creates and starts the sensor task thread
    tempSensorAdaptor.run()
    
    
    