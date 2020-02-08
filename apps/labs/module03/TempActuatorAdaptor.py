'''
Created on Feb 6, 2020

@author: pallaksingh
'''
#import libraries and modules
from sense_hat import SenseHat
from time import sleep

class TempActuatorAdaptor(object):
    '''
    classdocs
    '''
    
    #set the rgb values
    #no color
    e = [0, 0, 0]
    
    #red color
    r = [255, 0, 0]
    
    #blue color
    b = [0, 0, 255]
    
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
                    
                    #keep it displayed
                    sleep(3)
                    
                    #clear            
                    self.sense.clear()
        
                except Exception as e:
                    
                    print(e)
                    
                    #if error found, return a false
                    return False
                
                #if successful, return true
                return True
                
               
            #if the actuator should decrease the temperature 
            elif actuatorData.getCommand() == "DECREASE TEMP":
                
                try:
                
                    #display a blue arrow
                    self.sense.set_pixels(actuatorData.getValue());
                    
                    #keep it displayed
                    sleep(3)
                    
                    #clear 
                    self.sense.clear()
                 
                except:
                    
                    #if error found, return a false  
                    return False
                
                #if successful, return true
                return True
            
            else:
                
                #not valid temperature actuator trigger hence, return false
                return False 
        
        #if passed value is NoneType
        else:
            
            #return false coz invalid actuator 
            return False
                
               
        
    
    
        