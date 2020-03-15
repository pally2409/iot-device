'''
Created on Feb 14, 2020

@author: pallaksingh
'''
#Import libraries and modules
import threading
import asyncio
from time                                   import sleep
from labs.module07.TempSensorAdaptorTask    import TempSensorAdaptorTask
from labs.module07.CoapClientConnector      import CoapClientConnector

class TempSensorAdaptor(threading.Thread):
    '''
    The TempSensorAdaptor gets the temperature from the TempSensorAdaptorTask. It
    gets the amount of reading at a frequency indicated during instantiation
    '''
    #Instantiate TempSensorAdaptorTask
    tempSensorAdaptorTask = TempSensorAdaptorTask()
    
    #Instantiate CoapClientConnector
    coapClientConnector = CoapClientConnector()
    
    #Disable the fetcher initially
    enableFetcher = False

    """
    The constructor is used to set the readings (numReadings) and the 
    frequency of readings (rateInSec) if provided, else defaults to 10 and 5 respectively
    """
    def __init__(self, numReadings = 10, rateInSec = 5):
        '''
        Constructor
        '''
        #Get the asynchronous event reference that can be passed to the thread initialization
        self.loop = asyncio.get_event_loop()

        #Initialize the thread using the asyncio event loop
        threading.Thread.__init__(self, args=(self.loop,))
        
        #If provided numReadings and rateInSec
        self.numReadings = numReadings
        self.rateInSec = rateInSec
    
    """    
    This method takes in a CoapClientConnector reference and assigns it to its own
    CoapClientConnector

    @param coapClientConnector An object reference of CoapClientConnector which should be assigned to this class's CoapClientConnector
    """
    def setCoapClient(self, coapClientConnector):
        #Check if the parameter passed is of the type coapClientConnector, only set it then
        if(type(coapClientConnector) == CoapClientConnector):
    
            #Set the reference of coapClientConnector
            self.coapClientConnector = coapClientConnector
            
            #Return True for successful assignment
            return True
        
        #if its of any other type besides CoapClientConnector
        else:
            
            #return False for failure to assign
            return False
    
    """    
    This method polls the TempSensorAdaptor task to get the SensorData from it,
    it then calls the COAPClientConnector to publish it COAP
    """    
    def start(self):
        
        #Sending different types of request messages to the server
        self.coapClientConnector.callGETRequest(self.loop, "pallybook.lan", "Temp"),                                      #The GET Request
        self.coapClientConnector.callDELETERequest(self.loop, "pallybook.lan", "Temp")                                    #The DELETE Request
        self.coapClientConnector.callPOSTRequest(self.loop, "Sending a POST request message", "pallybook.lan", "Temp")    #The POST Request

        #Data is not fetched if only 0 readings set:
        if self.numReadings == 0:
                    
            #Return false because fetcher didn't run 
            return False
                
        #Run the loop as many times as indicated in the numReadings variable
        while self.numReadings > 0:
                    
            #If the fetcher is enabled
            if self.enableFetcher:
                        
                #Get the sensorData from the task
                sensorData = self.tempSensorAdaptorTask.getTemperature()
                
                #Send request data to COAP 
                self.coapClientConnector.prepareAndSendSensorData(sensorData, self.loop, "pallybook.lan", "Temp")
                        
                #Decrement the number of readings by 1
                self.numReadings -= 1
                    
                #Sleep for time specified by user
                sleep(self.rateInSec)
                        
            #If fetcher is disabled    
            else: 
                        
                #Return false to indicate no readings taken
                return False
                
        #Fetcher is done running, return true to indicate readings were taken   
        return True  