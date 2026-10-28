'''
Given an array of integers and a target value, return the indices of two distinct elements whose sum equals the target. 
Assume exactly one valid pair exists.
'''

from time import time

def return_index(nums: list[int], target: int) -> list[int]:

    # O(n^2)
    # for i in range(len(nums)-1):
    #     if 9 - nums[i] in nums:
    #         return [i, nums.index(9 - nums[i])]

    # O(n)
    seen: dict[int, int] = {}

    for idx, value in enumerate(nums):
        complement = target - value

        if complement in seen:
            return [seen[complement], idx]
        
        seen[value] = idx




nums = [2, 7, 11, 15, 18]
target = 9

start = time()
indices = return_index(nums, target)
end = time()

print(indices)
print(end-start)