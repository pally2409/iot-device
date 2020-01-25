'''
Created on Jan 14, 2020

@author: pallaksingh
'''

'''Library for system monitoring'''
import psutil

class SystemMemUtilTask(object):
    '''
    classdocs
    '''
    #empty constructor as no extra params needed
    def __init__(self):
        '''
        Constructor
        '''
    
    #method to return virtual memory utilization    
    def getSensorData(self):
        #index 2 corresponds to utilization percent'''
        return psutil.virtual_memory()[2] 