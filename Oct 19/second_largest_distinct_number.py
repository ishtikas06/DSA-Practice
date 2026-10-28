def second_largest(input: list[int]) -> int:
    n = m = -100
    for i in input:
        if i > m:
            m = i
        elif i < m and i > n:
            n = i
    return n

input = [12, 35, 1, 10, 34, 35]

second_largest_num = second_largest(input)
print(second_largest_num)