import unittest
from labs.module01	import SystemMemUtilTask
from labs.module01	import SystemCpuUtilTask
from labs.module01	import SystemPerformanceAdaptor



"""
Test class for all requisite Module01 functionality.

Instructions:
1) Rename 'testSomething()' method such that 'Something' is specific to your needs; add others as needed, beginning each method with 'test...()'.
2) Add the '@Test' annotation to each new 'test...()' method you add.
3) Import the relevant modules and classes to support your tests.
4) Run this class as unit test app.
5) Include a screen shot of the report when you submit your assignment.

Please note: While some example test cases may be provided, you must write your own for the class.
"""
class Module01Test(unittest.TestCase):

	"""
		Setting up variables required for the tests
	"""
	def setUp(self):
		
		#instantiate the tasks
		self.systemCpuUtilTask = SystemCpuUtilTask.SystemCpuUtilTask()
		self.systemMemUtilTask = SystemMemUtilTask.SystemMemUtilTask()
		
		#instantiate the adaptor
		self.systemPerformanceAdaptor = SystemPerformanceAdaptor.SystemPerformanceAdaptor()
	"""
		Tearing down any allocated resources after the tests are complete
	"""
	def tearDown(self):
		
		#set the reference to the tasks as none to release the resources they're holding
		self.systemCpuUtilTask = None
		self.systemMemUtilTask = None
		self.systemPerformanceAdaptor = None
		
		
	'''
		This test tests whether the CPU utilization percent returned by the corresponding task method
		is greater than 0.0 and less than or equal to 100.0
	'''
	def testSystemCpuUtilTask(self):
		
		cpuUtil = self.systemCpuUtilTask.getSensorData()
		
		#check if its true whether the cpu utilization is > 0.0 and <= 100.0
		self.assertTrue(0.0 < cpuUtil, 'CPU Utilization less than 0.0')
		self.assertTrue(100.0 >= cpuUtil, 'CPU Utilization greater than 100.0')
	
			
	'''
		This test tests whether the Memory utilization percent returned by the corresponding task method
		is greater than 0.0 and less than or equal to 100.0
	'''
	def testSystemMemUtilTaskTest(self):
		
		memUtil = self.systemMemUtilTask.getSensorData()
		
		#check if its true whether the memory utilization is > 0.0 and <= 100.0
		self.assertTrue(0.0 < memUtil, 'Memory Utilization less than 0.0')
		self.assertTrue(100.0 >= memUtil, 'Memory Utilization greater than 100.0')

	
	def testSystemPerformanceAdaptor(self):
		
		#return value from system performance adaptor's run function
		success = self.systemPerformanceAdaptor.run()
		
		#check if the return is false when the enableAdaptor variable of adaptor is false
		self.assertEqual(success, False, 'Adaptor did not run because adaptor was disabled')
		
		#set the number of readings required to 0
		self.systemPerformanceAdaptor.numReadings = 0
		
		#return value from system performance adaptor's run function
		success = self.systemPerformanceAdaptor.run()
		
		#check if the return is false when the number of readings required were 0
		self.assertEqual(success, False, 'Adaptor did not run because number of readings entered were 0')
		
		#set the number of readings to a small value 
		self.systemPerformanceAdaptor.numReadings = 1
		
		#set the sleep time to a small value
		self.systemPerformanceAdaptor.rateInSec = 3
		
		#enable the adaptor
		self.systemPerformanceAdaptor.enableAdaptor = True
		
		#return value from system performance adaptor's run function
		success = self.systemPerformanceAdaptor.run()
		
		#check if the return is true when the adaptor runs and provides some readings
		self.assertEqual(success, True, 'Adaptor did run')
		
		
if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testName']
	unittest.main()
	