#!/usr/bin/env python3
"""6-sum_mixed_list module that handles summation of mixed lists."""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Define sum_mixed_list function.
    Description:
                The function takes argument conatining a list of both
                integers and floats.

                It then returns their sum as a float.
    """
    total = 0
    for input in mxd_lst:
        total = total + input
    return total
