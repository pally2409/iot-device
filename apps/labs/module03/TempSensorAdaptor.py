'''
Created on Feb 6, 2020

@author: pallaksingh
'''
#import libraries and modules
from labs.module03.TempSensorAdaptorTask import TempSensorAdaptorTask
import threading

class TempSensorAdaptor(object):
    '''
    classdocs
    '''

    #initialize TempSensorAdaptorTask
    tempSensorAdaptorTask = TempSensorAdaptorTask()

    def __init__(self):
        '''
        Constructor
        '''
        
    def run(self):
        
        threadTempSensorAdaptor = threading.Thread(target = self.tempSensorAdaptorTask.run())
        
        threadTempSensorAdaptor.daemon = True
        
        threadTempSensorAdaptor.start()
        