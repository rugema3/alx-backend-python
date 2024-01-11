#!/usr/bin/env python3
"""5-sum_list module."""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Define sun_list function.
    Description:
                The function takes a list of floats as argument
                and returns a sum of the list as a float.
    """
    total = 0
    for input in input_list:
        total = total + input
    return total
