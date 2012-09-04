import unittest
from fizz_buzz import fizz_buzz
import random

class test(unittest.TestCase):
    def test_get_three(self):
        
        # Arrange
        fizz_buzz_object = fizz_buzz()
        number = 3
        
        # Act
        actual_value = fizz_buzz_object.get(number)

        # Assert
        self.assertEqual(actual_value, "fizz")
        
    def test_get_five(self):
        
        # Arrange
        fizz_buzz_object = fizz_buzz()
        number = 5
        
        # Act
        actual_value = fizz_buzz_object.get(5)
        
        # Assert
        self.assertEqual(actual_value, 'buzz')
        
    
    def test_module_three(self):
        
        min_random_value = 1
        max_random_value = 33
        
        fizz_buzz_object = fizz_buzz()
        number = random.randint(min_random_value, max_random_value) *3 * 5 - 3
        
        actual_value = fizz_buzz_object.get(number)
        
        
        self.assertEqual(actual_value,'fizz')
        
        
    def test_module_five(self):
        
        min_random_value = 1
        max_random_value = 33
        
        fizz_buzz_object = fizz_buzz()
        number = random.randint(min_random_value, max_random_value) * 5 * 3 - 5
        
        actual_value = fizz_buzz_object.get(number)
        
        self.assertEqual(actual_value,'buzz')
        
    def test_module_three_five(self):
        
        min_random_value = 1
        max_random_value = 11
        
        
        fizz_buzz_object = fizz_buzz()
        number = random.randint(min_random_value, max_random_value) * 3 * 5
        
        actual_value = fizz_buzz_object.get(number)
        
        self.assertEqual(actual_value, 'fizzbuzz')
        
    def test_not_module_three_five(self):
        
        min_random_value = 1
        max_random_value = 11
        
        fizz_buzz_object = fizz_buzz()
        number = (random.randint(min_random_value, max_random_value) * 3 * 5) - 1
        
        actual_value = fizz_buzz_object.get(number)
        
        self.assertEqual(actual_value, number)
     
        
        
        
        
        