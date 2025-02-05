"""Module implementing Counting Sort for character sorting."""

def counting_sort(input_arr):
    """Sorts a string using Counting Sort algorithm."""

    output = [0] * 256
    count = [0] * 256

    for char in input_arr:
        count[ord(char)] += 1

    for i in range(1, 256):
        count[i] += count[i - 1]

    for char in reversed(input_arr):
        output[count[ord(char)] - 1] = char
        count[ord(char)] -= 1

    return "".join(output[:len(input_arr)])

INPUT_STRING = "anchalkakadia"
SORTED_STRING = counting_sort(INPUT_STRING)

print(f"Sorted character array is {SORTED_STRING}")
