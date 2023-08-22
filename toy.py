def sum_array(arr):
    if not arr or len(arr) <= 2:
        return 0
        sorted_arr = sorted(arr)
        total_sum = sum(sorted_arr[1: -1])

array1 = [6, 2, 1, 8, 10]
array2 = [1, 1, 11, 2, 3]

result1 = sum_array(array1)
result2 = sum_array(array2)

print(result1)
