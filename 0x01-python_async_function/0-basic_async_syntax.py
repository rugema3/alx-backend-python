#!/usr/bin/env python3
"""Module providing an asynchronous coroutine for generating random delays."""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay
    between 0 and max_delay seconds.

    Args:
        max_delay (float, optional):    The maximum delay in seconds
                                        (default is 10).

    Returns:
        float: The random delay waited.
    """
    # Generate a random delay between 0 and max_delay
    delay = random.uniform(0, max_delay)

    # Pause the coroutine for the generated delay
    await asyncio.sleep(delay)

    # Return the random delay
    return delay
