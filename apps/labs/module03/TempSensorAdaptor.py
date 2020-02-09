'''
Created on Feb 6, 2020

@author: pallaksingh
'''
#import libraries and modules
from labs.module03.TempSensorAdaptorTask import TempSensorAdaptorTask
import threading
import logging

#set the basic configuration to display time, level and the message
logging.getLogger("temperature sensor adaptor")
logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.DEBUG)

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
        
    #method for creating and running the thread    
    def run(self):
        
        #log the initial message
        logging.info("Starting getTemperature thread()")
        
        #try the running thread
        try:
        
            #enable the temperature fetcher
            self.tempSensorAdaptorTask.enableFetcher = True
            
            #create the thread that calls the getTemperature() method of the tempSensorAdaptorTask
            threadTempSensorAdaptor = threading.Thread(target = self.tempSensorAdaptorTask.getTemperature())
            
            #set the temp sensor adaptor daemon to true (enable main thread to exit when done)
            threadTempSensorAdaptor.daemon = True
          
        #if found error  
        except:
            
            #return false
            return False
        
        #return true for running successfully
        return True
        