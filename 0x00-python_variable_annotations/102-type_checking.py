#!/usr/bin/env python3
"""102-type_checking module."""
from typing import Tuple, List, Any


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Zoom in on the elements of a tuple by repeating each element.

    Args:
        lst (Tuple): The input tuple.
        factor (int, optional): The factor by which to repeat each
                                element (default is 2).

    Returns:
        List:   A list containing each element of the input
                tuple repeated by the specified factor.
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in
