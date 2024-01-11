#!/usr/bin/env python3
"""
A type-annotated function add.
"""


def add(a: float, b: float) -> float:
    """Define add function.
    description:
                This functions takes two arguments
                and returns their sum.
    Args:
            a(float): used annotations to clarify what type expected.
            b(float): Value as a float

    Return:
            The sum of the arguments.
    """
    return a + b
