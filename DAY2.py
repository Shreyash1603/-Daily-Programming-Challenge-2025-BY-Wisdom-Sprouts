def find_missing_by_sum(arr):
    n = len(arr) + 1
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    return expected_sum - actual_sum

def find_missing_by_xor(arr):
    n = len(arr) + 1
    xor_res = 0
    for i in range(1, n + 1):
        xor_res ^= i
    for num in arr:
        xor_res ^= num
    return xor_res

arr = [1, 2, 4, 5]
print(find_missing_by_sum(arr))
print(find_missing_by_xor(arr))
