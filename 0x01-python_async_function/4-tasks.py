#!/usr/bin/env python3
"""
Module providing asynchronous coroutines for concurrent
waiting with random delays.
"""

import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous coroutine that spawns task_wait_random n times
    with the specified max_delay.

    Args:
        n (int): The number of times to spawn task_wait_random.
        max_delay (float): The maximum delay in seconds for each
                            task_wait_random.

    Returns:
        List[float]: List of delays in ascending order.
    """
    # Create a list to store the delays
    delays = []

    # Use asyncio.gather to concurrently spawn task_wait_random n times
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*tasks)

    # Return the list of delays in ascending order
    return sorted(results)
