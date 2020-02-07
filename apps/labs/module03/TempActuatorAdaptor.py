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


    #initialize upward red arrow to indicate actuatior increasing my temperature
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
    
    #initialize downward blue arrow to indicate actuatior increasing my temperature
    arrowBlueDec = [
                e,e,e,r,r,e,e,e,
                e,e,e,r,r,e,e,e,
                e,e,e,r,r,e,e,e,
                e,e,e,r,r,e,e,e,
                r,e,e,r,r,e,e,r,
                e,r,e,r,r,e,r,e,
                e,e,r,r,r,r,e,e,
                e,e,e,r,r,e,e,e
        ]
 

    def __init__(self):
        '''
        Constructor
        '''
        
        
    #responsible for actuation
    def updateActuator(self, actuatorData) -> bool:
        
        #if the actuator should increase the temperature
        if actuatorData.getCommand().equals("INCREASE TEMP"):
            
            #display a red arrow
            self.sense.set_pixel(self.arrowRedInc);
            
            sleep(3)
            
            self.sense.clear()
           
        #if the actuator should decrease the temperature 
        else:
            
            #display a blue arrow
            self.sense.set_pixel(self.arrowBlueDec);
            
            sleep(3)
            
            self.sense.clear()
               
        return 
    
    
        