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
    
    #red color indicates i2c output
    r = [255, 0, 0]
    
    #blue color indicates sense_hat api output
    b = [0, 0, 255]
 
    def __init__(self):
        '''
        Constructor
        '''
        
    #this method is responsible for actuation if the trigger is valid (in this case, it is a display on the sense hat led matrix)
    def updateActuator(self, actuatorDatas) -> bool:
        
        #if passed value is NoneType
        if actuatorDatas == None:
                
            #return false coz invalid actuator 
            return False
        
        #iterate through the actuatorData in the list of actuatorData passed
        for actuatorData in actuatorDatas:
            
            #if the actuator should display humidity read directly from 12c bus
            if actuatorData.getCommand() == "DISPLAY I2C Humidity":
                    
                #try printing the corresponding value on the led matrix
                try:
                    
                    #get the value to display
                    val = actuatorData.getValue()
                        
                    #clear the matrix           
                    self.sense.clear()
                        
                    #if value is less than 10 only print a letter
                    if val < 10:
                                 
                        #display a red letter indicating reading from i2c
                        self.sense.show_letter(str(int(floor(val))), text_colour = self.r);
                            
                    #if value 10 or more    
                    else:
                            
                        #display a red scroll message indicating the reading from i2c
                        self.sense.show_message(str(int(floor(val))), text_colour = self.r)
  
                #if unable to print on sensehat
                except Exception as e:
                        
                    #log an error message
                    logging.info("Exception occured in I2C Actuation")
                    
                   
            #if the actuator should display humidity read from SenseHAT API 
            elif actuatorData.getCommand() == "DISPLAY SENSE HAT API Humidity":
                    
                #try printing the corresponding value on the led matrix
                try:
 
                    #get the value to display
                    val = actuatorData.getValue()
                        
                    #clear the matrix
                    self.sense.clear()
                        
                    #if value is less than 10 only print a letter
                    if val < 10:
                            
                        #display a blue letter indicating reading from sense hat api
                        self.sense.show_letter(str(int(floor(val))), text_colour = self.b);
                        
                    #if value 10 or more       
                    else:
                            
                        #display a blue scroll message indicating the reading from sense hat api
                        self.sense.show_message(str(int(floor(val))), text_colour = self.b)

                #if unable to print on sensehat 
                except:
                        
                    #log an error message
                    logging.info("exception occured in SenseHAT API actuator")
                        
                
            #if invalid command to actuator 
            else:
    
                #not valid actuator command hence, return false
                return False 
            
        #if everything fine, return true    
        return True
    
    