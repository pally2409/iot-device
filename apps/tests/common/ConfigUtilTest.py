import unittest
import logging
from labs.common import ConfigUtil



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
logging.getLogger("temperature emulator logger")
logging.basicConfig(format='%(message)s', level=logging.DEBUG)

class ConfigUtilTest(unittest.TestCase):

	"""
	Use this to setup your tests. This is where you may want to load configuration
	information (if needed), initialize class-scoped variables, create class-scoped
	instances of complex objects, initialize any requisite connections, etc.
	"""
	def setUp(self):
		
		#instantiate configUtil
		self.configUtil = ConfigUtil.ConfigUtil()
		
		#if the default config file is not loaded: while testing the pipeline on the cloud
		if self.configUtil.configFileLoaded == False:
			
			#load the sample config directory
			self.configUtil.__init__('../../../sample/ConnectedDevicesConfig_NO_EDIT_TEMPLATE_ONLY.props')
			
		pass
	
	

	"""
	Use this to tear down any allocated resources after your tests are complete. This
	is where you may want to release connections, zero out any long-term data, etc.
	"""
	def tearDown(self):
		pass
	
	"""
	This method checks the getBooleanValue() function of ConfigUtil class. It checks for valid boolean values, checks
	for when an invalid key is sent as a parameter and when an invalid section is sent as a parameter
	"""
	def testGetBooleanProperty(self):
		# TODO: implement this
		
		logging.info('Testing getBooleanValue()')
		
		#check boolean value for ubidots.cloud section's useWebAccess key which is correctly stored as a boolean property
		self.assertEqual(True, self.configUtil.getBooleanValue('ubidots.cloud', 'useWebAccess'))
		
		#check boolean value for ubidots.cloud section's host key which is invalid boolean
		self.assertEqual(0, self.configUtil.getBooleanValue('ubidots.cloud', 'host'))
		
		#check boolean value for ubidots.cloud section's 'hostt' key which is a typo and should return a 0
		self.assertEqual(0, self.configUtil.getBooleanValue('ubidots.cloud', 'hostt'))
		
		#check boolean value for ubidots.cloudd section which is a typo
		self.assertEqual(0, self.configUtil.getBooleanValue('ubidots.cloudd', 'host'))
		
		pass
	
	"""
	This method checks the getIntegerValue() function of ConfigUtil class. It checks for valid integer values, checks
	for when an invalid key is sent as a parameter and when an invalid section is sent as a parameter
	"""
	def testGetIntegerProperty(self):
		# TODO: implement this
		
		logging.info('Running testGetIntegerProperty()')
		
		#check integer value for smtp.cloud section's port key which is correctly stored as an integer property
		self.assertEqual(465, self.configUtil.getIntegerValue('smtp.cloud', 'port'))
		
		#check integer value for ubidots.cloud section's host key which is not an integer and should return a false
		self.assertEqual(False, self.configUtil.getIntegerValue('ubidots.cloud', 'host'))
		
		#check integer value for ubidots.cloud section's 'hostt' key which is an error in typing and should return a false
		self.assertEqual(False, self.configUtil.getIntegerValue('ubidots.cloud', 'hostt'))
		
		#check integer value for ubidots.cloudd section which is an error in typing and should return a false
		self.assertEqual(False, self.configUtil.getIntegerValue('ubidots.cloudd', 'host'))
		
		pass
	
	"""
	This method checks the getValue() function of ConfigUtil module. It checks valid values, checks
	for when an invalid key is sent as a parameter and when an invalid section is sent as a parameter
	"""
	def testGetProperty(self):
		# TODO: implement this
		
		logging.info('Running testGetProperty()')
		
		#check value for smtp.cloud section's port key which is correctly stored
		self.assertEqual('smtp.gmail.com', self.configUtil.getValue('smtp.cloud', 'host'))
		
		#check value for ubidots.cloud section's 'hostt' key which is an error in typing and should return a false
		self.assertEqual(False, self.configUtil.getValue('ubidots.cloud', 'hostt'))
		
		#check value for ubidots.cloudd section which is an error in typing and should return a false
		self.assertEqual(False, self.configUtil.getValue('ubidots.cloudd', 'host'))
		
		pass
	
	"""
	Tests if a property exists.
	"""
	def testHasProperty(self):
		# TODO: implement this
		
		logging.info('Running testHasProperty()')
		
		#check value for smtp.cloud section's port key which is correctly stored
		self.assertEqual('smtp.gmail.com', self.configUtil.getValue('smtp.cloud', 'host'))
		
		
		#check value for ubidots.cloud section's 'hostess' key and should return a false because hostess key doesn't exist
		self.assertEqual(False, self.configUtil.getValue('ubidots.cloud', 'hostess'))
		
		pass

	"""
	Tests if a section exists.
	"""
	def testHasSection(self):
		# TODO: implement this
		
		logging.info('Running testHasSection()')
		
		#check value for smtp.cloud section's port key which is correctly stored
		self.assertEqual('smtp.gmail.com', self.configUtil.getValue('smtp.cloud', 'host'))
		
		#check value for ubidots.sky section's 'host' and should return a false because ubidots.sky is not a section
		self.assertEqual(False, self.configUtil.getValue('ubidots.cloud', 'hostt'))
		
		pass
	
	"""
	Tests if the configuration is loaded.
	"""
	def testIsConfigDataLoaded(self):
		
		logging.info('Running testIsConfigDataLoaded()')
		
		#when config file is correctly loaded 
		self.assertEqual(True, self.configUtil.configFileLoaded)
		
		#set a gibberish value as the config file
		self.configUtil.loadConfig('/config/blah.props')
		
		#configFileLoaded should return a false because the given file above doesn't exist
		self.assertEqual(False, self.configUtil.configFileLoaded)
		
	
if __name__ == "__main__":
	unittest.main()
