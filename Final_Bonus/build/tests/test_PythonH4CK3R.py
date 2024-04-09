import unittest
from PythonH4CK3R import set_password, brute_force_attack, performance_analysis
from gradescope_utils.autograder_utils.decorators import weight
import importlib
import time
import os
import random

class TestPythonH4CK3R(unittest.TestCase):

    def test_set_password(self):
        """Testing set_password function with a known seed"""
        expected_password = "7503544"  # Expected password for seed 42 and length 4
        self.assertEqual(set_password(7,677977805654), expected_password, "NO WAY.  WE HAVE THE SAME RANDOM NUMBER.  Seeds are cool.  They grow things. ")

    def test_brute_force_attack(self):
        """Testing brute_force_attack function"""
        password = "7503544"  # Ensure no leading zeros
        start = 7393000
        _, attempts = brute_force_attack(password, start=start)

        # The number of attempts is the difference between the password and the start value, plus one
        expected_attempts = int(password) - start + 1
        self.assertEqual(attempts, expected_attempts,f"My ultimate Ninja password should be cracked in only {expected_attempts} attempts!")



    def test_performance_analysis(self):
        """Testing performance_analysis function"""
        start_time = time.time()
        time.sleep(1)  # Simulating a delay of 1 second
        end_time = time.time()
        _, attempts_per_sec = performance_analysis(start_time, end_time, 1000)
        self.assertAlmostEqual(attempts_per_sec, 1000, delta=100)
        print(f"My potatoe can outrun your potatoe for sure.")  # Allowing a variance

    # Additional tests for base64 encoded conditions with misleading headings
#    @weight(0)
#    def test_format_string_check(self):
#        """Format string Check"""
#        troll = random.choice([True,False])
#        self.assertTrue(troll, "This test literally does nothing.  Or does it?  Can you figure out how to pass it?")  # Needed 1 more test to make the list the right size

    def test_bruce_forte_evaluation(self):
        """Bruce Forte Evaluation"""
        success = False
        busted = False

        try:
            # Try running the script normally
            import PythonH4CK3R
            success = True
            self.assertTrue(True, "You are the not the Bruce Forte we are looking for.  This is a good thing.")  # Placeholder test

        except ImportError:
            # If there's an ImportError, try importing potential missing modules
            try:
                import random
                import time
                import datetime
                importlib.reload(PythonH4CK3R)
                success = True
                busted = True  # Indicates the script ran successfully only after importing missing modules
            except ImportError:
                pass  # If it still fails, success remains False

        self.assertTrue(success)
        if busted:
            self.assertTrue(True, "You just got busted cheating, homie.  Was it worth it?")  # Placeholder test

    def test_robin_laid_an_easter_egg(self):
        """Robin laid an Easter Egg"""
        comment_text = "# Fleming College has been notified of this use of AI"

        # Path to the PythonH4CK3R.py script
        script_path = "PythonH4CK3R.py"  # Update this if the script is in a different location

        if os.path.exists(script_path):
            with open(script_path, "r") as file:
                for line in file:
                    if comment_text in line:
                        self.assertTrue(False,"Oh. You really shouldn't have submitted this.  Busted.")
                        break

        self.assertTrue(True, "You're not the Robin we need.")

if __name__ == '__main__':
    unittest.main()
