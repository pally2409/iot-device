import unittest
from labs.module05.MultiActuatorAdaptor import MultiActuatorAdaptor
from labs.module05.MultiSensorAdaptor import MultiSensorAdaptor
from labs.module05.TempSensorAdaptorTask import TempSensorAdaptorTask
from labs.common.ActuatorData import ActuatorData


"""
Test class for all requisite Module05 functionality.

Instructions:
1) Rename 'testSomething()' method such that 'Something' is specific to your needs; add others as needed, beginning each method with 'test...()'.
2) Add the '@Test' annotation to each new 'test...()' method you add.
3) Import the relevant modules and classes to support your tests.
4) Run this class as unit test app.
5) Include a screen shot of the report when you submit your assignment.

Please note: While some example test cases may be provided, you must write your own for the class.
"""


class Module05Test(unittest.TestCase):

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
		
		#initialize the variables
		self.multiActuatorAdaptor = MultiActuatorAdaptor()
		self.multiSensorAdaptor = MultiSensorAdaptor()
		self.tempSensorAdaptorTask = TempSensorAdaptorTask()
		pass

	"""
	Use this to tear down any allocated resources after your tests are complete. This
	is where you may want to release connections, zero out any long-term data, etc.
	"""
	def tearDown(self):
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
	def testMultiSensorAdaptor(self):
		
		#get the reference to the tempSensorEmulatorTask
		tempSensTask = self.multiSensorAdaptor.tempSensorAdaptorTask
		
		#change numReadings to a small finite value to check
		tempSensTask.numReadings = 1
		
		#change sleep time (rateInSec) to a small amount
		tempSensTask.rateInSec = 1
		
		#enable the tempEmulatorTask's emulator
		tempSensTask.enableFetcher = True
		
		#run the run function of tempEmulatorAdaptor and get the value of success of the adaptor
		self.assertEqual(True, self.multiSensorAdaptor.run())
	
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
		self.assertEqual(False, self.multiActuatorAdaptor.updateActuator(actuatorData))
		
		#create a valid actuator trigger
		actuatorData = ActuatorData()
		actuatorData.setCommand("INCREASE TEMP")
		actuatorData.setValue(self.arrowRedInc)
		
		#updateActuator should return a True
		self.assertEqual(True, self.multiActuatorAdaptor.updateActuator(actuatorData))
		
		#sending a none should throw an exception, where when caught, returns a false
		self.assertEqual(False, self.multiActuatorAdaptor.updateActuator(None))
		
		pass
		

if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testName']
	unittest.main()