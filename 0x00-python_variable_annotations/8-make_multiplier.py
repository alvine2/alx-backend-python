#!/usr/bin/env python3
"""Contains  function that multiplies float by multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Multiplies  float by multiplier
    Args:
        multiplier (float): The multiplier
    Returns:
        A function that multiplies  float by multiplier
    """

    def multiplier_func(number: float) -> float:
        """Multiplies a float by multiplier"""
        return multiplier * number

    return multiplier_func
