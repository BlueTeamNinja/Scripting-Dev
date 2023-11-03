class TestExercise1(TestCommon):

    script_file = 'A6E1.py'

    @weight(10)
    def test_output(self):
        """Exercise 1 - Correct Output - 10 points"""
        test_name = "Jeremy"
        expected_output = f"{test_name} is the most amazing person I have ever met.\n"
        expected_output += f"My mother is always saying, \"You need to be more like {test_name}.\"\n"
        expected_output += f"Dear {test_name}: You rock!\n"
        output = subprocess.check_output(["python", self.script_file, test_name]).decode().strip()
        self.assertEqual(output, expected_output)

    @weight(10)
    def test_sys_argv_usage(self):
        """Exercise 1 - Use of sys.argv - 10 points"""
        with open(self.script_file, 'r') as file:
            code = file.read()
            self.assertIn('sys.argv', code, "You must use sys.argv to handle command-line arguments.")

    @weight(10)
    def test_handling_no_arguments(self):
        """Exercise 1 - Handling No Arguments - 10 points"""
        # We will check if an appropriate error or usage message is displayed if no arguments are passed.
        # The specific message is not standardized here, so you should provide additional context in your class.
        with self.assertRaises(subprocess.CalledProcessError):
            subprocess.check_output(["python", self.script_file])
