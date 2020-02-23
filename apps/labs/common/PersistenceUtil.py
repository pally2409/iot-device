'''
Created on Feb 21, 2020

@author: pallaksingh
'''

#import libraries and modules
from labs.common.DataUtil                           import DataUtil
from labs.common.SensorData                         import SensorData
from datetime                                       import datetime
from labs.common.SensorDataListener                 import SensorDataListener
from labs.common.ActuatorDataListener               import ActuatorDataListener
from time                                           import sleep
import redis
import uuid




class PersistenceUtil(object):
    '''
    classdocs
    '''

    #initialize DataUtil()
    dataUtil = DataUtil()
    
    
    def __init__(self):
        '''
        Constructor
        '''
        #try to connect to the redis server
        try:
             
            #initialize redis client
            self.r_sensor = redis.Redis(host = "localhost", port = 6379, db = 0)
            self.r_actuator = redis.Redis(host = "localhost", port = 6379, db = 1)
         
        #if error occured   
        except Exception as e:
            
            print(e) 
        
    #register actuator data DBMS listener
    def registerActuatorDataDbmsListener(self) -> bool:
        
        #try registering to actuatorDataListener
        try:
            
            #initialize ActuatorDataListener and send current reference to redis
            actuatorDataListener = ActuatorDataListener(self.r_actuator)
            
            #start the thread
            actuatorDataListener.start()
        
        #if caused an exception    
        except Exception as e:
        
            print(e)
            
            #return false
            return False
         
        #if ran successfully   
        return True
        
    
    #register sensor data DBMS listener
    def registerSensorDataDbmsListener(self) -> bool:
        
        #try registering to sensorDataListener
        try:
        
            #initialize SensorDataListener and send current reference to redis
            sensorDataListener = SensorDataListener(self.r_sensor)
            
            #start the thread
            sensorDataListener.start()
            
        #if caused an exception    
        except Exception as e:
        
            print(e)
            
            #return false
            return False
         
        #if ran successfully   
        return True    

    
    #write actuator data to DBMS 
    def writeActuatorDataToDbms(self, actuatorData) -> bool:
        
        #convert the actuarData reference to JSON string using DataUtil()
        jsonStr = self.dataUtil.toJsonFromActuatorData(actuatorData)
        
        #create a unique key by combining device name and uuid
        key = uuid.uuid4()
        
        #add the key-value to redis
        self.r_actuator.set("actuatorData" + str(key), jsonStr)
        
        pass
    
    #write sensor data to DBMS 
    def writeSensorDataToDbms(self, sensorData) -> bool:
        
        
        
        #convert the actuarData reference to JSON string using DataUtil()
        jsonStr = self.dataUtil.toJsonFromSensorData(sensorData)
        
        #create a unique key by combining device name and uuid
        key = uuid.uuid4()
        
        print("i am here to write" + jsonStr)
        
        #add the key-value to redis
        self.r_sensor.set("sensorData" + str(key), jsonStr)
        
        pass
    
# if __name__ == '__main__':
#     
#     i = 0
#     pUtil = PersistenceUtil()
#     pUtil.registerActuatorDataDbmsListener()
#      
#     while i < 3:
#         i = i + 1
#         sensorData = SensorData()
#         sensorData.addValue(i+1)
#         sensorData.setName("Temperature Sensor")
#         pUtil.writeSensorDataToDbms(sensorData)
#         sleep(5)
    
    