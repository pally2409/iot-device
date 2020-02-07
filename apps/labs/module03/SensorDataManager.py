'''
Created on Feb 6, 2020

@author: pallaksingh
'''
#import libraries and modules
from labs.module03.TempActuatorAdaptor              import TempActuatorAdaptor
from labs.common.ConfigUtil                         import ConfigUtil
from labs.module02.SmtpClientConnector              import SmtpClientConnector
from labs.common                                    import ActuatorData
import logging

class SensorDataManager(object):
    '''
    classdocs
    '''

    #instantiate TempActuatorAdaptor
    tempActuatorAdaptor = TempActuatorAdaptor()
    
    #instantiate ConfigUtil
    configUtil = ConfigUtil()
    
    #instantiate smtp client connector
    smtpClientConnector = SmtpClientConnector()
    


    def __init__(self):
        '''
        Constructor
        '''
        #get the nominal temp from ConfigUtil
        self.nominalTemp = self.configUtil.getIntegerValue("device", "nominalTemp")
        
    def handleSensorData(self, sensorData):
        
        #get the current sensor value
        sensorVal = sensorData.getCurrentValue()
        
        #check if temperature greater than the nominal temp
        if sensorVal > self.nominalTemp:
            
            #send email notification
            self.sendNotification(sensorData.loggingData, "High Temperature")
            
            #instantiate ActuatorData
            actuatorData = ActuatorData.ActuatorData()
            
            #the thermostat should decrease the temp as the temperature is too hot!
            actuatorData.setCommand("DECREASE TEMP")
            
            #set the value that triggered the actuator
            actuatorData.value = sensorData.getCurrentValue()
            
            #set the name of the actuator 
            actuatorData.setName("Temperature")
            
            #send the reference to the Actuator Adaptor
            self.tempActuatorAdaptor.updateActuator(actuatorData)
            
            
            return actuatorData
            
        #check if temperature less than the nominal temp
        elif sensorVal < self.nominalTemp:
            
            #send email notification
            self.sendNotification(sensorData.loggingData, "Low Temperature")
            
            #instantiate ActuatorData
            actuatorData = ActuatorData.ActuatorData()
            
            #the thermostat should increase the temp as the temperature is too cold!
            actuatorData.setCommand("INCREASE TEMP")
            
            #set the value that triggered the actuator
            actuatorData.value = sensorData.getCurrentValue()
            
            #set the name of the actuator 
            actuatorData.setName("Temperature")
            
            #send the reference to the Actuator Adaptor
            self.tempActuatorAdaptor.updateActuator(actuatorData)
            
            return actuatorData
        
        #if temperature is equal to nominal temperature, do nothing and simply return a none    
        else:
        
            #no actuation 
            return None
        
        
    #method for sending the notification via e-mail
    def sendNotification(self, data, topic):
        
        #if the currentValue is greater than or equal to the average by more than the threshold
        if topic == "High Temperature":
            
            #log the difference 
            logging.info('\n Current temperature exceeds the nominal temperature, decreasing the temperature')
            
            #send email with topic indicating excessive temperature
            self.smtpClientConnector.publishMessage("High Temperature", data)
        
        #if current value is less than the average by more than the threshold
        elif topic == "Low Temperature": 
            
            #log the difference
            logging.info('\n Nominal temperature exceeds the current temperature, increasing the temperature')
            
            #send email with topic indicating excessive temperature
            self.smtpClientConnector.publishMessage("Too low temperature", data)
        
        #return true for running successfully
        return True
        
        
        
