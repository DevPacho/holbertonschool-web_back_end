#!/usr/bin/env python3
"""Measure the runtime"""

from time import time
from asyncio import run

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measures the total execution time for wait_n(n, max_delay),
    and returns total_time / n"""

    start_execution_time = time()
    run(wait_n(n, max_delay))
    finish_execution_time = time()

    total_time = finish_execution_time - start_execution_time
    measured_time = total_time / n

    return measured_time
