#!/usr/bin/env python3
"""Multiple coroutines at the same time with async"""

from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Takes in 2 int arguments (in this order): n and max_delay.
        You will spawn wait_random n times with the specified max_delay."""

    delays = []

    for _ in range(n):
        delay_times = await wait_random(max_delay)
        delays.append(delay_times)

    return sorted(delays)
