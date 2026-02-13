import unittest
import os
import json
from app import ExpenseManager

class TestExpenseManager(unittest.TestCase):
    def setUp(self):
        self.test_file = 'test_expenses.json'
        self.manager = ExpenseManager(self.test_file)

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_add_expense(self):
        self.manager.add_expense("Test Item", 100)
        self.assertEqual(len(self.manager.expenses), 1)
        self.assertEqual(self.manager.expenses[0]['description'], "Test Item")

    def test_total_calculation(self):
        self.manager.add_expense("Item 1", 100)
        self.manager.add_expense("Item 2", 200)
        total = sum(e['amount'] for e in self.manager.expenses)
        self.assertEqual(total, 300)

if __name__ == '__main__':
    unittest.main()
