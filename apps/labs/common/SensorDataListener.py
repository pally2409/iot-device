'''
Created on Feb 21, 2020

@author: pallaksingh
'''
import threading
from labs.common.DataUtil           import DataUtil
from time                           import sleep

class SensorDataListener(threading.Thread):
    '''
    classdocs
    '''
    
    #initialize DataUtil
    dUtil = DataUtil()


    def __init__(self, r_sensor):
        '''
        Constructor
        '''
        threading.Thread.__init__(self)
        
        #set the sensor reference to one by PersistenceUtil
        self.r_sensor = r_sensor
        
        #create instance of pubsub
        self.r_pubsub = r_sensor.pubsub()
        
        #subscribe to keyspace event notifications
        self.r_pubsub.psubscribe('__keyspace@0__:*')
        
    
    #SensorData callback function   
    def onMessage(self, sensorData):
        
        #DO SOMETHING
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
                    sensorDataJson =  self.r_sensor.get(channel[1])
                    
                    #call DataUtil to convert it to sensorData
                    sensorData = self.dUtil.toSensorDataFromJson(sensorDataJson)
                
                    #send to onMessage
                    self.onMessage(sensorData)
                
            
                
        
        
        
        
        