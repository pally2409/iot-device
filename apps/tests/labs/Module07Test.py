import unittest
import asyncio										
from labs.module07.CoapClientConnector 				import CoapClientConnector
from labs.module07.DeviceDataManager 				import DeviceDataManager
from labs.module07.TempSensorAdaptor 				import TempSensorAdaptor
from labs.module07.TempSensorAdaptorTask 			import TempSensorAdaptorTask
from labs.common.SensorData							import SensorData

"""
Test class for all requisite Module07 functionality.

Instructions:
1) Rename 'testSomething()' method such that 'Something' is specific to your needs; add others as needed, beginning each method with 'test...()'.
2) Add the '@Test' annotation to each new 'test...()' method you add.
3) Import the relevant modules and classes to support your tests.
4) Run this class as unit test app.
5) Include a screen shot of the report when you submit your assignment.

Please note: While some example test cases may be provided, you must write your own for the class.
"""
class Module07Test(unittest.TestCase):

	"""
	Use this to setup your tests. This is where you may want to load configuration
	information (if needed), initialize class-scoped variables, create class-scoped
	instances of complex objects, initialize any requisite connections, etc.
	"""
	def setUp(self):

		"""
		Initialize TempSensorAdaptor, TempSensorAdaptorTask, DeviceDataManager 
		and CoapClientConnector (Modules in Module7)
		"""
		self.tempSensorAdaptor 		= 		TempSensorAdaptor()
		self.tempSensorAdaptorTask	= 		TempSensorAdaptorTask()
		self.deviceDataManager 		= 		DeviceDataManager()
		self.coapClientConnector 	= 		CoapClientConnector()

	"""
	Use this to tear down any allocated resources after your tests are complete. This
	is where you may want to release connections, zero out any long-term data, etc.
	"""
	def tearDown(self):

		#Set the references for the modules in Module 7 to None to release any resources
		self.deviceDataManager = None
		self.coapClientConnector = None
		self.tempSensorAdaptor = None
		self.tempSensorAdaptorTask = None

	"""
	This method tests the sendSensorData() of CoapClientConnector module, 
	it checks for success (true) when valid host and resource name are given to 
	the method, and false when invalid host and resource name are given to the method
	"""
	def testSendSensorData(self):
		
		#Get the current event loop 
		loop = asyncio.get_event_loop()

		#Assert True when valid host and resource are given
		self.assertEqual(loop.run_until_complete(self.coapClientConnector.sendSensorData("TestString", "pallybook.lan", "Temp")), True)

		#Assert False when invalid host and resource are given
		self.assertEqual(loop.run_until_complete(self.coapClientConnector.sendSensorData("TestString", "notavalidhost", "TestResource")), False)

	"""
	This method tests the sendGETRequest() of CoapClientConnector module, 
	it checks for success (true) when valid host and resource name are given to 
	the method, and false when invalid host and resource name are given to the method
	"""
	def testSendGETRequest(self):
		
		#Get the current event loop 
		loop = asyncio.get_event_loop()
		
		#Assert True when valid host and resource are given
		self.assertEqual(loop.run_until_complete(self.coapClientConnector.sendGETRequest("pallybook.lan", "Temp")), True)

		#Assert False when invalid host and resource are given
		self.assertEqual(loop.run_until_complete(self.coapClientConnector.sendGETRequest("notavalidhost", "TestResource")), False)

	"""
	This method tests the sendDELETERequest() of CoapClientConnector module, 
	it checks for success (true) when valid host and resource name are given to 
	the method, and false when invalid host and resource name are given to the method
	"""
	def testSendDELETERequest(self):
		
		#Get the current event loop 
		loop = asyncio.get_event_loop()
		
		#Assert True when valid host and resource are given
		self.assertEqual(loop.run_until_complete(self.coapClientConnector.sendDELETERequest("pallybook.lan", "Temp")), True)

		#Assert False when invalid host and resource are given
		self.assertEqual(loop.run_until_complete(self.coapClientConnector.sendDELETERequest("notavalidhost", "TestResource")), False)

	"""
	This method tests the sendPOSTRequest() of CoapClientConnector module, 
	it checks for success (true) when valid host and resource name are given to 
	the method, and false when invalid host and resource name are given to the method
	"""
	def testSendPOSTRequest(self):
		
		#Get the current event loop 
		loop = asyncio.get_event_loop()
		
		#Assert True when valid host and resource are given
		self.assertEqual(loop.run_until_complete(self.coapClientConnector.sendPOSTRequest("Testing text", "pallybook.lan", "Temp")), True)

		#Assert False when invalid host and resource are given
		self.assertEqual(loop.run_until_complete(self.coapClientConnector.sendPOSTRequest("Testing text", "notavalidhost", "TestResource")), False)

	"""
	This method tests the prepareAndSendSensorData() of CoapClientConnectorModule. It
	tests for successful running when valid parameters are given(sensor data and event loop)
	And tests for indication of failure when invalid parameters are given (not sensor data type and
	no current event loop exists) 
	"""
	def testPrepareAndSendSensorData(self):

		#Get the current event loop
		loop = asyncio.get_event_loop()

		#Assert false when the event loop given is running but not valid SensorData given
		self.assertEqual(self.coapClientConnector.prepareAndSendSensorData("Hello", loop, "pallybook.lan", "Temp"), False)

		#Create a sensorData object
		sensorData = SensorData()

		#add a value to SensorData
		sensorData.addValue(9)

		#Assert true when given the current event loop is running and valid SensorData
		self.assertEqual(self.coapClientConnector.prepareAndSendSensorData(sensorData, loop, "pallybook.lan", "Temp"), True)

		#Get a new event loop
		loop = asyncio.new_event_loop()

		#Stop the loop such that there is no event loop currently
		loop.stop()

		#Assert false when the event loop given is not running but valid SensorData
		self.assertEqual(self.coapClientConnector.prepareAndSendSensorData(sensorData, loop, "pallybook.lan", "Temp"), False)

	"""
	This method tests the callGETRequest() of CoapClientConnectorModule. It
	tests for successful running when valid parameters are given(event loop)
	And tests for indication of failure when invalid parameters are given (no current event loop 
	exists) 
	"""
	def testCallGETRequest(self):

		#Get the current event loop
		loop = asyncio.get_event_loop()

		#Assert true when given the current event loop is running
		self.assertEqual(self.coapClientConnector.callGETRequest(loop, "pallybook.lan", "Temp"), True)

		#Get a new event loop
		loop = asyncio.new_event_loop()

		#Stop the loop such that there is no event loop currently
		loop.stop()

		#Assert false when the event loop given is not running 
		self.assertEqual(self.coapClientConnector.callGETRequest(loop, "pallybook.lan", "Temp"), False)

	"""
	This method tests the callDELETERequest() of CoapClientConnectorModule. It
	tests for successful running when valid parameters are given(event loop)
	And tests for indication of failure when invalid parameters are given (no current event loop 
	exists) 
	"""
	def testCallDELETERequest(self):

		#Get the current event loop
		loop = asyncio.get_event_loop()

		#Assert true when given the current event loop is running
		self.assertEqual(self.coapClientConnector.callDELETERequest(loop, "pallybook.lan", "Temp"), True)

	"""
	This method tests the callPOSTRequest() of CoapClientConnectorModule. It
	tests for successful running when valid parameters are given(event loop)
	And tests for indication of failure when invalid parameters are given (no current event loop 
	exists) 
	"""
	def testCallDELETERequest(self):

		#Get the current event loop
		loop = asyncio.get_event_loop()

		#Assert true when given the current event loop is running
		self.assertEqual(self.coapClientConnector.callPOSTRequest(loop, "Hello", "pallybook.lan", "Temp"), True)

		#Get a new event loop
		loop = asyncio.new_event_loop()

		#Stop the loop such that there is no event loop currently
		loop.stop()

		#Assert false when the event loop given is not running 
		self.assertEqual(self.coapClientConnector.callPOSTRequest(loop, "Hello", "pallybook.lan", "Temp"), False)

		#Get a new event loop
		loop = asyncio.new_event_loop()

		#Stop the loop such that there is no event loop currently
		loop.stop()

		#Assert false when the event loop given is not running 
		self.assertEqual(self.coapClientConnector.callDELETERequest(loop, "pallybook.lan", "Temp"), False)

	"""
	This method tests the callPOSTRequest() of CoapClientConnectorModule. It
	tests for successful running when valid parameters are given(event loop)
	And tests for indication of failure when invalid parameters are given (no current event loop 
	exists) 
	"""
	def testCallDELETERequest(self):

		#Get the current event loop
		loop = asyncio.get_event_loop()

		#Assert true when given the current event loop is running
		self.assertEqual(self.coapClientConnector.callPOSTRequest(loop, "Hello", "pallybook.lan", "Temp"), True)

		#Get a new event loop
		loop = asyncio.new_event_loop()

		#Stop the loop such that there is no event loop currently
		loop.stop()

		#Assert false when the event loop given is not running 
		self.assertEqual(self.coapClientConnector.callPOSTRequest(loop, "Hello", "pallybook.lan", "Temp"), False)

		#Get a new event loop
		loop = asyncio.new_event_loop()

		#Stop the loop such that there is no event loop currently
		loop.stop()

		#Assert false when the event loop given is not running 
		self.assertEqual(self.coapClientConnector.callDELETERequest(loop, "pallybook.lan", "Temp"), False)

	"""
	This method tests the setCoapClient() method of the TempSensorAdaptor
	It checks for false when sent a null instead of a reference of type CoapClientConnector, and true when 
	appropriate reference type passed
	"""
	def testSetMqttClientConnector(self):
		
		#Set an invalid reference and assert False for failure too assign
		self.assertEqual(False, self.tempSensorAdaptor.setCoapClient(None))

		#Set a valid reference and assert True for successful assignment
		self.assertEqual(True, self.tempSensorAdaptor.setCoapClient(self.coapClientConnector))
	
	"""
	This method tests the start() method of the TempSensorAdaptor
	It checks for false if the number of readings needed is 0 
	or if fetcher is not enabled. Checks true if the readings are taken
	"""
	def testStart(self):
		
		#Check for false when there is no reference to MQTT client connector
		self.assertEqual(False, self.tempSensorAdaptor.start())
		
		#Set the MQTT client connector reference to the current reference 
		self.tempSensorAdaptor.setCoapClient(self.coapClientConnector)
		
		#Enable the fetcher
		self.tempSensorAdaptor.enableFetcher = True
		
		#Change numReadings to a small finite value to check
		self.tempSensorAdaptor.numReadings = 1
		
		#Change sleep time (rateInSec) to a small amount
		self.tempSensorAdaptor.rateInSec = 1
		
		#Run when numReadings > 0 and adaptor is enabled, assert True for readings were taken
		self.assertEqual(True, self.tempSensorAdaptor.start())
		
		#Change numReadings to 0
		self.tempSensorAdaptor.numReadings = 0
		
		#Run when numReadings = 0 and fetcher is enabled, should return false because readings weren't taken
		self.assertEqual(False, self.tempSensorAdaptor.start())
		
		#Disable the fetcher
		self.tempSensorAdaptor.enableFetcher = False
		
		#Change readings to > 0
		self.tempSensorAdaptor.numReadings = 1
		
		#run when numReadings > 0 and Fetcher is disabled, should return false because readings weren't taken
		self.assertEqual(False, self.tempSensorAdaptor.start())

	"""
	This method tests the getTemperature() method of the TempSensorAdaptorTask
	It checks for difference between the gathered temperature from the method 
	should not exceed 55 degrees celsius or be less than -30 degrees celsius 
	(A VALID TEMPERATURE RANGE)
	"""
	def testGetTemperature(self):

		#Get the temperature 
		temperature = self.tempSensorAdaptorTask.getTemperature()

		#Assert if less than 55 degrees
		self.assertTrue(temperature.getCurrentValue() < 55)

		#Assert if greater than -30 degrees
		self.assertTrue(temperature.getCurrentValue() > -30)

	"""
	This method tests the run() method of the DeviceDataManager
	It asserts true always
	"""
	def testRun(self):

		#Set the number of readings to 1
		self.deviceDataManager.tempSensorAdaptor.numReadings = 1

		#Assert true as it is always successful
		self.deviceDataManager.run()

if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testName']
	unittest.main()