import unittest
from main import square_root, process_random_integer, divisible_numbers # type: ignore

class TestFunctions(unittest.TestCase):
    
    def test_square_root_positive(self):
        self.assertAlmostEqual(square_root(4), 2)
        self.assertAlmostEqual(square_root(9), 3)
        
    def test_square_root_negative(self):
        with self.assertRaises(ValueError):
            square_root(-1)
            
    def test_process_random_integer(self):
        # Since process_random_integer involves randomness, mocking would be better.
        with self.assertRaises(ValueError):
            process_random_integer()
    
    def test_divisible_numbers(self):
        self.assertEqual(divisible_numbers(2), [2, 4, 6, 8, 10])
        self.assertEqual(divisible_numbers(3), [3, 6, 9])
        with self.assertRaises(ValueError):
            divisible_numbers(0)

if __name__ == '__main__':
    unittest.main()
