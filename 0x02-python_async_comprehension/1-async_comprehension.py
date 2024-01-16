#!/usr/bin/env python3
"""
Module to define an asynchronous coroutine using async comprehensions.
"""

import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Asynchronous coroutine that collects 10 random numbers
    using an async comprehension over async_generator.

    Returns:
        List[float]: A list containing 10 random numbers.
    """
    # Using asynchronous comprehension to collect 10 random numbers
    random_numbers = [i async for i in async_generator()]
    return random_numbers
