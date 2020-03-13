'''
Created on Mar 12, 2020

@author: pallaksingh
'''
#Import libraries and modules
import logging
import json
from labs.common.DataUtil               import DataUtil
from coapthon.client.helperclient       import HelperClient
from coapthon.utils                     import parse_uri

#Set the basic configuration to display time, level and the message
logging.getLogger("MQTTClientConnector")
logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.DEBUG, datefmt='%Y-%m-%d %H:%M:%S')

class CoapClientConnector(object):
    '''
    MqttClientConnector class provides abstraction for all MQTT related tasks such as
    subscribing, publishing various Sensor Data. It also holds the callback methods
    for when message is received, connection is created
    '''
    host = "coap.me"
    port = 5683
    
    client = HelperClient(server=(host, port))
    client.o
    
    #The constructor sets the callback methods to be called when a certain event happens 
    def __init__(self, params):
        '''
        Constructor
        '''
        
        
        
    
        