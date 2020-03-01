'''
Created on Feb 21, 2020

@author: pallaksingh
'''
#import libraries and modules
from labs.common.SensorData             import SensorData
from labs.common.ActuatorData           import ActuatorData
import json
import logging

class DataUtil(object):
    '''
    classdocs
    '''

    #initialize loggers
    sensorDataLog = logging.getLogger("SensorDataLog")
    actuatorDataLog = logging.getLogger("ActuatorDataLog")
    
    #add handlers
    sensorHandler = logging.FileHandler('../../../logfiles/SensorDataLogFile.log')
    actuatorHandler = logging.FileHandler('../../../logfiles/ActuatorDataLogFile.log')
    
    #set their levels
    sensorHandler.setLevel(logging.DEBUG)
    actuatorHandler.setLevel(logging.DEBUG)
    
    #add handlers to logger
    sensorDataLog.addHandler(sensorHandler)
    actuatorDataLog.addHandler(actuatorHandler)

    def __init__(self):
        '''
        Constructor
        '''
        
    #method to convert SensorData to JSON string
    def toJsonFromSensorData(self, sensorData) -> str:
        
        #create json string from sensorData
        jsonStr = {
            
            "currentValue"      : sensorData.currentValue,
            "average"           : sensorData.average,
            "totalCount"        : sensorData.totalCount,
            "totalValue"        : sensorData.totalValue,
            "maxValue"          : sensorData.maxValue,
            "minValue"          : sensorData.minValue,
            "sensorName"        : sensorData.sensorName,
            "timestamp"         : sensorData.timeStamp 
            
        }
        
        jsonStr = json.dumps(jsonStr)
        #return the string
        return jsonStr
    
    #method to convert JSON string to SensorData 
    def toSensorDataFromJson(self, jsonStr) -> SensorData:
        
        #instantiate SensorData
        sensorData = SensorData()
        
        #use json load to convert it to a dictionary
        jsonLoad = json.loads(jsonStr)
        
        #parse and add it to the sensorData object one by one
        sensorData.currentValue =       jsonLoad["currentValue"]
        sensorData.average =            jsonLoad["average"]
        sensorData.totalCount =         jsonLoad["totalCount"]
        sensorData.minValue =           jsonLoad["minValue"]
        sensorData.maxValue =           jsonLoad["maxValue"]
        sensorData.totalValue =         jsonLoad["totalValue"]
        sensorData.sensorName =         jsonLoad["sensorName"]
        sensorData.timeStamp =          jsonLoad["timestamp"]
        
        #return the SensorData  reference
        return sensorData
    
    #method to convert SensorData to JSON and write to filesystem
    def writeSensorDataToFile(self, sensorData) -> bool:
        
        #if the type of ActuatorData passed is not of type actuatorData
        if(type(sensorData) != SensorData):
            
            #create json string with everything not set
            jsonStr = {
                
                    "currentValue"      : 0.0,
                    "average"           : 0.0,
                    "totalCount"        : 0.0,
                    "totalValue"        : 0.0,
                    "maxValue"          : 0.0,
                    "minValue"          : 0.0,
                    "sensorName"        : "Not Set",
                    "timestamp"         : "No Timestamp" 
                
            }
        
        #create json string from sensorData
        jsonStr = {
            
            "currentValue"      : sensorData.currentValue,
            "average"           : sensorData.average,
            "totalCount"        : sensorData.totalCount,
            "totalValue"        : sensorData.totalValue,
            "maxValue"          : sensorData.maxValue,
            "minValue"          : sensorData.minValue,
            "sensorName"        : sensorData.sensorName,
            "timestamp"         : sensorData.timeStamp 
            
        }
        
        #get the JSONstr
        jsonStr = json.dumps(jsonStr)
        
        #format it to pretty printed JSON string
        jsonFormatted = json.loads(jsonStr)
        prettyJson = json.dumps(jsonFormatted, indent = 2)
        
        #log it 
        self.sensorDataLog.info(prettyJson)
        
        return True
        
        pass
    
    #method to convert ActuatorData to JSON string
    def toJsonFromActuatorData(self, actuatorData) -> str:
        
        #if the type of ActuatorData passed is not of type actuatorData
        if(type(actuatorData) != ActuatorData):
            
            #create json string with everything not set
            jsonStr = {
                
                "name"              : "Not Set",
                "command"           : "Not Set",
                "value"             : "Not Set",
                
            }
        
        else:     
        
            #create json string from actuatorData
            jsonStr = {
                
                "name"              : actuatorData.name,
                "command"           : actuatorData.command,
                "value"             : actuatorData.value,
                
            }
        
        #get the string from the dict    
        jsonStr = json.dumps(jsonStr)
        
        #return the string
        return jsonStr
    
    #method to convert JSON string to ActuatorData 
    def toActuatorDataFromJson(self, jsonStr) -> ActuatorData:
        
        #instantiate ActuatorData
        actuatorData = ActuatorData()
        
        #use json load to convert it to a dictionary
        jsonLoad = json.loads(jsonStr)
        
        #parse and add it to the actuatorData object one by one
        actuatorData.name =             jsonLoad['name']
        actuatorData.command =          jsonLoad['command']
        actuatorData.value =            jsonLoad['value']
        
        #return the actuatorData reference
        return actuatorData
    
    #method to convert ActuatorData to JSON and write to filesystem
    def writeActuatorDataToFile(self, actuatorData) -> bool:
        
        #if the type of ActuatorData passed is not of type actuatorData
        if(type(actuatorData) != ActuatorData):
            
            #create json string with everything not set
            jsonStr = {
                
                "name"              : "Not Set",
                "command"           : "Not Set",
                "value"             : "Not Set",
                
            }
        
        else:     
        
            #create json string from actuatorData
            jsonStr = {
                
                "name"              : actuatorData.name,
                "command"           : actuatorData.command,
                "value"             : actuatorData.value,
                
        }
        
        #get the JSONstr
        jsonStr = json.dumps(jsonStr)
        
        #format it to pretty printed JSON string
        jsonFormatted = json.loads(jsonStr)
        prettyJson = json.dumps(jsonFormatted, indent = 2)
        
        #log it 
        self.actuatorDataLog.info(prettyJson)
        
        return True
    
