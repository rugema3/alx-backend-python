#!/usr/bin/env python3
"""A modudule to loop 10 times."""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronous generator that yields a random number between 0 and 10
    after waiting for 1 second in each iteration.

    Yields:
        int: A random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
