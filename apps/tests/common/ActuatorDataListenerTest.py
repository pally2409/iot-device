#import libraries and modules
import unittest
import logging
from labs.common import ConfigUtil
from labs.common import ActuatorDataListener
from labs.common.ActuatorData import ActuatorData



"""
Test class for the ConfigUtil module.

Instructions:
1) Rename 'testSomething()' method such that 'Something' is specific to your needs; add others as needed, beginning each method with 'test...()'.
2) Add the '@Test' annotation to each new 'test...()' method you add.
3) Import the relevant modules and classes to support your tests.
4) Run this class as unit test app.
5) Include a screen shot of the report when you submit your assignment.

Please note: While some example test cases may be provided, you must write your own for the class.
"""

#set the basic configuration to display time, level and the message
logging.getLogger("ActuatorDataListenerTest")
logging.basicConfig(format='%(message)s', level=logging.DEBUG)

class ActuatorDataListenerTest(unittest.TestCase):

	"""
	Use this to setup your tests. This is where you may want to load configuration
	information (if needed), initialize class-scoped variables, create class-scoped
	instances of complex objects, initialize any requisite connections, etc.
	"""
	def setUp(self):
		
		#instantiate actuatorDataListner
		self.actuatorDataListener = ActuatorDataListener.ActuatorDataListener()

	"""
	Use this to tear down any allocated resources after your tests are complete. This
	is where you may want to release connections, zero out any long-term data, etc.
	"""
	def tearDown(self):
		
		#set the reference to the variables to none to release any resources
		self.actuatorDataListener = None
	
	"""
	This method tests the onMessage() method of the ActuatorDataListener()
	It tests if the method runs correctly when valid actuatorData is sent and
	doesn't break if sent a null
	"""
	def testOnMessage(self):
		
		#initialize an actuatorData
		actuatorData = ActuatorData()
		
		#send to onMessage and assert True
		self.assertEqual(True, self.actuatorDataListener.onMessage(actuatorData))
		
		#set actuatorData to None 
		actuatorData = None
		
		#send to onMessage and assert False
		self.assertEqual(False, self.actuatorDataListener.onMessage(actuatorData))
		

if __name__ == "__main__":
	unittest.main()
