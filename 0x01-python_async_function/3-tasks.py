#!/usr/bin/env python3
"""
Module providing a function to create an asyncio.Task for wait_random.
"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create an asyncio.Task for the wait_random function
    with the given max_delay.

    Args:
        max_delay (float): The maximum delay in seconds for wait_random.

    Returns:
        asyncio.Task: A Task representing the execution of wait_random.
    """
    # Create an event loop
    loop = asyncio.get_event_loop()

    # Create a task for the wait_random function
    task = loop.create_task(wait_random(max_delay))

    return task
