import unittest
from gradescope_utils.autograder_utils.decorators import weight
import A9E1
import sys
import io
from contextlib import redirect_stdout

class TestA9E1(unittest.TestCase):
    @weight(40)
    def test_clean_string(self):
        """A9E1 - Testing clean_string() for functionality"""
        self.assertEqual(A9E1.clean_string('   great    lakes  '), "great lakes")
    
    @weight(20)
    def test_get_song_desc(self):
        """A9E1 - Testing get_song_desc() for valid input"""
        self.assertEqual(A9E1.get_song_desc('great lakes', 'CleoPAtrick'), 
                         "The song is GREAT LAKES by Cleopatrick")

    @weight(20)
    def test_get_movie_desc(self):
        """A9E1 - Testing get_movie_desc() for valid input"""
        self.assertEqual(A9E1.get_movie_desc('star WARS', 'george lucas', 'MARK HamiLL'), 
                         'The movie is "Star Wars", directed by George Lucas, starring Mark Hamill')

    @weight(20)
    def test_get_movie_desc_sequel(self):
        """A9E1 - Testing get_movie_desc() for sequel"""
        self.assertEqual(A9E1.get_movie_desc('SPIDER-man 2', 'sam raimi', 'TOBEY maguire'), 
                         'The movie sequel is "Spider-Man 2", directed by Sam Raimi, starring Tobey Maguire')

    @weight(50)
    def test_error_message(self):
        """A9E1 - Testing main() for complete functionality"""
        original_argv = sys.argv
        try:
            test_args = ['A9E1.py', '   star  WARS', '   gEorgE lUcas    ', '    MARK HamiLL       ']
            sys.argv = test_args

            # Redirect stdout to capture the print output from main
            with io.StringIO() as buf, redirect_stdout(buf):
                A9E1.main()
                output = buf.getvalue()

            expected_output = 'The movie is "Star Wars", directed by George Lucas, starring Mark Hamill\n'

            self.assertEqual(output, expected_output)
        finally:
            sys.argv = original_argv

    @weight(0)
    def test_ai_detection(self):
        """AI DETECTION"""
        self.assertEqual("D3ADB33FCAF3", "D3ADB33FCAF3")

if __name__ == '__main__':
    unittest.main()
