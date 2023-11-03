class TestExercise2(TestCommon):

    script_file = 'A6E2.py'

    @weight(10)
    def test_output(self):
        """Exercise 2 - Correct Output - 10 points"""
        test_input = "32"
        expected_output = f"{float(test_input):.2f} F == 0.00 C == 273.15 K"
        output = subprocess.check_output(["python", self.script_file, test_input]).decode().strip()
        self.assertEqual(output, expected_output)

    @weight(10)
    def test_fahrenheit_to_celsius_and_kelvin(self):
        """Exercise 2 - Fahrenheit to Celsius and Kelvin Conversion - 10 points"""
        test_input = "212"
        expected_celsius = (float(test_input) - 32) * 5/9
        expected_kelvin = expected_celsius + 273.15
        output = subprocess.check_output(["python", self.script_file, test_input]).decode().strip()
        self.assertIn(f"{expected_celsius:.2f} C", output)
        self.assertIn(f"{expected_kelvin:.2f} K", output)

    @weight(10)
    def test_f_string_usage(self):
        """Exercise 2 - Use of F-string Formatting - 10 points"""
        with open(self.script_file, 'r') as file:
            code = file.read()
            self.assertTrue(re.search(r'f".*:\.2f"', code), "You must use f-string format specifiers to round numbers.")
