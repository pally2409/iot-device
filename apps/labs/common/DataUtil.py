'''
Created on Feb 21, 2020

@author: pallaksingh
'''
#import libraries and modules
from labs.common.SensorData             import SensorData
from labs.common.ActuatorData           import ActuatorData
import json

class DataUtil(object):
    '''
    classdocs
    '''


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
        pass
    
    #method to convert ActuatorData to JSON string
    def toJsonFromActuatorData(self, actuatorData) -> str:
        
        #create json string from actuatorData
        jsonStr = {
            
            "name"              : actuatorData.name,
            "command"           : actuatorData.command,
            "value"             : actuatorData.value,
            
        }
        
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
        pass
    
# if __name__ == '__main__':
# #     dUtil = DataUtil()
# #     sensorData = SensorData()
# #     sensorData.addValue(9)
# #     str1 = dUtil.toJsonFromSensorData(sensorData)
# #     print(str1)
# #     sData = dUtil.toSensorDataFromJson(str1)
# #     pUtil = PersistenceUtil()
# #     pUtil.writeSensorDataToDbms(sData)
#     pass
   