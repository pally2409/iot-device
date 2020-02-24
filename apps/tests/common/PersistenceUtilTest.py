#import libraries and modules
import unittest
import logging
from labs.common.ActuatorData import ActuatorData
from labs.common.SensorData import SensorData
from labs.common.PersistenceUtil import PersistenceUtil
from redis.client import Redis



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

class PersistenceUtilTest(unittest.TestCase):

	"""
	Use this to setup your tests. This is where you may want to load configuration
	information (if needed), initialize class-scoped variables, create class-scoped
	instances of complex objects, initialize any requisite connections, etc.
	"""
	def setUp(self):
		
		#instantiate persistenceUtil
		self.persistenceUtil = PersistenceUtil()

	"""
	Use this to tear down any allocated resources after your tests are complete. This
	is where you may want to release connections, zero out any long-term data, etc.
	"""
	def tearDown(self):
		
		#set the reference to the variables to none to release any resources
		self.persistenceUtil = None
		
	"""
	/**
	 * Tests the writeActuatorDataToDbms() method of PersistenceUtil class. 
	 * Checks whether it is able to write to redis and doesn't
	 * break if it cannot set up the connection to the server
	 */
	"""
	def testWriteActuatorDataToDbms(self):
		
		#Create ActuatorData instance
		actuatorData = ActuatorData();
		
		#write to redis and check if it returns true
		self.assertEqual(True, self.persistenceUtil.writeActuatorDataToDbms(actuatorData));
		
		#add an invalid port to the jedisActuator
		self.persistenceUtil.r_actuator = Redis(host = "localhost", port = 6379)
		
		#write to redis and check if it returns false
		self.assertEqual(True, self.persistenceUtil.writeActuatorDataToDbms(actuatorData));
	
	"""	
	/**
	 * Tests the writeSensorDataToDbms() method of PersistenceUtil class. 
	 * Checks whether it is able to write to redis and doesn't
	 * break if it cannot set up the connection to the server
	 */
	"""
	def testWriteSensorDataToDbms(self):
		
		#Create ActuatorData instance
		sensorData = SensorData();
		
		#write to redis and check if it returns true
		self.assertEqual(True, self.persistenceUtil.writeSensorDataToDbms(sensorData));
		
		#add an invalid port to the jedisSensor
		self.persistenceUtil.r_sensor = Redis(host = "localhost", port = 6890)
		
		#write to redis and check if it returns false
		self.assertEqual(False, self.persistenceUtil.writeSensorDataToDbms(sensorData));
	
	"""	
	/**
	 * Tests the registerSensorDataDbmsListener() method of PersistenceUtil class. 
	 * Checks whether it is able to register and doesn't
	 * break if it cannot set up the connection to the server
	 */
	"""
	def testRegisterSensorDataDbmsListener(self):
	
		#check for true when the connection variables are ok
		self.assertEqual(True, self.persistenceUtil.registerSensorDataDbmsListener())
	
		#add an invalid port to the jedisSensor
		self.persistenceUtil.r_sensor = Redis(host = "localhost", port = 6890)
		
		#check for false when connection variables are invalid
		self.assertEqual(False, self.persistenceUtil.registerSensorDataDbmsListener())
		
	"""	
	/**
	 * Tests the registerActuatorDataDbmsListener() method of PersistenceUtil class. 
	 * Checks whether it is able to register and doesn't
	 * break if it cannot set up the connection to the server
	 */
	"""
	def testRegisterActuatorDataDbmsListener(self):
	
		#check for true when the connection variables are ok
		self.assertEqual(True, self.persistenceUtil.registerActuatorDataDbmsListener())
	
		#add an invalid port to the jedisSensor
		self.persistenceUtil.r_actuator = Redis(host = "localhost", port = 6890)
		
		#check for false when connection variables are invalid
		self.assertEqual(False, self.persistenceUtil.registerActuatorDataDbmsListener())
		

if __name__ == "__main__":
	unittest.main()
