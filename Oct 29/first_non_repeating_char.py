""" 
Given a string s, find the index of its first non-repeating character. 
Return -1 if every character repeats. 
"""

import math

def first_non_repeating_char(strng: str) -> int:
    # seen = {char: [index, count]}
    seen = {}

    # O(n)
    for i in range(len(strng)):
        char = strng[i]
        if char in seen:
            seen[char][1] += 1
        else:
            seen[char] = [i, 1]

    least = float("inf")

    for value in seen.values():
        if 1 == value[1]:
            if value[0] < least:
                least = value[0]

    if not math.isinf(least):
        return least

    return -1

strng = "aaabb"

print(first_non_repeating_char(strng))