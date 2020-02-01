#import the libraries
import unittest
import logging
from labs.common.SensorData 				import SensorData
from labs.module02.SmtpClientConnector 		import SmtpClientConnector
from labs.module02.TempSensorEmulatorTask  	import TempSensorEmulatorTask
from labs.module02.TempEmulatorAdaptor 							import TempEmulatorAdaptor


"""
Test class for all requisite Module02 functionality.

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


class Module02Test(unittest.TestCase):

	"""
	Use this to setup your tests. This is where you may want to load configuration
	information (if needed), initialize class-scoped variables, create class-scoped
	instances of complex objects, initialize any requisite connections, etc.
	"""
	def setUp(self):
		
		#initialize the variables required
		self.smtpClientConnector = SmtpClientConnector()
		self.tempSensorEmulatorTask = TempSensorEmulatorTask()
		self.tempEmulatorAdaptor = TempEmulatorAdaptor()

	"""
	Use this to tear down any allocated resources after your tests are complete. This
	is where you may want to release connections, zero out any long-term data, etc.
	"""
	def tearDown(self):
		
		#set the reference to the variables as none to release the resources they're holding
		self.smtpClientConnector = None
		self.tempSensorEmulatorTask = None
		self.tempEmulatorAdaptor = None
	
	"""
	 This method tests the publishMessage() of SmtpClientConnector module. It checks whether the SmtpClientConnector is able to successfully 
	 send an email or not by testing it in various scenarios like when the configurations are correct, wrong configurations, wrong values 
	 in configurations, connection failure
	"""
	def testPublishMessage(self):
		
		logging.info("Running testPublishMessage()")
		
		#when testing on the pipeline on cloud, the config file has been ignored. hence, load sample config file
		if self.smtpClientConnector.config.configFileLoaded == False:
			
			self.smtpClientConnector.config.loadConfig('../sample/ConnectedDevicesConfig_NO_EDIT_TEMPLATE_ONLY.props')
		
		#when default config file is loaded properly (testing on the computer)
		else: 
			
			#when configurations are correct
			success = self.smtpClientConnector.publishMessage("Testing Message", "This is a test")
		
			#test true on success of mail
			self.assertEqual(success, True, "Message was sent successfully, test case showing false")
			
		
		#load the sample config file where the fromAddr and toAddr, authToken are not valid
		self.smtpClientConnector.config.loadConfig('../sample/ConnectedDevicesConfig_NO_EDIT_TEMPLATE_ONLY.props')
		
		#test false on success of mail
		success = self.smtpClientConnector.publishMessage("Testing Message", "This is a test")
		self.assertEqual(success, False, "Message was not sent successfully, test case showing true")
	
	"""
	This method tests the generateRandomTemperature() method of the TempSensorEmulatorTask module. It checks whether the 
	generator runs in various scenarios such as disabling the emulator, setting the number of readings to 0
	"""
		
	def testGenerateRandomTemperature(self):
		
		logging.info("Running testGenerateRandomTemperature()")
		
		#enable the emulator
		self.tempSensorEmulatorTask.enableEmulator = True
		
		#change numReadings to a small finite value to check
		self.tempSensorEmulatorTask.numReadings = 3
		
		#change sleep time (rateInSec) to a small amount
		self.tempSensorEmulatorTask.rateInSec = 3
		
		#run when numReadings > 0 and adaptor is enabled
		self.assertEqual(True, self.tempSensorEmulatorTask.generateRandomTemperature())
		
		#change numReadings to 0
		self.tempSensorEmulatorTask.numReadings = 0
		
		#run when numReadings = 0 and emulator is enabled, should return false because generator didn't run
		self.assertEqual(False, self.tempSensorEmulatorTask.generateRandomTemperature())
		
		#disable the emulator 
		self.tempSensorEmulatorTask.enableEmulator = False
		
		#change readings to > 0
		self.tempSensorEmulatorTask.numReadings = 3
		
		#run when numReadings > 0 and emulator is disabled, should return false because generator didn't run
		self.assertEqual(False, self.tempSensorEmulatorTask.generateRandomTemperature())
	
	"""
	This method tests the getSensorData() method of the TempSensorEmulatorTask module. It simply checks
	whether the reference to the sensorData of tempSensorEmulatorTask is valid or not
	"""	
	def testGetSensorData(self):
		
		logging.info("Running testGetSensorData()")
		
		#check type of the return of the method, should be of type SensorData
		self.assertEqual(type(self.tempSensorEmulatorTask.getSensorData()), SensorData)
		
		#check if the returned sensorData reference belongs to the tempSensorEmulatorTask's sensorData 
		sensorData = self.tempSensorEmulatorTask.getSensorData()
		sensorData.addValue(30)
		self.assertEqual(30, self.tempSensorEmulatorTask.getSensorData().getCurrentValue())
	
	"""
	 This method tests the sendNotification method of the TempSensorEmulatorTask module. It simply whether
	 the notification is being sent or not. This has been shown in documentation using screenshot of the
	 email
	"""	
	def testSendNotification(self):
		
		logging.info("Running testSendNotification()")
		
		#if the config file is loaded: while testing on system
		if self.tempSensorEmulatorTask.smtpConnector.config.configFileLoaded == True:
			
			#returns true, notification is being sent
			self.assertEqual(True, self.tempSensorEmulatorTask.sendNotification("Hello"))
	
	"""
	This method simply checks whether the adaptor is running successfully
	"""		
	def testTempEmulatorAdaptor(self):
		
		logging.info("Running testTempEmulatorAdaptor()")
		
		#get the reference to the tempSensorEmulatorTask
		tempSensTask = self.tempEmulatorAdaptor.tempSensorEmulator
		
		#change numReadings to a small finite value to check
		tempSensTask.numReadings = 3
		
		#change sleep time (rateInSec) to a small amount
		tempSensTask.rateInSec = 1
		
		#enable the tempEmulatorTask's emulator
		tempSensTask.enableEmulator = True
		
		#run the run function of tempEmulatorAdaptor and get the value of success of the adaptor
		self.assertEqual(True, self.tempEmulatorAdaptor.run())
		
if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testName']
	unittest.main()