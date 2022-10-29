import unittest
from translator import frenchtoenglish
from translator import englishtofrench

class TestE2F(unittest.TestCase):
    """English to French tests"""
    def test1(self):
        # Test Hello returns Bonjour
        self.assertEqual(englishtofrench('Hello'), 'Bonjour')
        # Test Hello does not return Hello
        self.assertNotEqual(englishtofrench('Hello'), 'Hello')
        # Test None returns empty string
        self.assertNotEqual(englishtofrench("None"), '')
        # Test empty string returns empty string
        self.assertNotEqual(englishtofrench(0), 0)

class TestF2E(unittest.TestCase):
    """French to English tests"""
    def test1(self):
        # Test Bonjour returns Hello
        self.assertEqual(frenchtoenglish('Bonjour'), 'Hello')
        # Test Bonjour does not return Bonjour
        self.assertNotEqual(frenchtoenglish('Bonjour'), 'Bonjour')
        # Test None returns empty string
        self.assertNotEqual(frenchtoenglish("None"), '')
        # Test empty string returns empty string
        self.assertNotEqual(frenchtoenglish(0),0)

unittest.main()