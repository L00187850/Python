#Name: Philip Stewart
#Student Number: L00187850
#Date: 25 Nov 2024
#Purpose: Building a Test

"""

This part will show how to build a test from creating a class, methods and importing two files.
"""

import unittest  # This is the built-in module.
import formater  # This is your formater.py file in the same directory.

class TestFormater(unittest.TestCase):
    """
    This is a test case for the formater module.
    It tests the funtions on it called convert_upper,convert_lower and convert_town"
    """
    def test_lower(self):
        """
        This test helps in converting strings to lowercase.
        """

        test_text = "PHILIP STEWART"
        result = formater.convert_lower(test_text)
        self.assertEqual(result, "philip stewart")

    def test_upper(self):
        """
        This test helps in converting strings to uppercase.
        """
        test_text = "Philip Stewart"
        result = formater.convert_upper(test_text)
        self.assertEqual(result, "PHILIP STEWART")

#Johns Code
#    def test_upper(self):
#        test_text = "John ORaw"
#        result = formatter.convert_upper(test_text)
#        self.assertEqual(result, "JoHN ORAW")


####I added another method and added that on error throw up


    def test_invalid(self):
        """
        This test throws an AttributeError when an invalid type is passed.
        """

        with self.assertRaises(AttributeError):
# This part of the command gives an example of what an incorrect input looks like
# for example in the form of a list and not a string.
            formater.convert_lower(["Error 404"])

        with self.assertRaises(AttributeError):
             #I added a list here instead of just a string, from a previous example.
            formater.convert_upper(["Philip", "Stewart"])
if __name__ == "__main__":
    unittest.main()
