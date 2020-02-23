'''
Created on Feb 21, 2020

@author: pallaksingh
'''
import threading
from labs.common.DataUtil import DataUtil
from labs.module05.MultiActuatorAdaptor import MultiActuatorAdaptor
class ActuatorDataListener(threading.Thread):
    '''
    classdocs
    '''


    #initialize DataUtil
    dUtil = DataUtil()
    
    #initialize MultiActuatorAdaptor
    multiActuatorAdaptor = MultiActuatorAdaptor()
    
    def __init__(self, r_actuator):
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
        
        #do something
        self.multiActuatorAdaptor.updateActuator(actuatorData)
        
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
                    actuatorData = self.dUtil.toActuatorDataFromJson(actuatorDataJson)
                
                    #send to onMessage
                    self.onMessage(actuatorData)
    