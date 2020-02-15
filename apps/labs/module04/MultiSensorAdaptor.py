'''
Created on Feb 14, 2020

@author: pallaksingh
'''

#import modules and libraries
import logging
import threading 
from labs.module04.HI2CSensorAdaptorTask                    import HI2CSensorAdaptorTask
from labs.module04.HumiditySensorAdaptorTask                import HumiditySensorAdaptorTask


#set the basic configuration to display time, level and the message
logging.getLogger("temperature sensor adaptor")
logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.DEBUG)

class MultiSensorAdaptor(object):
    '''
    classdocs
    '''

    #initialize H12CAdaptorTask and HumiditySensorAdaptorTask  
    hI2CSensorAdaptorTask = HI2CSensorAdaptorTask()
    humiditySensorAdaptorTask = HumiditySensorAdaptorTask

    def __init__(self):
        '''
        Constructor
        '''
        
    #method for creating and running the thread    
    def run(self):
        
        #log the initial message
        logging.info("Starting sensor reading daemon threads")
        
        #try the running thread
        try:
        
            #enable the fetchers
            self.hI2CSensorAdaptorTask.enableFetcher = True
            self.humiditySensorAdaptorTask.enableFetcher = True
            
            #create the thread that calls the getHumidityData() method of the tempSensorAdaptorTask
            threadHI2CSensorAdaptor = threading.Thread(target = self.hI2CSensorAdaptorTask.getHumidityData())
            threadHumiditySensorAdaptor = threading.Thread(target = self.humiditySensorAdaptorTask.getHumidityData())
            
            #set the humidity sensor adaptors daemon to true (enable main thread to exit when done)
            threadHI2CSensorAdaptor.daemon = True
            threadHumiditySensorAdaptor.daemon = True
            
            threadHI2CSensorAdaptor.start()
            threadHumiditySensorAdaptor.start()
            
          
        #if found error  
        except:
            
            #return false
            return False
        
        #return true for running successfully
        return True
        