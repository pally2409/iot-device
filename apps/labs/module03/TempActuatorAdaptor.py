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


    #initialize upward red arrow to indicate actuator increasing my temperature
    arrowRedInc = [
                e,e,e,r,r,e,e,e,
                e,e,r,r,r,r,e,e,
                e,r,e,r,r,e,r,e,
                r,e,e,r,r,e,e,r,
                e,e,e,r,r,e,e,e,
                e,e,e,r,r,e,e,e,
                e,e,e,r,r,e,e,e,
                e,e,e,r,r,e,e,e
        ]
    
    #initialize downward blue arrow to indicate actuator increasing my temperature
    arrowBlueDec = [
                e,e,e,b,b,e,e,e,
                e,e,e,b,b,e,e,e,
                e,e,e,b,b,e,e,e,
                e,e,e,b,b,e,e,e,
                b,e,e,b,b,e,e,b,
                e,b,e,b,b,e,b,e,
                e,e,b,b,b,b,e,e,
                e,e,e,b,b,e,e,e
        ]
 
 
    def __init__(self):
        '''
        Constructor
        '''
        
        
    #this method is responsible for actuation if the trigger is valid
    def updateActuator(self, actuatorData) -> bool:
        
        #if the actuator should increase the temperature
        if actuatorData.getCommand() == "INCREASE TEMP":
            
            try:
            
                #display a red arrow
                self.sense.set_pixels(self.arrowRedInc);
                
                #keep it displayed
                sleep(3)
                
                #clear            
                self.sense.clear()
    
            except:
                
                #if error found, return a false
                return False
            
            #if successful, return true
            return True
            
           
        #if the actuator should decrease the temperature 
        elif actuatorData.getCommand() == "DECREASE TEMP":
            
            try:
            
                #display a blue arrow
                self.sense.set_pixels(self.arrowBlueDec);
                
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
            
            #not valid actuator trigger hence, return false
            return False 
                
                
               
        
    
    
        