#!/usr/bin/python3
"""Unittest for max_integer([..])
"""

import unittest
from 6-max_integer import max_integer


class TestMaxInteger(unittest.TestCase):
    """
    This class contains unittests for the max_integer function.
    """

    def test_max_at_end(self):
        """Test case where the max integer is at the end of the list."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_at_beginning(self):
        """Test case where the max integer is at the beginning of the list."""
        self.assertEqual(max_integer([4, 1, 2, 3]), 4)

    def test_max_in_middle(self):
        """
        Test case where the max integer is somewhere in the middle of the list
        """
        self.assertEqual(max_integer([1, 4, 2, 3]), 4)

    def test_one_element(self):
        """Test case where the list contains only one element."""
        self.assertEqual(max_integer([4]), 4)

    def test_empty_list(self):
        """Test case where the list is empty."""
        self.assertIsNone(max_integer([]))

    def test_negative_integers(self):
        """Test case where the list contains negative integers."""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_all_same_elements(self):
        """Test case where all elements in the list are the same."""
        self.assertEqual(max_integer([7, 7, 7, 7]), 7)

    def test_with_zero(self):
        """Test case where the list includes zero."""
        self.assertEqual(max_integer([0, 1, 2, 3]), 3)

    def test_none_input(self):
        """Test case where None is passed instead of a list."""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_non_int_elements(self):
        """Test case where the list contains non-integer elements."""
        with self.assertRaises(TypeError):
            max_integer([1, 2, "three", 4])


if __name__ == "__main__":
    unittest.main()
