'''
Created on Jan 14, 2020

@author: pallaksingh
'''
'''Library for system monitoring'''
import psutil

class SystemCpuUtilTask(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
    def getSensorData(self):
        '''
        Function for getting CPU utilization
        '''
        return psutil.cpu_percent(interval = 1)
        