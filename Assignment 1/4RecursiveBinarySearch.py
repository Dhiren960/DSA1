def binary_search(arr, key, low, high):
    if len(arr) == 0:
        return -1
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == key:
        return mid
    if key < arr[mid]:
        return binary_search(arr, key, low, mid - 1)
    return binary_search(arr, key, mid + 1, high)

arr = [1, 3, 5, 7, 9, 11, 13]

print(binary_search(arr, 7, 0, len(arr) - 1))
print(binary_search(arr, 1, 0, len(arr) - 1))
print(binary_search(arr, 13, 0, len(arr) - 1))
print(binary_search(arr, 2, 0, len(arr) - 1))

arr2 = []
print(binary_search(arr2, 5, 0, len(arr2) - 1))