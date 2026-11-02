""" 
Given an integer array nums and an integer k, return the k most frequent elements.
You may return the answer in any order. 
The input guarantees that exactly k distinct elements belong in the result.
"""
from operator import itemgetter

def k_most_frequent_elem(nums: list[int], k: int) -> list:
    elem = {}

    for num in nums:
        if num in elem:
            elem[num] += 1
        else:
            elem[num] = 1

    sorted_elem = dict(sorted(elem.items(), key=itemgetter(1), reverse=True))

    i = 0
    ans = []
    for key in sorted_elem.keys():
        if i < k:
            ans.append(key)
        i += 1

    return ans


nums = [1, 1, 1, 2, 2, 3]
k = 1

print(k_most_frequent_elem(nums, k))