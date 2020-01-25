'''
Created on Jan 22, 2020

@author: pallaksingh
'''
import configparser
import os

DEFAULT_CONFIG_FILE = '../../../config/ConnectedDevicesConfig.props'
class ConfigUtil(object):
    '''
    classdocs
    '''
    config = configparser.ConfigParser()
    configFileLoaded = False

    def __init__(self, configFileName = DEFAULT_CONFIG_FILE):
        '''
        Constructor
        '''
        self.loadConfig(configFileName)
        
    def getValue(self, section: str, key: str) -> str:
        if self.configFileLoaded == True:
            if section in self.config:
                if key in self.config[section]:
                    return self.config[section][key]
        return 'Error'
    
    def hasConfigData(self) -> bool:
        if self.configFileLoaded == True:
            sections = list(self.config.sections())
            for section in sections:
                if list(self.config[section]):
                    set_values = set(self.config[section].values())
                    if len(set_values) > 1 or list(set_values)[0]!= 'Not Set':
                        return True
                    
        return False    
    
    def loadConfig(self, fileName)->bool:
        if os.path.exists(fileName):
            self.config.read(fileName)
            self.configFileLoaded = True
            return True
        else:
            return False
            
            
        