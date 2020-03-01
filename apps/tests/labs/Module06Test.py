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
		
		pass

	"""
	Use this to tear down any allocated resources after your tests are complete. This
	is where you may want to release connections, zero out any long-term data, etc.
	"""
	def tearDown(self):
		
		#initialize the modules in Module 6
		self.deviceDataManager = None
		self.mqttClientConnector = None
		self.multiSensorAdaptor = None
		self.tempSensorAdaptorTask = None
		
		pass

	"""
	This method tests the connect() method of the MqttClientConnector
	It checks when the correct host and port are given and when incorrect port is given
	"""
	def testConnect(self):
		
		#call the connect method of MqttClientConnector with accurate values
		self.mqttClientConnector.connect("broker.hivemq.com", 1883)
		
		sleep(1)
		
		#check that isConnected should be true
		self.assertEqual(self.mqttClientConnector.client.is_connected(), True)
		
		#call the connect method of MqttClientConnector
		self.mqttClientConnector.connect("broker.hivemqqqq.com", 1883)
		
		#check that isConnected should be true
		self.assertEqual(self.mqttClientConnector.client.is_connected(), False)
		
		pass
	
	"""
	This method tests the testPublishSensorCommand() method of the MqttClientConnector
	It checks for false when failure to publish, and true when publishes properly
	"""
	def testPublishSensorCommand(self):
		
		#call the connect method of MqttClientConnector with accurate values
		self.mqttClientConnector.connect("broker.hivemq.com", 1883)
		
		sleep(2)
		
		#create sensorData
		sensorData = SensorData()
		sensorData.addValue(9)
		
		#publish to topic and check true
		self.assertEqual(True, self.mqttClientConnector.publishSensorCommand(sensorData, 2))

		#call the connect method of MqttClientConnector with inaccurate values
		self.mqttClientConnector.connect("brosdf235iytksg", 1883)
		
		sleep(2)
		
		#create sensorData
		sensorData = SensorData()
		sensorData.addValue(9)
		
		#publish to topic and check true
		self.assertEqual(False, self.mqttClientConnector.publishSensorCommand(sensorData, 2))

		#send a null and check for false
		self.assertEqual(False, self.mqttClientConnector.publishSensorCommand(None, 2))
		
		pass
	
	"""
	This method tests the testPublishActuatorCommand() method of the MqttClientConnector
	It checks for false when failure to publish, and true when publishes properly
	"""
	def testPublishActuatorCommand(self):
		
		#call the connect method of MqttClientConnector with accurate values
		self.mqttClientConnector.connect("broker.hivemq.com", 1883)
		
		sleep(2)
		
		#create actuatorData
		actuatorData = ActuatorData()
		actuatorData.setCommand("Test Command")
		
		#publish to topic and check true
		self.assertEqual(True, self.mqttClientConnector.publishActuatorCommand(actuatorData, 2))

		#call the connect method of MqttClientConnector with inaccurate values
		self.mqttClientConnector.connect("brosdf235iytksg", 1883)
		
		sleep(2)
		
		#publish to topic and check true
		self.assertEqual(False, self.mqttClientConnector.publishActuatorCommand(actuatorData, 2))
		
		#send a null and check for false
		self.assertEqual(False, self.mqttClientConnector.publishActuatorCommand(None, 2))

		pass
	
	
	"""
	This method tests the testSubscribeToActuatorCommands() method of the MqttClientConnector
	It checks for false when failure to subscribe, and true when subscribes properly
	"""
	def testSubscribeToActuatorCommands(self):
		
		#call the connect method of MqttClientConnector with accurate values
		self.mqttClientConnector.connect("broker.hivemq.com", 1883)
		
		sleep(2)
		
		#publish to topic and check true
		self.assertEqual(True, self.mqttClientConnector.subscribeToActuatorCommands("TestingTopic", 1))

		#call the connect method of MqttClientConnector with inaccurate values
		self.mqttClientConnector.connect("brosdf235iytksg", 1883)
		
		sleep(2)
		
		#publish to topic and check true
		self.assertEqual(False, self.mqttClientConnector.subscribeToActuatorCommands("TestingTopic", 1))

		pass
	
	
	"""
	This method tests the testSubscribeToActuatorCommands() method of the MqttClientConnector
	It checks for false when failure to subscribe, and true when subscribes properly
	"""
	def testSubscribeToSensorCommands(self):
		
		#call the connect method of MqttClientConnector with accurate values
		self.mqttClientConnector.connect("broker.hivemq.com", 1883)
		
		sleep(2)
		
		#publish to topic and check true
		self.assertEqual(True, self.mqttClientConnector.subscribeToSensorCommands("TestingTopic", 1))

		#call the connect method of MqttClientConnector with inaccurate values
		self.mqttClientConnector.connect("brosdf235iytksg", 1883)
		
		sleep(2)
		
		#publish to topic and check true
		self.assertEqual(False, self.mqttClientConnector.subscribeToSensorCommands("TestingTopic", 1))

		pass
	
	"""
	This method tests the testSubscribeToActuatorCommands() method of the MqttClientConnector
	It checks for false when failure to subscribe, and true when subscribes properly
	"""
	def testMessageReceived(self):
		
		#call the connect method of MqttClientConnector with accurate values
		

		pass
	
	"""
	This method tests the setMqttClient() method of the MultiSensorAdaptor
	It checks for false when sent a null instead of a reference of type MqttClientConnector, and true when 
	appropriate reference passed
	"""
	def testSetMqttClientConnector(self):
		
		#set a valid reference and check for true
		self.assertEqual(False, self.multiSensorAdaptor.setMqttClient(None))

		#set an invalid reference and check for false
		self.assertEqual(True, self.multiSensorAdaptor.setMqttClient(self.mqttClientConnector))

		pass
	
	"""
	This method tests the start() method of the MultiSensorAdaptor
	It checks for false if the number of readings needed is 0 
	or if fetcher is not enabled. Else return true if it runs
	"""
	def testStart(self):
		
		#check for false when there is no reference to mqtt client connector
		self.assertEqual(False, self.multiSensorAdaptor.start())
		
		#set the mqtt client connector reference to self
		self.multiSensorAdaptor.setMqttClient(self.mqttClientConnector)
		
		#enable the fetcher
		self.multiSensorAdaptor.enableFetcher = True
		
		#change numReadings to a small finite value to check
		self.multiSensorAdaptor.numReadings = 1
		
		#change sleep time (rateInSec) to a small amount
		self.multiSensorAdaptor.rateInSec = 1
		
		#run when numReadings > 0 and adaptor is enabled
		self.assertEqual(True, self.multiSensorAdaptor.start())
		
		#change numReadings to 0
		self.multiSensorAdaptor.numReadings = 0
		
		#run when numReadings = 0 and emulator is enabled, should return false because generator didn't run
		self.assertEqual(False, self.multiSensorAdaptor.start())
		
		#disable the fetcher
		self.multiSensorAdaptor.enableFetcher = False
		
		#change readings to > 0
		self.multiSensorAdaptor.numReadings = 1
		
		#run when numReadings > 0 and fetcher is disabled, should return false because generator didn't run
		self.assertEqual(False, self.multiSensorAdaptor.start())
		
		pass
	
	

if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testName']
	unittest.main()