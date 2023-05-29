#!/usr/bin/env python3
"""Multiple coroutines at the same time with async and creating async task"""

from typing import List
from asyncio import create_task

wait_n = __import__('1-concurrent_coroutines').wait_n


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """The code is nearly identical to wait_n
    except task_wait_random is being called."""

    return await create_task(wait_n(n, max_delay))
