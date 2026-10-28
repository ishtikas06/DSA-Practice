"""Find the maximum sum of a non-empty contiguous subarray."""


def max_subarray_sum(arr: list[int]) -> int:

    # O(n^2)
    max_sum = arr[0]
    i = j = 0
    while j < len(arr):
        sum = None
        for idx in range(i, len(arr)):
            if sum == None:
                sum = arr[idx]
            else:
                sum += arr[idx]
    
            if max_sum < sum:
                max_sum = sum
    
        i += 1
        j += 1

    # O(n)
    # Kadane's Algorithm
    if not arr:
        raise ValueError("arr must not be empty")

    max_sum = current_sum = arr[0]

    for value in arr[1:]:
        current_sum = max(value, current_sum + value)
        max_sum = max(max_sum, current_sum)

    return max_sum


if __name__ == "__main__":
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(max_subarray_sum(arr))