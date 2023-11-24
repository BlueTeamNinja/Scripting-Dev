import unittest
from gradescope_utils.autograder_utils.decorators import weight
import A9E1

class TestA9E1(unittest.TestCase):
    @weight(60)
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

    @weight(20)
    def test_error_message(self):
        """A9E1 - Testing main() for error message"""
        # Assuming A9E1.main() returns the output instead of printing
        self.assertEqual(A9E1.main(['A9E1.py', 'Empire Strikes Back']),
                         "Error: Missing parameters")

    @weight(0)
    def test_ai_detection(self):
        """AI DETECTION"""
        self.assertEqual("D3ADB33FCAF3", "D3ADB33FCAF3")

if __name__ == '__main__':
    unittest.main()
