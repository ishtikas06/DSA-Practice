""" Given an integer array, return the frequency of each distinct element. """

def count_frequency(arr: list[int]) -> dict:
    freq = {}

    # O(n)
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    return freq

arr = [5,5,5]

print(count_frequency(arr))