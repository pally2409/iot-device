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
    tempSensorAdaptor = TempSensorAdaptor()
    TempSensorAdaptor.run()
    
    
    