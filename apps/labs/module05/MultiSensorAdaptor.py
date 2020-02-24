'''
Created on Feb 14, 2020

@author: pallaksingh
'''

#import modules and libraries
import logging
import threading 
from datetime                                               import datetime
from time                                                   import sleep
from labs.module05.TempSensorAdaptorTask                    import TempSensorAdaptorTask
from labs.common.PersistenceUtil import PersistenceUtil


#set the basic configuration to display time, level and the message
logging.getLogger("temperature sensor adaptor")
logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.DEBUG)

class MultiSensorAdaptor():
    '''
    classdocs
    '''

    #initialize TempSensorAdaptorTask
    tempSensorAdaptorTask = TempSensorAdaptorTask()

    def __init__(self):
        '''
        Constructor
        '''
        #start the Dbms listener from PersistenceUtil
        self.pUtil = PersistenceUtil()
        self.pUtil.registerActuatorDataDbmsListener()
        
        
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
            
            
                
            
            
               
        
               

           