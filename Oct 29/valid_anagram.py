"""
Given two strings s and t, determine whether t is an anagram of s.
Two strings are anagrams if they contain exactly the same characters with the same frequencies.
"""

# O(n)
def check_valid_anagram(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False

    char = {}

    for elem in s1:
        if elem in char:
            char[elem] += 1
        else:
            char[elem] = 1

    for elem in s2:
        if elem not in char:
            return False
        else:
            char[elem] -= 1

    for val in char.values():
        if val != 0:
            return False

    return True

s1 = "anagram"
s2 = "nagaram"

print(check_valid_anagram(s1, s2))