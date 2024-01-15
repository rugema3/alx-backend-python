#!/usr/bin/env python3
"""Module providing asynchronous coroutine 4 concurrent waiting."""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous coroutine that spawns wait_random n times with the
    specified max_delay.

    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (float): The maximum delay in seconds for each wait_random.

    Returns:
        List[float]: List of delays in ascending order.
    """
    # Create a list to store the delays
    delays = []

    # Use asyncio.gather to concurrently spawn wait_random n times
    tasks = [wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*tasks)

    # Return the list of delays in ascending order
    return sorted(results)
