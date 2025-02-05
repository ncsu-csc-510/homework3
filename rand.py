"""Module for generating a random array using the `secrets` module."""

import secrets

def random_array(arr):
    """Fills an array with secure random numbers between 1 and 20."""
    for i, _ in enumerate(arr):
        arr[i] = secrets.randbelow(20) + 1
    return arr
