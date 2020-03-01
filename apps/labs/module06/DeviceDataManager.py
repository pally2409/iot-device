'''
Created on Feb 24, 2020

@author: pallaksingh
'''
#import modules
from labs.module06.MqttClientConnector      import MqttClientConnector
from labs.module06.MultiSensorAdaptor       import MultiSensorAdaptor

class DeviceDataManager(object):
    '''
    The manager for the device responsible for creating 
    the MqttClientConnector to be used for this Module
    Also responsible for starting the MultiSensorAdaptor thread
    '''
    #instantiate the modules
    mqttClientConnector = MqttClientConnector()
    multiSensorAdaptor = MultiSensorAdaptor()

    #empty constructor as we do not want to initialize anything during instantiation
    def __init__(self):
        '''
        Constructor
        '''  
    """
    Method that passes its own reference MqttClientConnector to MultiSensorAdaptor
    and starts the MultiSensorAdaptor's thread so that it can get SensorData 
    """
    def run(self):
        
        #set the mqtt client of the MultiSensorAdaptor to the current MqttClientConnector reference
        self.multiSensorAdaptor.setMqttClient(self.mqttClientConnector)
        
        #enable the fetcher of adaptor
        self.multiSensorAdaptor.enableFetcher = True
        
        #start
        self.multiSensorAdaptor.start()