'''
Created on Feb 14, 2020

@author: pallaksingh
'''
#import modules and libraries
from labs.module06.DeviceDataManager import DeviceDataManager

"""
The main method that instantiates the DeviceDataManager and calls its run method
"""
if __name__ == '__main__':
    
    #instantiate the DeviceDataManager()
    deviceDataManager = DeviceDataManager()

    #call the run function of the adaptor runs the sensor threads
    deviceDataManager.run()