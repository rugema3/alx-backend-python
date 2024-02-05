#!/usr/bin/env python3
"""
Test access_nested_map function.
"""
import unittest
from parameterized import parameterized
from typing import Mapping, Sequence, Any

from utils import access_nested_map


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


if __name__ == '__main__':
    unittest.main()
