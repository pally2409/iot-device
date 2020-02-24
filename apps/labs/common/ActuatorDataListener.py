'''
Created on Feb 21, 2020

@author: pallaksingh
'''
import threading
from labs.common.DataUtil import DataUtil
from labs.common.ActuatorData import ActuatorData
from labs.module05.MultiActuatorAdaptor import MultiActuatorAdaptor
import redis
import logging

#set the basic configuration to display time, level and the message
logging.getLogger("PersistenceUtil")
logging.basicConfig(format='%(message)s', level=logging.DEBUG)

class ActuatorDataListener(threading.Thread):
    '''
    classdocs
    '''


    #initialize DataUtil
    dUtil = DataUtil()
    
    #initialize actuatorData
    actuatorData = ActuatorData()
    
    #initialize MultiActuatorAdaptor
    multiActuatorAdaptor = MultiActuatorAdaptor()
    
    def __init__(self, r_actuator = redis.Redis(host = "localhost", port = 6379, db = 1)):
        '''
        Constructor
        '''
        
        threading.Thread.__init__(self)
        
        #set the sensor reference to one by PersistenceUtil
        self.r_actuator = r_actuator
        
        #create instance of pubsub
        self.r_pubsub = r_actuator.pubsub()
        
        #subscribe to keyspace event notifications
        self.r_pubsub.psubscribe('__keyspace@1__:*')
        
        
      
    #callback function for ActuatorData
    def onMessage(self, actuatorData):
        
        #if the type actually is of ActuatorData
        if(type(actuatorData) == ActuatorData):
            
            #do something
            self.multiActuatorAdaptor.updateActuator(actuatorData)
            
            #return true
            return True
        
        #return false if error    
        else:
            
            #return false
            return False
        
        pass
    
    def run(self):
        
        #listen for new data on the subscribed keyspace notification events 
        for event in self.r_pubsub.listen():
            
            #ignore the first message
            if type(event['data']) != int:
                
                #see if the event is a set event
                if event['data'].decode() == 'set':
                    
                    #get the channel which consists of the key 
                    event_data = event['channel'].decode()
                    
                    #split it to only get the value after the colon
                    channel = event_data.split(':')
                    actuatorDataJson =  self.r_actuator.get(channel[1])
                    
                    #call DataUtil to convert it to actuatorData
                    self.actuatorData = self.dUtil.toActuatorDataFromJson(actuatorDataJson)
                    
                    #log the data
                    logging.info("----------------------------------------------")
                    logging.info("New ActuatorData")
                    
                    #add it to file
                    self.dUtil.writeActuatorDataToFile(self.actuatorData)
                    
                    #send to onMessage
                    self.onMessage(self.actuatorData)
    