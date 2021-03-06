import unittest
import sense_hat
import logging
from time										import sleep
from labs.module04.SensorDataManager 			import SensorDataManager
from labs.module04.HI2CSensorAdaptorTask 		import HI2CSensorAdaptorTask
from labs.module04.HumiditySensorAdaptorTask 	import HumiditySensorAdaptorTask
from labs.module04.MultiActuatorAdaptor 		import MultiActuatorAdaptor
from labs.module04.MultiSensorAdaptor 			import MultiSensorAdaptor
from labs.common.ActuatorData					import ActuatorData
from labs.common.SensorData						import SensorData




"""
Test class for all requisite Module04 functionality.

Instructions:
1) Rename 'testSomething()' method such that 'Something' is specific to your needs; add others as needed, beginning each method with 'test...()'.
2) Add the '@Test' annotation to each new 'test...()' method you add.
3) Import the relevant modules and classes to support your tests.
4) Run this class as unit test app.
5) Include a screen shot of the report when you submit your assignment.

Please note: While some example test cases may be provided, you must write your own for the class.
"""

#set the basic configuration to display time, level and the message
logging.getLogger("module 2 test logger")
logging.basicConfig(format='%(message)s', level=logging.DEBUG)

class Module04Test(unittest.TestCase):

	"""
	Use this to setup your tests. This is where you may want to load configuration
	information (if needed), initialize class-scoped variables, create class-scoped
	instances of complex objects, initialize any requisite connections, etc.
	"""
	def setUp(self):
		
		#instantiate the classes required
		self.sensorDataManager = SensorDataManager()
		self.hI2CSensorAdaptorTask = HI2CSensorAdaptorTask()
		self.humiditySensorAdaptorTask = HumiditySensorAdaptorTask()
		self.multiActuatorAdaptor = MultiActuatorAdaptor()
		self.multiSensorAdaptor = MultiSensorAdaptor()
		self.sense = sense_hat.SenseHat()

	"""
	Use this to tear down any allocated resources after your tests are complete. This
	is where you may want to release connections, zero out any long-term data, etc.
	"""
	def tearDown(self):
		
		#set the reference to the variables as none to release the resources they're holding
		self.sensorDataManager = None
		self.hI2CSensorAdaptorTask = None
		self.multiActuatorAdaptor = None
		self.multiSensorAdaptorTask = None
		self.multiSensorAdaptor = None
		self.sense = None
		pass

	"""
	This method tests the handleSensorData() of SensorDataManager module. It tests whether the sensor data list passed to the method triggers the correct
	actuator command.
	"""
	def testGetHandleSensorData(self):
		
		#log the test
		logging.info("\nTesting the handleSensorData() method of SensorDataManager")	
			
		#initialize sensor data to represent reading from I2C 
		sensorDataI2C = SensorData()
		
		#add a humidity value
		sensorDataI2C.addValue(10)
		
		#set the name for i2c 
		sensorDataI2C.setName("i2c humidity")
		
		#initialize sensor data to represent reading from SenseHAT API 
		sensorDataAPI = SensorData()
		
		#add a humidity value
		sensorDataAPI.addValue(9)
		
		#set the name for i2c 
		sensorDataAPI.setName("sense_hat API humidity")
		
		#add them to a list
		sensorDataTest = []
		sensorDataTest.append(sensorDataI2C)
		sensorDataTest.append(sensorDataAPI)
		
		#get the actuatorDataList returned from the sensor data manager 
		actuatorDataList = self.sensorDataManager.handleSensorData(sensorDataTest)
		
		#check if actuatorData at both indexes are of type ActuatorData
		self.assertIsInstance(actuatorDataList[0], ActuatorData)
		self.assertIsInstance(actuatorDataList[1], ActuatorData)
		
		#test the actuatorData value at the first index, which should simply be the first value (10)
		self.assertEqual(10, actuatorDataList[0].getValue())
		
		#test the actuatorData command at the first index which should be DISPLAY I2C Humidity
		self.assertEqual(actuatorDataList[0].getCommand(), "DISPLAY I2C Humidity")
		
		#test the actuatorData name at the second index which should be I2C Humidity
		self.assertEqual(actuatorDataList[0].getName(), "I2C Humidity")
		
		#test the value at the second index, which should simply be the first value (9)
		self.assertEqual(9, actuatorDataList[1].getValue())
	
		#test the actuatorData command at the second index which should be DISPLAY I2C Humidity
		self.assertEqual(actuatorDataList[1].getCommand(), "DISPLAY SENSE HAT API Humidity")
		
		#test the actuatorData name at the second index which should be I2C Humidity
		self.assertEqual(actuatorDataList[1].getName(), "SENSE HAT API Humidity")
		
		#initialize a random sensorData object and add it to the list and call the manager again
		sensorData = SensorData()
		
		#set invalid sensor data name
		sensorData.setName("blah blah")
		
		#append to list
		sensorDataTest.append(sensorData)
		
		#get the actuatorDataList returned from the manager should still have a length of 2 because we only added an invalid type
		actuatorDataList = self.sensorDataManager.handleSensorData(sensorDataTest)
		
		#check if length of actuatorDataList is 2
		self.assertEqual(len(actuatorDataList), 2)
			
		#clear the list and only add invalid sensor data
		sensorDataTest = []
		sensorDataTest.append(sensorData)
		
		#get the actuatorDataList returned from the manager should be None 
		actuatorDataList = self.sensorDataManager.handleSensorData(sensorDataTest)
		
		#check if it is none
		self.assertEqual(actuatorDataList, None)
		
		
	"""
	This tests the sendNotification() method of the SensorDataManager, it simply whether
	 the notification is being sent or not. This has been shown in documentation using screenshot of the
	 email
	"""
	def testSendNotification(self):
		
		#log the test
		logging.info("\nTesting the sendNotification() method of SensorDataManager")	
		
		#if the config file is loaded: while testing on system
		if self.sensorDataManager.smtpClientConnector.config.configFileLoaded == True:
			
			#returns true, notification is being sent
			self.assertEqual(True, self.sensorDataManager.sendNotification("Hello", "This is a test"))
			
		pass
	
	"""
	This tests the updateActuator() method of the MultiActuatorAdaptor, it checks whether the actuator is updated 
	(by returning an actuatorData reference) when the trigger is valid and when the trigger is invalid 
	(NOT A VALID TRIGGER)
	"""
	def testUpdateActuator(self):
		
		#log the test
		logging.info("\nTesting the updateActuator() method of MultiActuatorAdaptor")	
 		
		#create an invalid actuator trigger
		actuatorData = ActuatorData()
		actuatorData.setCommand("NOT A VALID TRIGGER")
		
		#add a valid value
		actuatorData.setValue(90)
		
		#add it to list of actuatorDataTest
		actuatorDataTest = []
		actuatorDataTest.append(actuatorData)
		
		#updateActuator should return a false
		self.assertEqual(False, self.multiActuatorAdaptor.updateActuator(actuatorDataTest))
		
		#create a valid actuator trigger
		actuatorData = ActuatorData()
		actuatorData.setCommand("DISPLAY SENSE HAT API Humidity")
		actuatorData.setValue(12)
		
		actuatorDataTest = []
		actuatorDataTest.append(actuatorData)
		
		#updateActuator should return a True
		self.assertEqual(True, self.multiActuatorAdaptor.updateActuator(actuatorDataTest))
		
		#sending a none should throw an exception, where when caught, returns a false
		self.assertEqual(False, self.multiActuatorAdaptor.updateActuator(None))
		
		pass
	
	"""
	This tests the getHumidityData() method of the HI2CSensorAdaptorTask, it checks whether the returned value and the sense_hat api value
	have difference < 1
	"""
	def testGetHumidityDataHI12C(self):
		
		#log the test
		logging.info("\nTesting the getHumidityData() method of HI2CSensorAdaptorTask")
		
		#get the humidity data
		sensorData = self.hI2CSensorAdaptorTask.getHumidityData()
		
		#sleep for little time
		sleep(1)
		
		#get the absolute difference between sensorData from i2c and the sense hat api
		self.assertTrue(abs(sensorData.getCurrentValue() - self.sense.get_humidity()) <= 1.0, "Value" + str(sensorData.getCurrentValue()))
		
	"""
	This tests the getHumidityData() method of the HI2CSensorAdaptorTask, it checks whether the returned value and the sense_hat api value
	have difference < 1
	"""
	def testGetHumidityDataAPI(self):
		
		#log the test
		logging.info("\nTesting the getHumidityData() method of HumiditySensorAdaptorTask")
		
		#get the humidity data
		sensorData = self.humiditySensorAdaptorTask.getHumidityData()
		
		#sleep for little time
		sleep(0.5)
		
		#get the absolute difference between sensorData from i2c and the sense hat api
		self.assertTrue(abs(sensorData.getCurrentValue() - self.sense.get_humidity()) <= 1.0)
		
	
	"""
	Tests the getSensorData() method of both the HI2CSensorAdaptorTask and HumiditySensorAdaptorTask 
	"""
	
	def testGetSensorData(self):
		
		#get the sensor data reference from the getSensorData method
		sensorDataHI2C = self.hI2CSensorAdaptorTask.getSensorData()
		sensorDataHumidity = self.humiditySensorAdaptorTask.getSensorData()
		
		#check if instance of SensorData
		self.assertIsInstance(sensorDataHI2C, SensorData)
		self.assertIsInstance(sensorDataHumidity, SensorData)
		
		
	"""
	This tests the whether the difference between the sensor values detected from , it checks whether the 
	i2c bus and sense hat API have a difference of <= 1.0 
	"""	
	def testComparisonI2CSenseHat(self):
		
		#log the test
		logging.info("\nTesting the comparison between readings of I2C Bus and API")
		
		#get the sensor data references from both
		sensorDataHumidity = self.humiditySensorAdaptorTask.getSensorData()
		
		#sleep for little time
		sleep(0.5)
		
		sensorDataHI2C = self.hI2CSensorAdaptorTask.getSensorData()
		
		#check for difference
		self.assertTrue(abs(sensorDataHumidity.getCurrentValue() - sensorDataHI2C.getCurrentValue()) <= 1.0, "Value more than 1")
		
	"""
	This test checks the run() method of the MultiSensorAdaptor
	"""	
	def testRun(self):
		
		#log the test
		logging.info("\nTesting the run() method of MultiSensorAdaptor()")
		
		#enable the fetcher
		self.multiSensorAdaptor.hI2CSensorAdaptorTask.enableFetcher = True
		self.multiSensorAdaptor.humiditySensorAdaptorTask.enableFetcher = True
		
		#change numReadings to a small finite value to check
		self.multiSensorAdaptor.numReadings = 1
		
		#change sleep time (rateInSec) to a small amount
		self.multiSensorAdaptor.rateInSec = 1
		
		#run when numReadings > 0 and adaptor is enabled
		self.assertEqual(True, self.multiSensorAdaptor.run())
		
		#change numReadings to 0
		self.multiSensorAdaptor.numReadings = 0
		
		#run when numReadings = 0 and fetcher is enabled, should return false because run will not fetch
		self.assertEqual(False, self.multiSensorAdaptor.run())
		
	
if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testName']
	unittest.main()