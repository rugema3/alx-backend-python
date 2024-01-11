#!/usr/bin/env python3
"""9-element_length module."""
from typing import List, Tuple


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """Calculate the length of each element in the input list.

    Args:
        lst (List[str]): The input list of strings.

    Returns:
        List[Tuple[str, int]]:  A list of tuples, each containing a string
                                from the input list
                            and its corresponding length.
    """
    return [(i, len(i)) for i in lst]
