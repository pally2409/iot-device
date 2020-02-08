'''
Created on Feb 6, 2020

@author: pallaksingh
'''
#import libraries and modules
from sense_hat              import SenseHat
from time                   import sleep
import logging

#set the basic configuration to display time, level and the message
logging.getLogger("temperature actuator adaptor")
logging.basicConfig(format='%(message)s', level=logging.DEBUG)

class TempActuatorAdaptor(object):
    '''
    classdocs
    '''
    
    #initialize the sense hat
    sense = SenseHat()
 
    def __init__(self):
        '''
        Constructor
        '''
        
        
    #this method is responsible for actuation if the trigger is valid
    def updateActuator(self, actuatorData) -> bool:
        
        #if the passed value is not of NoneType
        if actuatorData != None:
        
            #if the actuator should increase the temperature
            if actuatorData.getCommand() == "INCREASE TEMP":
                
                try:
                
                    #display a red arrow
                    self.sense.set_pixels(actuatorData.getValue());
                    
                    #logging actuator command
                    logging.info('Triggering actuator to increase temp')
                    
                    #keep it displayed
                    sleep(3)
                    
                    #clear the matrix           
                    self.sense.clear()
        
                except Exception as e:
                    
                    print(e)
                    
                    print("increase temp cannot")
                    
                    #if error found, return a false
                    return False
                
                #if successful, return true
                return True
                
               
            #if the actuator should decrease the temperature 
            elif actuatorData.getCommand() == "DECREASE TEMP":
                
                try:
                
                    #display a blue arrow
                    self.sense.set_pixels(actuatorData.getValue());
                    
                    #logging actuator command
                    logging.info('Triggering actuator to decrease temp')
                    
                    #keep it displayed
                    sleep(3)
                    
                    #clear the matrix
                    self.sense.clear()
                 
                except:
                    
                    print("decrease temp cannot")
                    
                    #if error found, return a false  
                    return False
                
                #if successful, return true
                return True
            
            else:
                
                print("not valid trigger cannot")
                #not valid temperature actuator trigger hence, return false
                return False 
        
        #if passed value is NoneType
        else:
            
            print("nonetype cannot")
            
            #return false coz invalid actuator 
            return False
                
               
        
    
    
        