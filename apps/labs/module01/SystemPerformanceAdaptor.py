'''
Created on Jan 14, 2020

@author: pallaksingh
'''
from time               import sleep
from labs.module01      import SystemCpuUtilTask, SystemMemUtilTask
import logging


class SystemPerformanceAdaptor(object):
    '''
    classdocs
    '''
    enableAdaptor = False
    rateInSec = 0

    def __init__(self, rateInSec = 10):
        '''
        Constructor
        '''
        self.rateInSec = rateInSec
        logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.DEBUG)
        logging.info("Starting System Performance Adaptor Thread")

    def run(self):
        systemCpuUtilTask = SystemCpuUtilTask.SystemCpuUtilTask()
        systemMemUtilTask = SystemMemUtilTask.SystemMemUtilTask()
        while True:
            if self.enableAdaptor:
                cpuUtil = systemCpuUtilTask.getSensorData()
                memUtil = systemMemUtilTask.getSensorData()
                cpuPerformanceData = 'CPU Utilization: ' + str(cpuUtil)
                memoryPerformanceData = 'Memory Utilization: ' + str(memUtil)
                logging.info(cpuPerformanceData)
                logging.info(memoryPerformanceData)
                sleep(self.rateInSec)
        