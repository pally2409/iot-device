#import libraries and modules
import unittest
from labs.module03.SensorDataManager 		import SensorDataManager
from labs.module03.TempActuatorAdaptor 		import TempActuatorAdaptor
from labs.module03.TempSensorAdaptor 		import TempSensorAdaptor
from labs.module03.TempSensorAdaptorTask 	import TempSensorAdaptorTask
from labs.common.SensorData 				import SensorData
from labs.common.ActuatorData 				import ActuatorData


"""
Test class for all requisite Module03 functionality.

Instructions:
1) Rename 'testSomething()' method such that 'Something' is specific to your needs; add others as needed, beginning each method with 'test...()'.
2) Add the '@Test' annotation to each new 'test...()' method you add.
3) Import the relevant modules and classes to support your tests.
4) Run this class as unit test app.
5) Include a screen shot of the report when you submit your assignment.

Please note: While some example test cases may be provided, you must write your own for the class.
"""

class Module03Test(unittest.TestCase):

	"""
	Use this to setup your tests. This is where you may want to load configuration
	information (if needed), initialize class-scoped variables, create class-scoped
	instances of complex objects, initialize any requisite connections, etc.
	"""
	#initialize the rgb values for the led colors
	
	#no color
	e = [0, 0, 0]
	
	#red
	r = [255, 0, 0]
	
	#blue
	b = [0, 0, 255]
	
	#initialize the red arrow when increasing the temperature on sense hat led matrix
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
	
	#initialize the blue arrow when decreasing the temperature on sense hat led matrix
	arrowBlueDec = [
                e,e,e,b,b,e,e,e,
                e,e,e,b,b,e,e,e,
                e,e,e,b,b,e,e,e,
                e,e,e,b,b,e,e,e,
                b,e,e,b,b,e,e,b,
                e,b,e,b,b,e,b,e,
                e,e,b,b,b,b,e,e,
                e,e,e,b,b,e,e,e
        ]
	
	
	def setUp(self):
		
		#instantiate the variables required
		self.sensorDataManager = SensorDataManager()
		self.tempActuatorAdaptor = TempActuatorAdaptor()
		self.tempSensorAdaptor = TempSensorAdaptor()
		self.tempSensorAdaptorTask = TempSensorAdaptorTask()

		
		pass

	"""
	Use this to tear down any allocated resources after your tests are complete. This
	is where you may want to release connections, zero out any long-term data, etc.
	"""
	def tearDown(self):
		
		#set the reference to the variables as none to release the resources they're holding
		self.sensorDataManager = None
		self.tempActuatorAdaptor = None
		self.tempSensorAdaptor = None
		self.tempSensorAdaptorTask = None
		pass

	"""
	This method tests the handleSensorData() of SensorDataManager module. It tests whether the sensor data passed to the method triggers the correct
	actuator command.
	"""
	def testGetHandleSensorData(self):	
			
		#initialize sensor data
		sensorData = SensorData()
		
		#when current value is greater than nominal temp
		sensorData.addValue(90)
		
		#get the actuatorData returned from the sensor data manager 
		actuatorData = self.sensorDataManager.handleSensorData(sensorData)
		
		#check if actuatorData is of type ActuatorData
		self.assertIsInstance(actuatorData, ActuatorData)
		
		#test the value, which should be "arrowBlueDec"
		self.assertEqual(self.arrowBlueDec, actuatorData.getValue())
		
		#actuatorData command should be decrease temp
		self.assertEqual(actuatorData.getCommand(), "DECREASE TEMP")
		
		#when current value is less than nominal temp
		sensorData.addValue(10)
		
		#get the actuatorData returned from the sensor data manager 
		actuatorData = self.sensorDataManager.handleSensorData(sensorData)
		
		#check if actuatorData is of type ActuatorData
		self.assertIsInstance(actuatorData, ActuatorData)
		
		print(actuatorData.getCommand())
		
		#actuatorData command should be increase temp
		self.assertEqual(actuatorData.getCommand(), "INCREASE TEMP")
		
		#when current value is equal to the nominal temp
		sensorData.addValue(20)
		
		#get the actuatorData returned from the sensor data manager 
		actuatorData = self.sensorDataManager.handleSensorData(sensorData)
		
		#actuatorData is none sensor data equal to nominal temp
		self.assertEqual(actuatorData, None)
			
		pass
	
	"""
	This tests the sendNotification() method of the SensorDataManager, it simply whether
	 the notification is being sent or not. This has been shown in documentation using screenshot of the
	 email
	"""
	def testSendNotification(self):
		
		#if the config file is loaded: while testing on system
		if self.sensorDataManager.smtpClientConnector.config.configFileLoaded == True:
			
			#returns true, notification is being sent
			self.assertEqual(True, self.sensorDataManager.sendNotification("Hello", "This is a test"))
			
		pass


	"""
	This tests the updateActuator() method of the TempActuatorAdaptor, it checks whether the actuator is updated 
	(by returning an actuatorData reference) when the trigger is valid (INCREASE TEMP) and when the trigger is invalid 
	(NOT A VALID TRIGGER)
	"""
	def testUpdateActuator(self):
		
		#create an invalid actuator trigger
		actuatorData = ActuatorData()
		actuatorData.setCommand("NOT A VALID TRIGGER")
		
		#add a valid value
		actuatorData.setValue(self.arrowBlueDec)
		
		#updateActuator should return a false
		self.assertEqual(False, self.tempActuatorAdaptor.updateActuator(actuatorData))
		
		#create a valid actuator trigger
		actuatorData = ActuatorData()
		actuatorData.setCommand("INCREASE TEMP")
		actuatorData.setValue(self.arrowRedInc)
		
		#updateActuator should return a True
		self.assertEqual(True, self.tempActuatorAdaptor.updateActuator(actuatorData))
		
		#sending a none should throw an exception, where when caught, returns a false
		self.assertEqual(False, self.tempActuatorAdaptor.updateActuator(None))
		
		pass
	
	
	"""
	This tests the getTemperature() method of the TempSensorAdaptorTask, it checks whether the fetcher runs when enabled,
	disabled, number of readings to get has been set to 0.
	"""
	def testGetTemperature(self):
		
		#enable the fetcher
		self.tempSensorAdaptorTask.enableFetcher = True
		
		#change numReadings to a small finite value to check
		self.tempSensorAdaptorTask.numReadings = 1
		
		#change sleep time (rateInSec) to a small amount
		self.tempSensorAdaptorTask.rateInSec = 1
		
		#run when numReadings > 0 and adaptor is enabled
		self.assertEqual(True, self.tempSensorAdaptorTask.getTemperature())
		
		#change numReadings to 0
		self.tempSensorAdaptorTask.numReadings = 0
		
		#run when numReadings = 0 and emulator is enabled, should return false because generator didn't run
		self.assertEqual(False, self.tempSensorAdaptorTask.getTemperature())
		
		#disable the emulator 
		self.tempSensorAdaptorTask.enableFetcher = False
		
		#change readings to > 0
		self.tempSensorAdaptorTask.numReadings = 1
		
		#run when numReadings > 0 and emulator is disabled, should return false because generator didn't run
		self.assertEqual(False, self.tempSensorAdaptorTask.getTemperature())
	
		
	"""
	This tests the run() method of the TempSensorAdaptor, it checks whether it runs successfully.
	"""
	def testTempSensorAdaptor(self):
		
		#get the reference to the tempSensorEmulatorTask
		tempSensTask = self.tempSensorAdaptor.tempSensorAdaptorTask
		
		#change numReadings to a small finite value to check
		tempSensTask.numReadings = 1
		
		#change sleep time (rateInSec) to a small amount
		tempSensTask.rateInSec = 1
		
		#enable the tempEmulatorTask's emulator
		tempSensTask.enableFetcher = True
		
		#run the run function of tempEmulatorAdaptor and get the value of success of the adaptor
		self.assertEqual(True, self.tempSensorAdaptor.run())

if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testName']
	unittest.main()