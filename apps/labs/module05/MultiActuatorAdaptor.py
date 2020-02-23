'''
Created on Feb 14, 2020

@author: pallaksingh
'''

#import libraries and modules
from sense_hat              import SenseHat
from time                   import sleep
from math                   import floor
import logging

#set the basic configuration to display time, level and the message
logging.getLogger("multi actuator adaptor")
logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.DEBUG)

class MultiActuatorAdaptor(object):
    '''
    classdocs
    '''
    
    #initialize the sense hat
    sense = SenseHat()
    
    #set the rgb values
    #no color
    e = [0, 0, 0]
    
    #red color
    r = [255, 0, 0]
    
    #blue color
    b = [0, 0, 255]
    
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
        
        #if the passed value is not of NoneType
        if actuatorData != None:
        
            #if the actuator should increase the temperature
            if actuatorData.getCommand() == "INCREASE TEMP":
                
                #try printing the corresponding arrow on the led matrix
                try:
                
                    #display a red arrow
                    self.sense.set_pixels(self.arrowRedInc);
                    
                    #logging actuator command
                    logging.info('Triggering actuator to increase temperature')
                    
                    #keep it displayed
                    sleep(3)
                    
                    #clear the matrix           
                    self.sense.clear()
        
                except Exception as e:
                    
                    #if error found during updating actuator, return a false
                    return False
                
                #if successful, return true
                return True
                
               
            #if the actuator should decrease the temperature 
            elif actuatorData.getCommand() == "DECREASE TEMP":
                
                #try printing the corresponding arrow on the led matrix
                try:
                
                    #display a blue arrow
                    self.sense.set_pixels(self.arrowBlueDec);
                    
                    #logging actuator command
                    logging.info('Triggering actuator to decrease temperature')
                    
                    #keep it displayed
                    sleep(3)
                    
                    #clear the matrix
                    self.sense.clear()
                 
                except:
                    
                    #if error found during updating actuator, return a false  
                    return False
                
                #if actuator successful, return true
                return True
            
            #if invalid command to actuator 
            else:

                #not valid temperature actuator trigger hence, return false
                return False 
        
        #if passed value is NoneType
        else:
            
            #return false coz invalid actuator 
            return False
    
    