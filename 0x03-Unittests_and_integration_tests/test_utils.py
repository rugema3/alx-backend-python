#!/usr/bin/env python3
"""
Test access_nested_map function.
"""
import unittest
import requests
from unittest.mock import patch
from typing import Mapping, Sequence, Any
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """Test class for the access_nested_map function."""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map: Mapping[str, Any],
                               path: Sequence[str], expected: Any) -> None:
        """Test access_nested_map function with different inputs.

        Parameters:
            nested_map (Mapping): The nested map.
            path (Sequence): The path to access.
            expected (Any): The expected result.

        Returns:
            None
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Sequence) -> None:
        """Test access_nested_map function raises KeyError for invalid inputs.

        Parameters:
            nested_map (Mapping): The nested map.
            path (Sequence): The path to access.


        Returns:
            None
        """
        with self.assertRaises(Exception):
            access_nested_map(nested_map, path)


if __name__ == '__main__':
    unittest.main()
