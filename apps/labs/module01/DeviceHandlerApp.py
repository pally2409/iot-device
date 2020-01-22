'''
Created on Jan 14, 2020

@author: pallaksingh
'''

from labs.module01 import SystemPerformanceAdaptor
import threading


if __name__ == '__main__':
    
    systemPerformanceAdaptor = SystemPerformanceAdaptor.SystemPerformanceAdaptor()
    systemPerformanceAdaptor.daemon = True
    systemPerformanceAdaptor.enableAdaptor = True
    threadSystemPerformanceAdaptor = threading.Thread(target = systemPerformanceAdaptor.run)
    threadSystemPerformanceAdaptor.start()
