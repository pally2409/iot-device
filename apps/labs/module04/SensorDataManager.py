'''
Created on Feb 14, 2020

@author: pallaksingh
'''

#import libraries and modules
from labs.common.ConfigUtil                         import ConfigUtil
from labs.common.ActuatorData                       import ActuatorData
from labs.module04.MultiActuatorAdaptor             import MultiActuatorAdaptor
from labs.module02.SmtpClientConnector              import SmtpClientConnector
import logging
from time import sleep


#set the basic configuration to display time, level and the message
logging.getLogger("sensor data manager logger")
logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.DEBUG)

class SensorDataManager(object):
    '''
    classdocs
    '''

    #instantiate TempActuatorAdaptor
    multiActuatorAdaptor = MultiActuatorAdaptor()
    
    #instantiate ConfigUtil
    configUtil = ConfigUtil()
    
    #instantiate smtp client connector
    smtpClientConnector = SmtpClientConnector()

    
    def __init__(self):
        '''
        Constructor
        '''   
     
    #this method takes in sensorData as a parameter and checks it against the type of readings and takes appropriate action   
    def handleSensorData(self, sensorDatas):
        
        #initialize the list for actuatorData 
        actuatorDataList = []
        
        #iterate through the sensorDatas list
        for sensorData in sensorDatas:
        
            #if the reading is directly from i2c bus
            if sensorData.getName() == "i2c humidity":
                
                #get the current sensor value
                sensorVal = sensorData.getCurrentValue()
                    
                #instantiate ActuatorData
                actuatorData = ActuatorData()
                    
                #the actuator should display the current humidity
                actuatorData.setCommand("DISPLAY I2C Humidity")
                    
                #set the name of the actuator 
                actuatorData.setName("I2C Humidity")
                    
                #set the value to the current humidity value
                actuatorData.setValue(sensorVal)
                
                #send email notification consisting of the reading
                self.sendNotification(sensorData.loggingData, "Humidity Reading from I2C Bus")
                
                #append the actuator data to the list 
                actuatorDataList.append(actuatorData)
            
            #if the reading is directly from sensehat api
            elif sensorData.getName() == "sense_hat API humidity":
                
                #get the current sensor value
                sensorVal = sensorData.getCurrentValue()
                    
                #instantiate ActuatorData
                actuatorData = ActuatorData()
                    
                #the actuator should display the current humidity
                actuatorData.setCommand("DISPLAY SENSE HAT API Humidity")
                    
                #set the name of the actuator 
                actuatorData.setName("SENSE HAT API Humidity")
                    
                #set the value to the current humidity value
                actuatorData.setValue(sensorVal)
                
                #send email notification consisting of the reading
                self.sendNotification(sensorData.loggingData, "Humidity Reading from SenseHAT API")
                 
                #append the actuator data to the list             
                actuatorDataList.append(actuatorData)
            
            #if not valid sensor data reading
            else:
                
                #return none
                return None
        
        #send the list to the updateActuator method of the multiActuatorAdaptor
        self.multiActuatorAdaptor.updateActuator(actuatorDataList)
        
        #return the list of actuatorData
        return actuatorDataList
            
        
    #method for sending the notification via e-mail
    def sendNotification(self, data, topic):
            
        #send email with topic indicating excessive temperature
        self.smtpClientConnector.publishMessage(data, topic)
        
        #create a delay for email to be sent
        sleep(2)
        
        #return true for running successfully
        return True
        
        