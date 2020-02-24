import unittest
from labs.common.DataUtil	import DataUtil
from labs.common.ActuatorData import ActuatorData
from labs.common.SensorData import SensorData


"""
Test class for all requisite DataUtil functionality.

Instructions:
1) Rename 'testSomething()' method such that 'Something' is specific to your needs; add others as needed, beginning each method with 'test...()'.
2) Add the '@Test' annotation to each new 'test...()' method you add.
3) Import the relevant modules and classes to support your tests.
4) Run this class as unit test app.
5) Include a screen shot of the report when you submit your assignment.

Please note: While some example test cases may be provided, you must write your own for the class.
"""
class DataUtilTest(unittest.TestCase):

	"""
	Use this to setup your tests. This is where you may want to load configuration
	information (if needed), initialize class-scoped variables, create class-scoped
	instances of complex objects, initialize any requisite connections, etc.
	"""
	def setUp(self):
		
		#instantiate DataUtil
		self.dataUtil = DataUtil()
		
		pass

	"""
	Use this to tear down any allocated resources after your tests are complete. This
	is where you may want to release connections, zero out any long-term data, etc.
	"""
	def tearDown(self):
		
		#set the reference to the variables to null to release any resources
		self.dataUtil = None
		
		pass
	
	"""
	/**
	 * This method tests the toJsonFromActuatorData() of DataUtil class
	 * Checks if two actuatorData instances with same values produce the same 
	 * JSONStr
	 */
	"""
	def testActuatorDataToJson(self):
		
		#instantiate two actuatorData instances
		actuatorData1 = ActuatorData()
		actuatorData2 = ActuatorData()
		
		#ceate two actuatorData instances and check if their jsonStr are equal
		actuatorData1.setName("Temp Actuator")
		actuatorData2.setName("Temp Actuator")
		actuatorData1.setCommand("INCREASE")
		actuatorData2.setCommand("INCREASE")
		actuatorData1.setValue("UP")
		actuatorData2.setValue("UP")
		
		#get their JSON strings 
		jsonStr1 = self.dataUtil.toJsonFromActuatorData(actuatorData1)
		jsonStr2 = self.dataUtil.toJsonFromActuatorData(actuatorData2)
		
		#check for equality
		self.assertEqual(jsonStr1, jsonStr2)
		
		#pass a non ActuatorData type to write
		jsonStr1 = self.dataUtil.toJsonFromActuatorData("Hello")
		
		#get the actuatorData back from the string passed
		actuatorData = self.dataUtil.toActuatorDataFromJson(jsonStr1)
		
		#the values should be "Not Set:
		self.assertEqual("Not Set", actuatorData.getCommand())
		self.assertEqual("Not Set", actuatorData.getName())
		self.assertEqual("Not Set", actuatorData.getValue())
		
		pass
	
	"""
	/**
	 * This method tests the toJsonFromSensorData() of DataUtil class
	 * Checks if two sensorData instances with same values produce the same 
	 * JSONStr 
	 */
	"""
	def testSensorDataToJson(self):
		
		#Create two sensorData instances
		sensorData1 = SensorData();
		sensorData2 = SensorData();
						
		#Create two sensor Data instances and check if their jsonStr are equal
		#First sensorData 
		sensorData1.setName("Temperature Sensor");
		sensorData1.addValue(9);
		
		#change timestamp to bogus value because they will be different
		sensorData1.timeStamp = "None"
						
		#Second sensorData
		sensorData2.setName("Temperature Sensor");
		sensorData2.addValue(9);
		
		#change timestamp to bogus value because they will be different 
		sensorData2.timeStamp = "None"
						
		#Get their JSON strings 
		jsonStr1 = self.dataUtil.toJsonFromSensorData(sensorData1);
		jsonStr2 = self.dataUtil.toJsonFromSensorData(sensorData2);
						
		#Check for equality
		self.assertEqual(jsonStr1, jsonStr2);
		
		pass
	
	
	"""
	/**
	 * This method tests writeSensorDataToFile() of DataUtil class.
	 */
	"""
	def testwriteSensorDataToFile(self):
		
		#create sensorData object
		sensorData = SensorData()
		
		#add a value
		sensorData.addValue(9)
		
		#write to file and assert True
		self.assertEqual(True, self.dataUtil.writeSensorDataToFile(sensorData))
		
		pass

	"""
	/**
	 * This method tests writeActuatorDataToFile() of DataUtil class. 
	 */
	"""
	def testwriteActuatorDataToFile(self):
		
		#create sensorData object
		actuatorData = ActuatorData()
		
		#add a value
		actuatorData.setName("Testinng")
		
		#write to file and assert True
		self.assertEqual(True, self.dataUtil.writeActuatorDataToFile(actuatorData))
		
		pass
	
	"""
	/**
	 * This method tests the toActuatorDataFromJson() of DataUtil class
	 * Checks if the actuatorData instances created from JSONString are equivalent in values
	 * and if they have the same data type
	 */
	"""
	def testJsonToActuatorData(self):
		
		#Create actuatorData
		actuatorData = ActuatorData();
				
		#Set some command, name and value
		actuatorData.setName("Temp Actuator");
		actuatorData.setCommand("INCREASE");
		actuatorData.setValue("UP");
				
		#convert to JSON 
		jsonStr = self.dataUtil.toJsonFromActuatorData(actuatorData);
				
		#convert back to ActuatorData
		actuatorDataTest = self.dataUtil.toActuatorDataFromJson(jsonStr);
				
		#test if their variables are equal
		self.assertEqual("Temp Actuator", actuatorDataTest.getName());
		self.assertEqual("INCREASE", actuatorDataTest.getCommand());
		self.assertEqual("UP", actuatorDataTest.getValue());
		
		"""		
		/*
			* Set the variable to a double value, check if the conversion to JsonStr and back 
			* to ActuatorData value remains of double type
		*/
		"""
				
		#Set some command, name and double value
		actuatorData.setName("Temp Actuator");
		actuatorData.setCommand("INCREASE");
		actuatorData.setValue(6.0);
				
		#convert to JSON 
		jsonStr = self.dataUtil.toJsonFromActuatorData(actuatorData);
				
		#convert back to ActuatorData
		actuatorDataTest = self.dataUtil.toActuatorDataFromJson(jsonStr);
				
		#test if their variables are equal
		self.assertEqual("Temp Actuator", actuatorDataTest.getName());
		self.assertEqual("INCREASE", actuatorDataTest.getCommand());
		self.assertEqual(6.0, actuatorDataTest.getValue());
	
	"""	
	/**
	 * This method tests the toSensorDataFromJson() of DataUtil class
	 * Checks if the sensorData instances created from JSONString are equivalent in values
	 * and if they have the same data type
	 */
	"""
	def testJsonToSensorData(self):

		#Create sensorData
		sensorData = SensorData();
						
		#Add some value and set a name
		sensorData.addValue(9.0);
		sensorData.setName("Temperature Sensor");
						
		#convert to JSON 
		jsonStr = self.dataUtil.toJsonFromSensorData(sensorData);
						
		#convert back to ActuatorData
		sensorDataTest = self.dataUtil.toSensorDataFromJson(jsonStr);
						
		#test if their variables are equal
		self.assertEqual("Temperature Sensor", sensorDataTest.getName());
		self.assertEqual(9.0, sensorDataTest.getCurrentValue(), 0);

	
if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testName']
	unittest.main()