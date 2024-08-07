#!/usr/bin/env python3
'''This is Task 2's module.'''

import asyncio
import time
from importlib import import_module as using


async_comprehension = using('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''This will execute async_comprehension
    4x and measures the total execution time as well.
    '''
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - start_time
