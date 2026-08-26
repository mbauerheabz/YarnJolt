# test_yarnjolt.py
"""
Tests for YarnJolt module.
"""

import unittest
from yarnjolt import YarnJolt

class TestYarnJolt(unittest.TestCase):
    """Test cases for YarnJolt class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = YarnJolt()
        self.assertIsInstance(instance, YarnJolt)
        
    def test_run_method(self):
        """Test the run method."""
        instance = YarnJolt()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
