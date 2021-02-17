#!/usr/bin/python3
"""
Test file for the base_mode class
"""
import unittest
from models.base_model import BaseModel


class TestClass(unittest.TestCase):

    def test_create_istance(self):
        new_model = BaseModel()
        self.assertIsInstance(new_model, BaseModel)


if __name__ == '__main__':
    unittest.main()
