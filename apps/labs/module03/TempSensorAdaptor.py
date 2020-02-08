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
        
        #try the running thread
        try:
        
            #enable the temperature fetcher
            self.tempSensorAdaptorTask.enableFetcher = True
            
            #create the thread that calls the getTemperature() method of the tempSensorAdaptorTask
            threadTempSensorAdaptor = threading.Thread(target = self.tempSensorAdaptorTask.getTemperature())
            
            #set the temp sensor adaptor daemon to true (enable main thread to exit when done)
            threadTempSensorAdaptor.daemon = True
            
            #start the thread
            threadTempSensorAdaptor.start()
          
        #if found error  
        except:
            
            #return false
            return False
        
        #return true for running successfully
        return True
        