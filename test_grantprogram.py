# test_grantprogram.py
"""
Tests for GrantProgram module.
"""

import unittest
from grantprogram import GrantProgram

class TestGrantProgram(unittest.TestCase):
    """Test cases for GrantProgram class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = GrantProgram()
        self.assertIsInstance(instance, GrantProgram)
        
    def test_run_method(self):
        """Test the run method."""
        instance = GrantProgram()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
