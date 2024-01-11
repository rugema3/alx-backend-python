#!/usr/bin/env python3
"""100-safe_first_element."""
from typing import Sequence, Union, Any, Optional


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Safely retrieve the first element of a sequence.

    Args:
        lst (Sequence[Any]): The input sequence.

    Returns:
        Union[Any, None]:   The first element of the sequence or None if
                            the sequence is empty.
    """
    if lst:
        return lst[0]
    else:
        return None
