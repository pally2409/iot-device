'''
Created on Jan 23, 2020

@author: pallaksingh
'''
import logging
class LoggerUtil(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
    def setupLogger(self, name, log_file, fmt, level = logging.INFO):
        handler = logging.FileHandler(log_file)
        handler.setFormatter(fmt)
        logger = logging.getLogger(name)
        logger.setLevel(level)
        logger.addHandler(handler)
        
        return logger