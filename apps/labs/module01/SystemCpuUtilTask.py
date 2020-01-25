'''
Created on Jan 14, 2020

@author: pallaksingh
'''

#import libraries
import psutil

class SystemCpuUtilTask(object):
    '''
    classdocs
    '''

    #empty constructor as no extra params needed 
    def __init__(self):
        '''
        Constructor
        '''
        pass
    
    
    #method to return the CPU utilization    
    def getSensorData(self):
        return psutil.cpu_percent(interval = 1)
        