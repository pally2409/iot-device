'''
Created on Feb 14, 2020

@author: pallaksingh
'''

#import libraries and modules
from sense_hat              import SenseHat
from time                   import sleep
import logging
from math                   import floor

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
        
    #this method is responsible for actuation if the trigger is valid
    def updateActuator(self, actuatorDatas) -> bool:
        
        for actuatorData in actuatorDatas:
        
            #if the passed value is not of NoneType
            if actuatorData != None:
            
                #if the actuator should increase the temperature
                if actuatorData.getCommand() == "DISPLAY I2C Humidity":
                    
                    logging.info("im in actuator i2c")
                    
                    #try printing the corresponding arrow on the led matrix
                    try:
                    
                        val = actuatorData.getValue()
                        
                        #clear the matrix           
                        self.sense.clear()
                        
                        if val < 10:
                            
                            logging.info("value less than 10")
                            
                            #display a red text indicating reading from i2c
                            self.sense.show_letter(str(int(floor(val))), text_colour = self.r);
                            
                            
                        else:
                            
                            logging.info("value more than 10")
                            
                            self.sense.show_message(str(int(floor(val))), text_colour = self.r)
                        
                        #logging actuator command
                        logging.info('Displaying Humidity from I2C Bus on actuator')
                        
                        
            
                    except Exception as e:
                        
                        print(e)
                        
                        logging.info("exception occured in actuator")
                        
                        #if error found during updating actuator, return a false
                        return False
                    
                    #if successful, return true
                    return True
                    
                   
                #if the actuator should decrease the temperature 
                elif actuatorData.getCommand() == "DISPLAY SENSE HAT API Humidity":
                    
                    logging.info("im in actuator sense hat")
                    
                    #try printing the corresponding arrow on the led matrix
                    try:
                        
                        logging.info("im in actuator sense hat try")
                    
                        #display a blue text indicating reading from sense hat
                        val = actuatorData.getValue()
                        
                        #clear the matrix
                        self.sense.clear()
                        
                        if val < 10:
                            
                            logging.info("value less than 10")
                            
                            #display a red text indicating reading from i2c
                            self.sense.show_letter(str(int(floor(val))), text_colour = self.b);
                            
                        else:
                            
                            logging.info("value more than 10")
                            
                            self.sense.show_message(str(int(floor(val))), text_colour = self.b)
                        
                        #logging actuator command
                        logging.info('Displaying Humidity from SenseHAT API on actuator')
                        

                        
                        
                     
                    except:
                        
                        print(e)
                        
                        logging.info("exception occured in actuator")
                        
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
    
    