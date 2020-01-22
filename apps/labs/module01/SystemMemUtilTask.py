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

    def __init__(self):
        '''
        Constructor
        '''
        
    def getSensorData(self):
        '''
        Function for getting memory utilization
        '''
        
        '''index 2 corresponds to utilization percent'''
        return psutil.virtual_memory()[2] 