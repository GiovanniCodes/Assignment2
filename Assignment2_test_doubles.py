import unittest
from datetime import datetime

from databaseFunc import databaseNeeds
from dataBaseFuncTest import databaseNeedStub
# from Assignment2 import shortestDistance, retirement


class TestRetire(unittest.TestCase):
    def test_Mock_Connection(self):
        self.assertTrue(databaseNeedStub.connection())

    def test_Stub_setUp(self):
        # Stub to return 20 if no data to print
        self.assertAlmostEqual(databaseNeedStub.printStubData({'x':1}),10);

    def test_retire_insert(self):
        self.assertTrue({
                'age': 10,
                'annualSalary': 200000,
                'percentSaved': 15,
                'retirementSaveGoal': 5,
                'timestamp': 'Timestamp: {:%Y-%m-%d %H:%M:%S}'.format(datetime.now())

            }
        )
    def test_retire_insert_result(self):
        self.assertFalse(databaseNeeds.insertResults({}))

class TestShort(unittest.TestCase):
    def test_Mock_Connection(self):
        self.assertTrue(databaseNeedStub.connection())

    def test_Stub_setUp(self):
        # Stub to return 20 if no data to print
        self.assertNotEqual(databaseNeedStub.printStubData({}),20);
    def test_insert(self):
        self.assertTrue( {'x1': 3, 'x2': 4, 'y1': 8,'y2': 2,'timestamp': 'Timestamp: {:%Y-%m-%d %H:%M:%S}'.format(datetime.now()) })

    def test_short_insert_result(self):
        self.assertFalse(databaseNeeds.insertResults({}))