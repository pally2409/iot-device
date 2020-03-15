'''
Created on Mar 12, 2020

@author: pallaksingh
'''
#Import libraries and modules
import logging
import json
import asyncio
from labs.common.DataUtil  import DataUtil
from labs.common.SensorData  import SensorData
from aiocoap import *

#Set the basic configuration to display time, level and the message
logging.getLogger("CoapClientConnector")
logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.DEBUG, datefmt='%Y-%m-%d %H:%M:%S')

class CoapClientConnector(object):
    '''
    CoapClientConnector class provides abstraction for Coap related tasks such as
    requesting messages (GET, PUT, POST, DELETE)
    '''
    #Instantiate DataUtil that will convert SensorData to JSON String
    dUtil = DataUtil()

    #Empty constructor as we do not want to initialize anything during instantiation
    def __init__(self):
        '''
        Constructor
        '''
    """
        This method defines the coroutine to send SensorData in the 
        PUT request message to the CoAP server

        @param:             sensorDataString This is a JSON String representation of SensorData object
        @param host         URL for the CoAP server
        @param resourceName Name of the resource to be addressed
        @returns            Returns a boolean value indicating success of the sending the request message
    """
    async def sendSensorData(self, sensorDataString, host, resourceName):

        #Try to send the sensorData in a PUT request message
        try: 

            """
            Create a context bound to all addresses on a random listening port
            and get a context suitable for sending client requests
            """
            context = await Context.create_client_context()

            #Give control to the event loop for 2 seconds and sleep
            await asyncio.sleep(2)

            #Get the payload in bytes by converting SensorData to JSONString using DataUtil  
            payload = sensorDataString.encode()

            #Send the request message to the CoAP server
            request = Message(code=PUT, payload = payload, uri="coap://"+host+"/" + resourceName)
            
            #Wait till you receive the response from the server 
            response = await context.request(request).response
            
            #Log the response code
            logging.info("Received response from CoAP server with response code" + str(response.code))

        #If encountered an error
        except Exception as e:

            #Log the error
            logging.info("Encountered an error: " + str(e))

            #Return false indicating an error
            return False

        #If runs smoothly, return True
        return True
    
    """
        This method converts the SensorData object to JSON string and calls the
        sendSensorData coroutine in the current event loop to send to the CoAP client

        @param sensorData   SensorData object to be sent in the request message
        @param loop         Event loop where the coroutine for sending SensorData JSON string should be executed
        @param host         URL for the CoAP server
        @param resourceName Name of the resource to be addressed
        @returns            Returns a boolean value indicating success of the sending the request message
    """
    def prepareAndSendSensorData(self, sensorData, loop, host, resourceName):

        #Try to call the method for the coroutine that sends the SensorData in a PUT message
        try: 

            #Check if the passed sensorData is an object of SensorData
            if type(sensorData) == SensorData:

                #Convert SensorData object to JSONString
                sensorDataString = self.dUtil.toJsonFromSensorData(sensorData)

                #Format it to pretty printed JSON string (properly indented)
                jsonFormatted = json.loads(sensorDataString)
                prettyJson = json.dumps(jsonFormatted, indent = 2)
                        
                #Log the JSON
                logging.info("Requesting PUT message to CoAP server")
                logging.info(prettyJson)
                logging.info("-----------------------------------------------------------------------------")
                
                #send the SensorData in the PUT request message to the CoAP server 
                loop.run_until_complete(self.sendSensorData(sensorDataString, host, resourceName))

            #if the sensorData is not of type SensorData
            else:
            
                #return false indicating failure
                return False

        #If encountered an error (no running event loop)
        except Exception as e:

            #log the error
            logging.info("Encountered an error: " + str(e))

            #return False indicating failure
            return False

        #Runs successfully, return True indicating success
        return True

    """
        This method calls the method for sending the GET request message to the server

        @param loop         Event loop where the coroutine for sending SensorData JSON string should be executed
        @param host         URL for the CoAP server
        @param resourceName Name of the resource to be addressed
        @returns            Returns a boolean value indicating success of the sending the request message           
    """
    def callGETRequest(self, loop, host, resourceName):

        #Try to call the method for the coroutine that sends the GET message
        try: 

            #Log the message
            logging.info("Sending GET message to CoAP server")

            #call the method to send the GET request message to the CoAP server
            loop.run_until_complete(self.sendGETRequest(host, resourceName))

        #If encountered an error (no running event loop)
        except Exception as e:

            #log the error
            logging.info("Encountered an error: " + str(e))

            #return False indicating failure
            return False

        #Runs successfully, return True indicating success
        return True

    """
        This method sends a GET request message to the server

        @param host         URL for the CoAP server
        @param resourceName Name of the resource to be 
        @returns            Returns a boolean value indicating success of the sending the request message
    """
    async def sendGETRequest(self, host, resourceName):

        """
        Create a context bound to all addresses on a random listening port
        and get a context suitable for sending client requests
        """
        context = await Context.create_client_context()

        #Send the request message to the CoAP server
        request = Message(code=GET, uri="coap://"+host+"/" + resourceName)

        #Get for a response from the server
        try:

            #Response holds the response gathered from the server, waits until the response from the server
            response = await context.request(request).response

        #If an error occured
        except Exception as e:

            #Log the error
            logging.info("Failed to fetch resource")

            #return False indicating failure
            return False

        #If no error occured while getting the response 
        else:

            #log the response code
            logging.info("Received response from the server with response code" + str(response.code))

            #return True indicating success
            return True

    """
        This method calls the method for sending the DELETE request message to the server

        @param loop         Event loop where the coroutine for sending the DELETE request message should be executed
        @param host         URL for the CoAP server
        @param resourceName Name of the resource to be addressed
        @returns            Returns a boolean value indicating success of the sending the request message
    """
    def callDELETERequest(self, loop, host, resourceName):

        #Try to call the method for the coroutine that sends the GET message
        try: 

            #Log the message
            logging.info("Sending DELETE message to CoAP server")

            #call the method to send the DELETE request message to the CoAP server
            loop.run_until_complete(self.sendDELETERequest(host, resourceName))

        #If encountered an error (no running event loop)
        except Exception as e:

            #log the error
            logging.info("Encountered an error: " + str(e))

            #return False indicating failure
            return False

        #Runs successfully, return True indicating success
        return True



    """
        This method sends a DELETE request message to the server

        @param host         URL for the CoAP server
        @param resourceName Name of the resource to be addressed
        @returns            Returns a boolean value indicating success of the sending the request message
    """
    async def sendDELETERequest(self, host, resourceName):

        """
        Create a context bound to all addresses on a random listening port
        and get a context suitable for sending client requests
        """
        context = await Context.create_client_context()

        #Send the request message to the CoAP server
        request = Message(code=DELETE, uri="coap://"+host+"/" + resourceName)

        #Get for a response from the server
        try:

            #Response holds the response gathered from the server, waits until the response from the server
            response = await context.request(request).response

        #If an error occured
        except Exception as e:

            #Log the error
            logging.info("Failed to fetch resource")

            #return False indicating failure
            return False

        #If no error occured while getting the response 
        else:

            #log the response code
            logging.info("Received response from the server with response code" + str(response.code))

            #return True indicating success
            return True

    """
        This method calls the method for sending the POST request message to the server

        @param loop         Event loop where the coroutine for sending the POST request message should be executed
        @param text         Piece of text which should be posted
        @param host         URL for the CoAP server
        @param resourceName Name of the resource to be addressed
        @returns            Returns a boolean value indicating success of the sending the request message
    """
    def callPOSTRequest(self, loop, text, host, resourceName):

        #Try to call the method for the coroutine that sends the GET message
        try: 

            #Log the message
            logging.info("Sending POST message to CoAP server")

            #call the method to send the POST request message to the CoAP server
            loop.run_until_complete(self.sendPOSTRequest(text, host, resourceName))

        #If encountered an error (no running event loop)
        except Exception as e:

            #log the error
            logging.info("Encountered an error: " + str(e))

            #return False indicating failure
            return False

        #Runs successfully, return True indicating success
        return True

    """
        This method sends a post request message to the server

        @param loop         Event loop where the coroutine for sending SensorData JSON string should be executed
        @param host         URL for the CoAP server
        @param resourceName Name of the resource to be addressed
        @returns            Returns a boolean value indicating success of the sending the request message
    """
    async def sendPOSTRequest(self, text, host, resourceName):

        """
        Create a context bound to all addresses on a random listening port
        and get a context suitable for sending client requests
        """
        context = await Context.create_client_context()

        #Send the request message to the CoAP server
        request = Message(code=POST, payload = text.encode(), uri="coap://"+host+"/" + resourceName)

        #Get for a response from the server
        try:

            #Response holds the response gathered from the server, waits until the response from the server
            response = await context.request(request).response

        #If an error occured
        except Exception as e:

            #Log the error
            logging.info("Failed to fetch resource")

            #return False indicating failure
            return False

        #If no error occured while getting the response 
        else:

            #log the response code
            logging.info("Received response from the server with response code" + str(response.code))

            #return True indicating success
            return True