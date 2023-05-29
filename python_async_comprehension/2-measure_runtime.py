#!/usr/bin/env python3
"""Measure runtime"""

from time import time
from asyncio import gather

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """This coroutine will execute async_comprehension four times
        in parallel using asyncio.gather. Then, should measure the
        total runtime and return it."""

    start_execution_time = time()
    await gather(*(async_comprehension() for _ in range(4)))
    finish_execution_time = time()

    total_execution_time = finish_execution_time - start_execution_time
    return total_execution_time
