def dutch_flag_sort(arr):
    start = 0
    current = 0
    end = len(arr) - 1

    while current <= end:
        val = arr[current]
        if val == 0:
            arr[start], arr[current] = arr[current], arr[start]
            start += 1
            current += 1
        elif val == 2:
            arr[current], arr[end] = arr[end], arr[current]
            end -= 1
        else:  # val == 1
            current += 1
    return arr

# Example usage:
numbers = [0, 1, 2, 1, 0, 2, 1, 0]
result = dutch_flag_sort(numbers)
print(result)  # Output: [0, 0, 0, 1, 1, 1, 2, 2]
