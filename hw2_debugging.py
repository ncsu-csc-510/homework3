"""Module providing functions to implement merge and bubble sort."""

import rand

def merge_sort(input_arr):
    """
    Performing merge sort.

    Args:
        input_arr (list): numbers to be sorted

    Returns:
        list: sorted list
    """
    if len(input_arr) <= 1:
        return input_arr

    half = len(input_arr) // 2

    return recombine(merge_sort(input_arr[:half]), merge_sort(input_arr[half:]))


def recombine(left_arr, right_arr):
    """
    Merging the two sorted arrays into a single sorted array.

    Args:
        left_arr (list): sorting the left half
        right_arr (list): sorting the right half

    Returns:
        list: Merged sorted array.
    """

    left_index = 0
    right_index = 0
    merged_arr = []

    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            merged_arr.append(left_arr[left_index])
            left_index += 1
        else:
            merged_arr.append(right_arr[right_index])
            right_index += 1

    merged_arr.extend(left_arr[left_index:])
    merged_arr.extend(right_arr[right_index:])

    return merged_arr

# Example Usage
array = rand.random_array([None] * 20)
array_out = merge_sort(array)

print(array_out)

def bubble_sort(input_arr):
    """
    Performing bubble sort on the input array.

    Args:
        input_arr (list): List of numbers to be sorted.

    Returns:
        list: Sorted list.
    """
    n = len(input_arr)
    for i in range(n):
        for j in range(n - i - 1):
            if input_arr[j] > input_arr[j + 1]:
                input_arr[j], input_arr[j + 1] = input_arr[j + 1], input_arr[j]

    return input_arr

# Example usage
array_bubble = rand.random_array([None] * 20)
array_out_bubble = bubble_sort(array_bubble)

print(array_out_bubble)
