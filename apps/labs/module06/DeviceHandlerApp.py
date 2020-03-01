'''
Created on Feb 14, 2020

@author: pallaksingh
'''
#import libraries and modules
from labs.module06.MultiSensorAdaptor   import MultiSensorAdaptor
import logging
from labs.common.PersistenceUtil import PersistenceUtil
from labs.module06.DeviceDataManager import DeviceDataManager

if __name__ == '__main__':
    
    #instantiate the temp sensor adaptor
    deviceDataManager = DeviceDataManager()
    
    try:
        #call the run function of the adaptor runs the sensor threads
        deviceDataManager.run()
        
    except Exception as e:
        
        print(e)
    
    
    