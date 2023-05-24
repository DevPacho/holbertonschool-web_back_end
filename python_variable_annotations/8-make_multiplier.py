#!/usr/bin/env python3
"""Complex types - functions"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[([float], float)]:
    """
    Type-annotated function 'make_multiplier' that takes a float 'multiplier'
    as argument and returns a function that multiplies a float by 'multiplier'.
    """

    def callable_multiplier(n: float) -> float:
        """Callable function that returns the result"""
        return multiplier * n
    return callable_multiplier
