#!/usr/bin/env python3
"""101-safely_get_value module."""
from typing import Mapping, Any, Union, TypeVar, Optional

T = TypeVar('T')


def safely_get_value(
    dct: Mapping,
    key: Any,
    default: Optional[T] = None
) -> Union[Any, T]:
    """Safely get a value from a dictionary.

    Args:
        dct (Mapping): The input dictionary (using the Mapping type).
        key (Any): The key to look up in the dictionary.
        default (Optional[U]): The default value to return if the key is
                                not present (default is None).

    Returns:
        Union[Any, T]: The value associated with the key in the dictionary,
        or the default value if the key is not present.
    """
    if key in dct:
        return dct[key]
    else:
        return default
