#!/usr/bin/env python3
"""7-to_kv module."""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Converts a string-key and int/float-value pair to a tuple.

    Args:
        k (str): The input string key.
        v (Union[int, float]): The input int or float value.

    Returns:
        Tuple[str, float]: A tuple containing the string key and
        the square of the int/float value.
    """
    result: float = float(v ** 2)
    return k, result
