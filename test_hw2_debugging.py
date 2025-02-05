"""
Including test cases for merge sort
"""

import pytest
from hw2_debugging import merge_sort

def test_empty_list():
    """
    Testing merge sort on an empty list
    """
    arr = []
    expected = []
    assert merge_sort(arr) == expected

def test_sorted_list():
    """
    Test merge sort on an already sorted list.
    """
    arr = [1, 2, 3, 4, 5]
    expected = [1, 2, 3, 4, 5]
    assert merge_sort(arr) == expected

def test_duplicate_values():
    """
    Test merge sort with duplicate values in the list.
    """
    arr = [4, 2, 2, 8, 3, 3, 1]
    expected = [1, 2, 2, 3, 3, 4, 8]
    assert merge_sort(arr) == expected