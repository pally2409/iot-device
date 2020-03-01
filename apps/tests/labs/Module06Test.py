#Import libraries and modules
import unittest
from time import sleep
from labs.common.SensorData import SensorData
from labs.common.ActuatorData import ActuatorData
"""
Test class for all requisite Module06 functionality.

Instructions:
1) Rename 'testSomething()' method such that 'Something' is specific to your needs; add others as needed, beginning each method with 'test...()'.
2) Add the '@Test' annotation to each new 'test...()' method you add.
3) Import the relevant modules and classes to support your tests.
4) Run this class as unit test app.
5) Include a screen shot of the report when you submit your assignment.

Please note: While some example test cases may be provided, you must write your own for the class.
"""
from labs.module06.MqttClientConnector import MqttClientConnector
from labs.module06.DeviceDataManager import DeviceDataManager
from labs.module06.MultiSensorAdaptor import MultiSensorAdaptor
from labs.module06.TempSensorAdaptorTask import TempSensorAdaptorTask
class Module06Test(unittest.TestCase):

	"""
	Use this to setup your tests. This is where you may want to load configuration
	information (if needed), initialize class-scoped variables, create class-scoped
	instances of complex objects, initialize any requisite connections, etc.
	"""
	def setUp(self):
		
		#initialize the modules in Module 6
		self.deviceDataManager = DeviceDataManager()
		self.mqttClientConnector = MqttClientConnector()
		self.multiSensorAdaptor = MultiSensorAdaptor()
		self.tempSensorAdaptorTask = TempSensorAdaptorTask()

	"""
	Use this to tear down any allocated resources after your tests are complete. This
	is where you may want to release connections, zero out any long-term data, etc.
	"""
	def tearDown(self):
		
		#set the references for the modules in Module 6 to None to release any resources
		self.deviceDataManager = None
		self.mqttClientConnector = None
		self.multiSensorAdaptor = None
		self.tempSensorAdaptorTask = None
		
	"""
	This method tests the connect() method of the MqttClientConnector
	It checks for successful connection when the correct host and port are given 
	and if the program crashes if incorrect port/host is given
	"""
	def testConnect(self):
		
		#Call the connect method of MqttClientConnector with accurate values
		self.mqttClientConnector.connect("broker.hivemq.com", 1883)
		
		#Give it time to connect
		sleep(1)
		
		#Assert isConnected is True for successful connection
		self.assertEqual(self.mqttClientConnector.client.is_connected(), True)
		
		#Call the connect method of MqttClientConnector with invalid host
		self.mqttClientConnector.connect("broker.hivemqqqq.com", 1883)
		
		#Assert isConnected for failure to connnect 
		self.assertEqual(self.mqttClientConnector.client.is_connected(), False)
	
	"""
	This method tests the testPublishSensorCommand() method of the MqttClientConnector
	It checks for false when failure to publish (due to no connection), and true when 
	publishes successfully
	"""
	def testPublishSensorCommand(self):
		
		#Call the connect method of MqttClientConnector with valid values
		self.mqttClientConnector.connect("broker.hivemq.com", 1883)
		
		#Let it connect
		sleep(2)
		
		#Create SensorData object and add a valid value
		sensorData = SensorData()
		sensorData.addValue(9)
		
		#Publish and assert true for successful publishing
		self.assertEqual(True, self.mqttClientConnector.publishSensorCommand(sensorData, 2))

		#Call the connect method of MqttClientConnector with invalid host value
		self.mqttClientConnector.connect("brosdf235iytksg", 1883)
		
		#Let it connect
		sleep(2)
		
		#Create sensorData and add a valid value
		sensorData = SensorData()
		sensorData.addValue(9)
		
		#Publish to topic and assert False for failure to publish
		self.assertEqual(False, self.mqttClientConnector.publishSensorCommand(sensorData, 2))

		#Pass a null to method and assert False for failure to publish
		self.assertEqual(False, self.mqttClientConnector.publishSensorCommand(None, 2))

	"""
	This method tests the testPublishActuatorCommand() method of the MqttClientConnector
	It checks for false when failure to publish (due to no connection), and true when 
	publishes successfully
	"""
	def testPublishActuatorCommand(self):
		
		#Call the connect method of MqttClientConnector with valid values
		self.mqttClientConnector.connect("broker.hivemq.com", 1883)
		
		#Let it connect
		sleep(2)
		
		#Create ActuatorData object and add a valid command
		actuatorData = ActuatorData()
		actuatorData.setCommand("Test Command")
		
		#Publish to topic and assert true for successful publishing
		self.assertEqual(True, self.mqttClientConnector.publishActuatorCommand(actuatorData, 2))

		#Call the connect method of MqttClientConnector with invalid values
		self.mqttClientConnector.connect("brosdf235iytksg", 1883)
		
		#Let it connect
		sleep(2)
		
		#Publish to topic and assert False for failure to publish
		self.assertEqual(False, self.mqttClientConnector.publishActuatorCommand(actuatorData, 2))
		
		#Pass a null to method and assert False for failure to publish
		self.assertEqual(False, self.mqttClientConnector.publishActuatorCommand(None, 2))

	"""
	This method tests the testSubscribeToActuatorCommands() method of the MqttClientConnector
	It checks for false when failure to subscribe(due to no connection), and true when 
	subscribes successfully
	"""
	def testSubscribeToActuatorCommands(self):
		
		#Call the connect method of MqttClientConnector with valid values
		self.mqttClientConnector.connect("broker.hivemq.com", 1883)
		
		#Let it connect
		sleep(2)
		
		#Subscribe to topic and assert true for successful subscription
		self.assertEqual(True, self.mqttClientConnector.subscribeToActuatorCommands(1, "TestingTopic"))

		#Call the connect method of MqttClientConnector with invalid values
		self.mqttClientConnector.connect("brosdf235iytksg", 1883)
		
		#Let it connect
		sleep(2)
		
		#Publish to topic and assert False for failure to subscribe
		self.assertEqual(False, self.mqttClientConnector.subscribeToActuatorCommands(1, "TestingTopic"))
		
	"""
	This method tests the testSubscribeToActuatorCommands() method of the MqttClientConnector
	It checks for false when failure to subscribe(due to no connection), and true when 
	subscribes successfully
	"""
	def testSubscribeToSensorCommands(self):
		
		#Call the connect method of MqttClientConnector with valid values
		self.mqttClientConnector.connect("broker.hivemq.com", 1883)
		
		#Let it connect
		sleep(2)
		
		#Subscribe to topic and assert true for successful subscription
		self.assertEqual(True, self.mqttClientConnector.subscribeToSensorCommands(1, "TestingTopic"))

		#Call the connect method of MqttClientConnector with invalid values
		self.mqttClientConnector.connect("brosdf235iytksg", 1883)
		
		#Let it connect
		sleep(2)
		
		#Publish to topic and assert False for failure to subscribe
		self.assertEqual(False, self.mqttClientConnector.subscribeToSensorCommands(1, "TestingTopic"))

	"""
	This method tests the setMqttClient() method of the MultiSensorAdaptor
	It checks for false when sent a null instead of a reference of type MqttClientConnector, and true when 
	appropriate reference type passed
	"""
	def testSetMqttClientConnector(self):
		
		#Set a valid reference and assert True for successful assignment
		self.assertEqual(False, self.multiSensorAdaptor.setMqttClient(None))

		#Set an invalid reference and assert False for failure too assign
		self.assertEqual(True, self.multiSensorAdaptor.setMqttClient(self.mqttClientConnector))
	
	"""
	This method tests the start() method of the MultiSensorAdaptor
	It checks for false if the number of readings needed is 0 
	or if fetcher is not enabled. Checks true if the readings are taken
	"""
	def testStart(self):
		
		#Check for false when there is no reference to MQTT client connector
		self.assertEqual(False, self.multiSensorAdaptor.start())
		
		#Set the MQTT client connector reference to the current reference 
		self.multiSensorAdaptor.setMqttClient(self.mqttClientConnector)
		
		#Enable the fetcher
		self.multiSensorAdaptor.enableFetcher = True
		
		#Change numReadings to a small finite value to check
		self.multiSensorAdaptor.numReadings = 1
		
		#Change sleep time (rateInSec) to a small amount
		self.multiSensorAdaptor.rateInSec = 1
		
		#Run when numReadings > 0 and adaptor is enabled, assert True for readings were taken
		self.assertEqual(True, self.multiSensorAdaptor.start())
		
		#Change numReadings to 0
		self.multiSensorAdaptor.numReadings = 0
		
		#Run when numReadings = 0 and fetcher is enabled, should return false because readings weren't taken
		self.assertEqual(False, self.multiSensorAdaptor.start())
		
		#Disable the fetcher
		self.multiSensorAdaptor.enableFetcher = False
		
		#Change readings to > 0
		self.multiSensorAdaptor.numReadings = 1
		
		#run when numReadings > 0 and Fetcher is disabled, should return false because readings weren't taken
		self.assertEqual(False, self.multiSensorAdaptor.start())

if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testName']
	unittest.main()