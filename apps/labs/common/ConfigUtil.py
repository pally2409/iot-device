'''
Created on Jan 22, 2020

@author: pallaksingh
'''
#import libraries
import configparser
import os
import logging

#set the default configuration file in case no config file provided
DEFAULT_CONFIG_FILE = '../../../config/ConnectedDevicesConfig.props'

#set the basic configuration to display time, level and the message
logging.getLogger("temperature emulator logger")
logging.basicConfig(format='%(message)s', level=logging.DEBUG)

class ConfigUtil(object):
    '''
    classdocs
    '''
    #load the library to parse the configuration file
    config = configparser.ConfigParser()
    
    #initially set the flag of whether the config file is loaded to false
    configFileLoaded = False

    #this constructor takes in config file name as its parameter, if not provided, sets the config file to default file and loads it
    def __init__(self, configFileName = DEFAULT_CONFIG_FILE):
        '''
        Constructor
        '''
        self.loadConfig(configFileName)
        
    #this method returns the string value for the given section and the key    
    def getValue(self, section: str, key: str) -> str:
        
        #check if the config file is loaded
        if self.configFileLoaded == True:
            
            #try getting the value with given section and key
            try: 
                
                #get string 
                self.config.get(section, key)
                
            #if it throws an exception: section or key don't exist    
            except Exception as e:
                
                #log the exception and return
                logging.error(e)
                return False
            
            #else return the value    
            return self.config.get(section, key)
             
        #if config file is not loaded        
        else:
            
            #log the error and return
            logging.info('Config file not loaded')
            return False    
    
    #this method returns the int value for the given section and the key
    def getIntegerValue(self, section: str, key: str):
        
        #check if the config file is loaded
        if self.configFileLoaded == True:
            
            #try getting integer with given section and key
            try: 
                
                #get integer 
                self.config.getint(section, key)
                
            except Exception as e:
                
                #log the exception and return
                logging.error(e)
                return False
            
            #else return the value    
            return self.config.getint(section, key)
                
        else:
            
            #log the error and return
            logging.info('Config file not loaded')
            return False      
            

    #this method returns the boolean value for the given section and the key
    def getBooleanValue(self, section: str, key: str):
        
        #check if the config file is loaded
        if self.configFileLoaded == True:
            
            #try getting integer with given section and key
            try: 
                
                #get boolean 
                self.config.getboolean(section, key)
                
            except Exception as e:
                
                #log the exception and return
                logging.error(e)
                return 0
            
            #else return the value    
            return self.config.getboolean(section, key)
                
        else:
            
            #log the error and return
            logging.info('Config file not loaded')
            return 0      
    
    #this method checks if the config file has any valid key value pairs
    def hasConfigData(self) -> bool:
        
        #if the config file is loaded
        if self.configFileLoaded == True:
            
            #get a list of all the sections in the file
            sections = list(self.config.sections())
            
            #run a loop to traverse through each section
            for section in sections:
                
                #if the section has any key-value pairs
                if list(self.config[section]):
                    
                    #get the list of unique values from the section
                    set_values = set(self.config[section].values())
                    
                    #if there are more than 1 unique values: i.e something else is also present besides 'Not Set' or the single value is not 'Not Set'
                    if len(set_values) > 1 or list(set_values)[0]!= 'Not Set':
                        
                        #there are valid key-value pairs
                        return True
         
        #either there is no configData or configFile is not loaded    
        return False    
    
    #this method loads the configuration file from the fileName
    def loadConfig(self, fileName)->bool:
        
        #check if the fileName is valid and exists
        if os.path.exists(fileName):
            
            #read the configuration file
            self.config.read(fileName)
            
            #set the config file loaded to true
            self.configFileLoaded = True
            
            #return true as config file has been loaded
            return True
        
        else:
            
            #set the config file loaded to false
            self.configFileLoaded = False
            
            #config file couldn't be loaded
            return False
            
            
        