'''
Created on Jan 14, 2020

@author: pallaksingh
'''
#import libraries
from time               import sleep
from labs.module01      import SystemCpuUtilTask, SystemMemUtilTask
from datetime           import datetime
from labs.common        import LoggerUtil
import logging

#set the basic configuration to display time, level and the message
logging.getLogger("performance logger")
logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.DEBUG)

#log the initial message
logging.info('Starting System Performance Adaptor Thread')

class SystemPerformanceAdaptor(object):
    '''
    classdocs
    '''
    #disable the adaptor initially
    enableAdaptor = False
    
    #constructor takes in variable to control how often and how many times reading is taken
    def __init__(self, rateInSec = 10, numReadings = 15):
        '''
        Constructor
        '''
        #if provided rateInSec, change, else, it defaults to 10
        self.rateInSec = rateInSec
        
        #if provided number of readings, change, else, it defaults to 15
        self.numReadings = numReadings
        
    
    #method for gathering readings from the CPU util task and Mem Util task 
    def run(self):
        
        #instantiate the tasks
        systemCpuUtilTask = SystemCpuUtilTask.SystemCpuUtilTask()
        systemMemUtilTask = SystemMemUtilTask.SystemMemUtilTask()
        
        #adaptor doesn't run if 0 readings set
        if self.numReadings == 0:
            return False
        
        #run the loop as indicated in the numReadings variable
        while self.numReadings > 0:
            
            #if the adaptor is enabled
            if self.enableAdaptor:
                
                #get the readings from the corresponding tasks
                cpuUtil = systemCpuUtilTask.getSensorData()
                memUtil = systemMemUtilTask.getSensorData()
                
                #prepare the string to be logged 
                cpuPerformanceData = 'CPU Utilization: ' + str(cpuUtil)
                memoryPerformanceData = 'Memory Utilization: ' + str(memUtil)
                
                #log the data 
                logging.info(cpuPerformanceData)
                logging.info(memoryPerformanceData)
                
                #decrement as the number of readings by 1 to keep count of how many readings left
                self.numReadings -= 1
                
                #sleep for time indicated in rateInSec
                sleep(self.rateInSec)
                
            else:
                
                #adaptor is disabled
                return False
        
        #the adaptor is done running
        return True        
                
        