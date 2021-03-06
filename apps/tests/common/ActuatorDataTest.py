#import libraries and modules
import unittest
from labs.common.ActuatorData import ActuatorData


"""
Test class for all requisite ActuatorData functionality.

Instructions:
1) Rename 'testSomething()' method such that 'Something' is specific to your needs; add others as needed, beginning each method with 'test...()'.
2) Add the '@Test' annotation to each new 'test...()' method you add.
3) Import the relevant modules and classes to support your tests.
4) Run this class as unit test app.
5) Include a screen shot of the report when you submit your assignment.

Please note: While some example test cases may be provided, you must write your own for the class.
"""
class ActuatorDataTest(unittest.TestCase):

	"""
	Use this to setup your tests. This is where you may want to load configuration
	information (if needed), initialize class-scoped variables, create class-scoped
	instances of complex objects, initialize any requisite connections, etc.
	"""
	def setUp(self):
		
		#instantiate ActuatorData
		self.actuatorData = ActuatorData()
		
		pass

	"""
	Use this to tear down any allocated resources after your tests are complete. This
	is where you may want to release connections, zero out any long-term data, etc.
	"""
	def tearDown(self):
		
		#set the reference to the variables to none to release any resources
		self.actuatorData = None
		
		pass
	
	"""
	Tests the getCommand() method of ActuatorData module. Checks whether the command is updating appropriately, and doesn't break if the command is set to None
	"""
	def testGetCommand(self):
		
		#test the command when nothing has been set
		self.assertEqual('Not set', self.actuatorData.getCommand(), "Command was not set")
		
		#test the command when set to 'INCREASE TEMP'
		self.actuatorData.setCommand('INCREASE TEMP')
		self.assertEqual('INCREASE TEMP', self.actuatorData.getCommand(), "Command was set to INCREASE TEMP")
		
		#test the command is set to 'Not Set' when set to None
		self.actuatorData.setCommand(None)
		self.assertEqual('Not set', self.actuatorData.getCommand(), "Command was not set")
		
		pass
	
	"""
	Tests the setCommand() method of ActuatorData module. Checks whether the command is updating appropriately, and doesn't break if the name is set to None
	"""
	def testSetCommand(self):
		
		#test the command when set to None
		self.actuatorData.setCommand(None)
		self.assertEqual('Not set', self.actuatorData.getCommand(), "Command was not set")
		
		#test the command when set to 'INCREASE TEMP'
		self.actuatorData.setCommand('INCREASE TEMP')
		self.assertEqual('INCREASE TEMP', self.actuatorData.getCommand(), "Command was set to INCREASE TEMP")
		
		pass
	
	"""
	Tests the getValue() method of ActuatorData module. Checks whether the value is updating appropriately, and doesn't break if the name is set to None
	"""
	def testGetValue(self):
		
		#test the name when nothing has been set
		self.assertEqual('Not set', self.actuatorData.getValue(), "Name was not set")
		
		#test the name when set to None
		self.actuatorData.setValue(None)
		self.assertEqual('Not set', self.actuatorData.getValue(), "Name was not set")
		
		#test the name when set to redArrowInc
		self.actuatorData.setValue('My Pixel')
		self.assertEqual('My Pixel', self.actuatorData.getValue(), "Name was set to My Pixel")
		
		pass
	
	"""
	Tests the setValue() method of ActuatorData module. Checks whether the value is updating appropriately, and doesn't break if the name is set to None
	"""
	def testSetValue(self):
		
		#test the name when nothing has been set
		self.assertEqual('Not set', self.actuatorData.getValue(), "Name was not set")
		
		#test the name when set to None
		self.actuatorData.setValue(None)
		self.assertEqual('Not set', self.actuatorData.getValue(), "Name was not set")
		
		#test the name when set to redArrowInc
		self.actuatorData.setValue('My Pixel')
		self.assertEqual('My Pixel', self.actuatorData.getValue(), "Name was set to My Pixel")
		
		pass
	
	"""
	Tests the getName() method of ActuatorData module. Checks whether the name is updating appropriately, and doesn't break if the name is set to None
	"""
	def testGetName(self):
		
		#test the name when nothing has been set
		self.assertEqual('Not set', self.actuatorData.getName(), "Name was not set")
		
		#test the name when set to None
		self.actuatorData.setName(None)
		self.assertEqual('Not set', self.actuatorData.getName(), "Name was not set")
		
		#test the name when set to 'Temperature'
		self.actuatorData.setName('Temperature')
		self.assertEqual('Temperature', self.actuatorData.getName(), "Name was set to Temperature")
		
	
	"""
	Tests the setName() method of ActuatorData module. Checks whether the name is updating appropriately, and doesn't break if the name is set to None
	"""
	def testSetName(self):
		
		#test the name when set to None
		self.actuatorData.setName(None)
		self.assertEqual('Not set', self.actuatorData.getName(), "Name was not set")
		
		#test the command when set to 'INCREASE TEMP'
		self.actuatorData.setName('Temperature')
		self.assertEqual('Temperature', self.actuatorData.getName(), "Name was set to Temperature")
		
		pass
	
	
		

if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testName']
	unittest.main()