class TestExercise3(TestCommon):

    script_file = 'A6E3.py'

    @weight(10)
    def test_output(self):
        """Exercise 3 - Correct Output - 10 points"""
        test_input = "123"
        expected_output = '123" == 10\'3"'
        with unittest.mock.patch('builtins.input', return_value=test_input):
            output = subprocess.check_output(["python", self.script_file]).decode().strip()
            self.assertEqual(output, expected_output)

    @weight(10)
    def test_error_handling_non_integer(self):
        """Exercise 3 - Error Handling Non-Integer Input - 10 points"""
        test_input = "paneer"
        expected_output = "Error: Distance in inches must be an integer."
        with unittest.mock.patch('builtins.input', return_value=test_input):
            output = subprocess.check_output(["python", self.script_file]).decode().strip()
            self.assertEqual(output, expected_output)

    @weight(10)
    def test_constants_usage(self):
        """Exercise 3 - Use of Constants - 10 points"""
        with open(self.script_file, 'r') as file:
            code = file.read()
            self.assertIn("INCHES_PER_FEET", code, "You should define and use a constant for the number of inches in a foot.")

    # Additional test methods could include testing for different inputs and ensuring the output format is exactly as specified.
