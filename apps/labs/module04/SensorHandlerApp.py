'''
Created on Feb 14, 2020

@author: pallaksingh
'''
#import libraries and modules
from labs.module04.MultiSensorAdaptor   import MultiSensorAdaptor
import logging

if __name__ == '__main__':
    
    #instantiate the temp sensor adaptor
    multiSensorAdaptor = MultiSensorAdaptor()
    
    #call the run function of the adaptor runs the sensor threads
    multiSensorAdaptor.start()
    
    
    