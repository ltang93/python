import unittest
from apptest import AppUnit

mysuite=unittest.TestSuite()
mysuite.addTest(AppUnit.MyTestCase('test_something'))
mysuite.addTest(AppUnit.MyTestCase('test_something1'))


runner=unittest.TextTestRunner()
runner.run(mysuite)
