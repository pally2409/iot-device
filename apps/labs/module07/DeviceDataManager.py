'''
Created on Feb 24, 2020

@author: pallaksingh
'''
#Import modules
from labs.module07.CoapClientConnector      import CoapClientConnector
from labs.module07.TempSensorAdaptor        import TempSensorAdaptor

class DeviceDataManager(object):
    '''
    The manager for the device responsible for creating 
    the CoapClientConnector to be used for this Module
    Also responsible for starting the TempSensorAdaptor thread
    '''
    #Instantiate the modules
    coapClientConnector = CoapClientConnector()
    tempSensorAdaptor = TempSensorAdaptor()

    #Empty constructor as we do not want to initialize anything during instantiation
    def __init__(self):
        '''
        Constructor
        '''  
    """
    Method that passes its own reference CoapClientConnector to TempSensorAdaptor
    and starts the TempSensorAdaptor's thread so that it can get SensorData from
    the TempSensorAdaptorTask
    """
    def run(self):
        
        #Set the CoapClientConnector of the TempSensorAdaptor to the current CoapClientConnector reference
        self.tempSensorAdaptor.setCoapClient(self.coapClientConnector)
        
        #Enable the fetcher of adaptor
        self.tempSensorAdaptor.enableFetcher = True
        
        #Start
        self.tempSensorAdaptor.start()

        #will always return true as no error can occur here
        return True

    