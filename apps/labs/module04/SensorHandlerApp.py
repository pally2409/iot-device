'''
Created on Feb 14, 2020

@author: pallaksingh
'''

from labs.module04.MultiSensorAdaptor   import MultiSensorAdaptor
import logging

if __name__ == '__main__':
    
    #instantiate the temp sensor adaptor
    multiSensorAdaptor = MultiSensorAdaptor()
    
    #call the run function of the adaptor that creates and starts the sensor task thread 
    multiSensorAdaptor.run()
    
    
    