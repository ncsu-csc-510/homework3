"""
This function demonstrates an implementation of binary search.
"""
def binary_search(arr, x, low, high):
    """
    Perform a binary search on a sorted array to find the target.

    Parameters:
        arr (list): The sorted array of integers.
        target (int): The element to search for.
        low (int): The starting index of the search range.
        high (int): The ending index of the search range.

    Returns:
        int: The index of the target if found, otherwise -1.
    """
    while low <= high:

        mid = low + (high - low)//2

        if x == arr[mid]:
            return mid
        if x > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1

    return -1

if __name__ == "__main__":
    arra = [3, 4, 5, 6, 7, 8, 9]
    Y = 3

    RESULT = binary_search(arra, Y, 0, len(arra)-1)

    if RESULT != -1:
        print("Element is present at index " + str(RESULT))
    else:
        print("Not found")
