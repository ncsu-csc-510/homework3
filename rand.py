"""Module for generating a random array."""

import random

def random_array(arr):
    """
    Generates a random array using a secure random generator.

    Args:
        arr (list): List to be filled with 20 random numbers.

    Returns:
        list: List filled with random numbers.
    """
    secure_random = random.SystemRandom()
    for i, _ in enumerate(arr):
        arr[i] = secure_random.randint(1, 20)
    return arr
