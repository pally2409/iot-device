#import libraries and modules
import unittest
import logging
from labs.common.SensorData import SensorData

#set the basic configuration to display time, level and the message
logging.getLogger("sensor data test logger")
logging.basicConfig(format='%(message)s', level=logging.DEBUG)

"""
Test class for all requisite SensorData functionality.

Instructions:
1) Rename 'testSomething()' method such that 'Something' is specific to your needs; add others as needed, beginning each method with 'test...()'.
2) Add the '@Test' annotation to each new 'test...()' method you add.
3) Import the relevant modules and classes to support your tests.
4) Run this class as unit test app.
5) Include a screen shot of the report when you submit your assignment.

Please note: While some example test cases may be provided, you must write your own for the class.
"""



class SensorDataTest(unittest.TestCase):

	"""
	Use this to setup your tests. This is where you may want to load configuration
	information (if needed), initialize class-scoped variables, create class-scoped
	instances of complex objects, initialize any requisite connections, etc.
	"""
	def setUp(self):
		
		#instantiate sensorData
		self.sensorData = SensorData()
		
		pass

	"""
	Use this to tear down any allocated resources after your tests are complete. This
	is where you may want to release connections, zero out any long-term data, etc.
	"""
	def tearDown(self):
		
		#set the reference to the variables to none to release any resources
		self.sensorData = None
	
	"""
	 This test tests the addValue() method of SensorData module. It checks whether the
	 values are being correctly stored by getting the current value, the average value and the count
	"""
	def testAddValue(self):
		
		logging.info('Running testAddValue()')
		
		#add any valid value
		self.sensorData.addValue(120)
		
		#the current value should represent the recently added value
		self.assertEqual(120, self.sensorData.getCurrentValue())
		
		#as it is the first test, the count should return 1
		self.assertEqual(1, self.sensorData.getCount())
		
		#add any valid value
		self.sensorData.addValue(140)
		
		#average value should return (120 + 140)/2 = 260/2 = 130 
		self.assertEqual(130, self.sensorData.getAverageValue())
		
		#add an invalid non-numeric value
		self.sensorData.addValue('blahblahblah')
		
		#current value should still remain 140
		self.assertEqual(140, self.sensorData.getCurrentValue())
		
		pass
	
	"""
	This test tests the getAverageValue() method of SensorData module. It checks whether the average is being 
	accurately calculated by the method
	
	"""
	def testGetAverageValue(self):
		
		#add some valid values
		self.sensorData.addValue(60)
		self.sensorData.addValue(90)
		self.sensorData.addValue(180)
		
		#get the average
		average = self.sensorData.getAverageValue()
		
		#check if average value = total value / count
		self.assertEqual(average, self.sensorData.totalValue/self.sensorData.getCount())
		
		#add invalid values and check if average remains the same
		self.sensorData.addValue(None)
		
		#check if average value = total value / count
		self.assertEqual(average, self.sensorData.totalValue/self.sensorData.getCount())
		
	"""
	 This test tests the getCount() method of SensorData module. It checks whether the count is 
	 incremented properly
	"""	
	def testGetCount(self):
		
		#add some valid values
		self.sensorData.addValue(30)
		self.sensorData.addValue(39)
		self.sensorData.addValue(300)
		
		#check if count is 3
		self.assertEqual(3, self.sensorData.getCount())

		#add an invalid value
		self.sensorData.addValue('baah')
		
		#check if count is still 3
		self.assertEqual(3, self.sensorData.getCount())
		
	"""
	 This test tests the getCurrentValue() method of SensorData module. It checks whether the current value is 
	 updated properly
	"""		
	
	def testGetCurrentValue(self):
		
		#add some valid value
		self.sensorData.addValue(30)
		
		#check if current value is 30
		self.assertEqual(30, self.sensorData.getCurrentValue())

		#add an invalid value
		self.sensorData.addValue('baah')
		
		#check if count is still 30
		self.assertEqual(30, self.sensorData.getCurrentValue())
		
		#add another valid value
		self.sensorData.addValue('60')
		
		#check if current value is 30
		self.assertEqual(60, self.sensorData.getCurrentValue())
	
	"""
	 This test tests the getMaxValue() method of SensorData module. It checks whether the max value is 
	 updated properly
	"""		
	
	def getMaxValue(self):
		
		#when there are no values it should return none
		self.assertEqual(None, self.sensorData.getMaxValue())
		
		#add a valid value
		self.sensorData.addValue('60')
		
		#check if max value updates to 60
		self.assertEqual(60, self.sensorData.getMaxValue())
		
		#add a large valid value
		self.sensorData.addValue('90')
		
		#check if max value updates to 60
		self.assertEqual(90, self.sensorData.getMaxValue())

	"""
	 This test tests the getMinValue() method of SensorData module. It checks whether the min value is 
	 updated properly
	"""
	def getMinValue(self):
		
		#when there are no values it should return none
		self.assertEqual(None, self.sensorData.getMinValue())
		
		#add a valid value
		self.sensorData.addValue('60')
		
		#check if max value updates to 60
		self.assertEqual(60, self.sensorData.getMinValue())
		
		#add a small valid value
		self.sensorData.addValue('-30')
		
		#check if min value updates to -30
		self.assertEqual(-30, self.sensorData.getMinValue())
	
	"""
	 This test tests the getName() method of SensorData module. It checks whether the 
	 the name is being returned properly
	"""
	def testGetName(self):
		
		#when name is not set, it has been initialized to 'Not Set', check if 'Not Set'
		self.assertEqual('Not Set', self.sensorData.getName())
		
		#change name
		self.sensorData.setName("Pallak's Sensor")
		
		#check whether the name is now "Pallak's Sensor"
		self.assertEqual("Pallak's Sensor", self.sensorData.getName())
	
		#check for none
		self.sensorData.setName(None)
		
		#it should return 'Not Set'
		self.assertEqual('Not Set', self.sensorData.getName())
	
	"""
	 This test tests the setName() method of SensorData module. It checks whether the 
	 the name is being updated properly
	"""
	def testSetName(self):
		
		#change name
		self.sensorData.setName("Temperature Sensor")
		
		#check whether the name is now "Temperature Sensor"
		self.assertEqual("Temperature Sensor", self.sensorData.getName())
	
		#change to none
		self.sensorData.setName(None)
		
		#check whether the name is now be 'Not Set'
		self.assertEqual("Not Set", self.sensorData.getName())
	


if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testName']
	unittest.main()