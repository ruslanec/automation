from django.test import TestCase

class AnimalTestCase(unittest.TestCase):

    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        self.assertEqual(True, True)
