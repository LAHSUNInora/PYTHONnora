import unittest
from exe1 import safe_division

class TestExceptions(unittest.TestCase):
     def test_safe_division_zero(self):
            with self.assertRaises(ZeroDivisionError):
                safe_division(10, 0)
            
unittest.main()