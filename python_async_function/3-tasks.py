#!/usr/bin/env python3
"""asyncio.Task"""

from asyncio import create_task

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int):
    """Creating asynchronous tasks"""

    return create_task(wait_random(max_delay))
