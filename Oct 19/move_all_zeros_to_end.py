'''
Given an integer array, move all zeroes to the end while preserving the relative order of non-zero elements. 
Modify the array in place.
'''

from time import time

def move_zero_to_end(input: list[int]):

    # O(n^2)
    # for i in range(len(input)-1):
    #     j = i+1
    #     if 0 == input[i]:
    #         while 0 == input[j] and j < len(input)-1:
    #             j += 1
    #         input[i], input[j] = input[j], input[i]

    # O(n)
    write = 0

    for value in input:
        if value != 0:
            input[write] = value
            write += 1

    for i in range(write, len(input)):
        input[i] = 0


input = [0, 1, 11, 0, 0, 12]

print(input)

start = time()
move_zero_to_end(input)
end = time()

print(input)
print(end-start)