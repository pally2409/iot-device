'''
Created on Feb 24, 2020

@author: pallaksingh
'''
from labs.module06.MqttClientConnector import MqttClientConnector
from labs.module06.MultiSensorAdaptor import MultiSensorAdaptor

class DeviceDataManager(object):
    '''
    classdocs
    '''

    #initialize the modules
    mqttClientConnector = MqttClientConnector()
    multiSensorAdaptor = MultiSensorAdaptor()


    def __init__(self):
        '''
        Constructor
        '''
        
        
    def run(self):
        
        #set the mqtt client of the MultiSensorAdaptor
        self.multiSensorAdaptor.setMqttClient(self.mqttClientConnector)
        
        #enable the fetcher of adaptor
        self.multiSensorAdaptor.enableFetcher = True
        
        #start
        self.multiSensorAdaptor.start()
        
        