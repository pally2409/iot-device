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
     
    #this method takes in sensorData as a parameter and checks it against the nominal temp and takes appropriate action   
    def handleSensorData(self, sensorData):
        
        logging.info(sensorData.getName())
        
        if sensorData.getName() == "i2c humidity":
            
            logging.info("hello im in handle sensor data")
            
            #get the current sensor value
            sensorVal = sensorData.getCurrentValue()
                
            #send email notification
            self.sendNotification(sensorData.loggingData, "Humidity reading from I2C Direct")
                
            #instantiate ActuatorData
            actuatorData = ActuatorData()
                
            #the thermostat should decrease the temp as the temperature is too hot!
            actuatorData.setCommand("DISPLAY I2C Humidity")
                
            #set the name of the actuator 
            actuatorData.setName("I2C Humidity")
                
            #set the value to pixel matrix
            actuatorData.setValue(sensorVal)
                
            #send the reference to the Actuator Adaptor
            self.multiActuatorAdaptor.updateActuator(actuatorData)
                
            #return the actuator data reference
            return actuatorData
        
        elif sensorData.getName() == "sense_hat API humidity":
            
            logging.info("hello im in sense hat api")
            
            #get the current sensor value
            sensorVal = sensorData.getCurrentValue()
                
            #send email notification
            self.sendNotification(sensorData.loggingData, "Humidity reading from SenseHAT API")
                
            #instantiate ActuatorData
            actuatorData = ActuatorData()
                
            #the thermostat should decrease the temp as the temperature is too hot!
            actuatorData.setCommand("DISPLAY SENSE HAT API Humidity")
                
            #set the name of the actuator 
            actuatorData.setName("SENSE HAT API Humidity")
                
            #set the value to pixel matrix
            actuatorData.setValue(sensorVal)
                
            #send the reference to the Actuator Adaptor
            self.multiActuatorAdaptor.updateActuator(actuatorData)
                
            #return the actuator data reference
            return actuatorData
        
        else:
            
            return None
            
        
    #method for sending the notification via e-mail
    def sendNotification(self, data, topic):
            
        #send email with topic indicating excessive temperature
        self.smtpClientConnector.publishMessage(data, topic)
        
        #return true for running successfully
        return True
        
        