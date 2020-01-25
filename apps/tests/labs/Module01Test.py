import unittest
from labs.module01	import SystemMemUtilTask
from labs.module01	import SystemCpuUtilTask



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
		

	"""
		Tearing down any allocated resources after the tests are complete
	"""
	def tearDown(self):
		
		#set the reference to the tasks as none to release the resources they're holding
		self.systemCpuUtilTask = None
		self.systemMemUtilTask = None
		
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

		
if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testName']
	unittest.main()
	