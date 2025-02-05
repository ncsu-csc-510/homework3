"""Module for debugging merge sort implementation."""

import rand

def merge_sort(input_arr):
    """Recursively sorts an array using merge sort algorithm."""
    if len(input_arr) == 1:
        return input_arr

    half = len(input_arr) // 2
    return recombine(merge_sort(input_arr[:half]), merge_sort(input_arr[half:]))

def recombine(left_arr, right_arr):
    """Merges two sorted arrays into a single sorted array."""
    left_index = 0
    right_index = 0
    merged_arr = [None] * (len(left_arr) + len(right_arr))

    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            merged_arr[left_index + right_index] = left_arr[left_index]
            left_index += 1
        else:
            merged_arr[left_index + right_index] = right_arr[right_index]
            right_index += 1

    while right_index < len(right_arr):
        merged_arr[left_index + right_index] = right_arr[right_index]
        right_index += 1

    while left_index < len(left_arr):
        merged_arr[left_index + right_index] = left_arr[left_index]
        left_index += 1

    return merged_arr

arr = rand.random_array([None] * 20)
arr_out = merge_sort(arr)

print(arr_out)
