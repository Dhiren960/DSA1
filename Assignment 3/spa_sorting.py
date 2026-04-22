import time
import random


def insertion_sort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > temp:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = temp


def merge(left, right):
    final = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            final.append(left[i])
            i += 1
        else:
            final.append(right[j])
            j += 1

    final.extend(left[i:])
    final.extend(right[j:])

    return final


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left_part = merge_sort(arr[:mid])
    right_part = merge_sort(arr[mid:])

    return merge(left_part, right_part)


def partition(arr, low, high):
    pivot = arr[low]
    left = low + 1
    right = high

    while True:
        while left <= right and arr[left] <= pivot:
            left += 1

        while left <= right and arr[right] >= pivot:
            right -= 1

        if left > right:
            break

        arr[left], arr[right] = arr[right], arr[left]

    arr[low], arr[right] = arr[right], arr[low]
    return right


def quick_sort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)

        quick_sort(arr, low, p - 1)
        quick_sort(arr, p + 1, high)


def measure(sort_func, arr, quick=False):
    copy_arr = arr.copy()

    start = time.time()

    if quick:
        sort_func(copy_arr, 0, len(copy_arr) - 1)
    else:
        result = sort_func(copy_arr)
        if result is not None:
            copy_arr = result

    end = time.time()

    return (end - start) * 1000


def generate_data():
    sizes = [1500, 6000, 12000]
    dataset = {}

    for size in sizes:
        random.seed(25)

        dataset[(size, "random")] = [
            random.randint(10, 50000) for _ in range(size)
        ]

    return dataset


if __name__ == "__main__":

    sample = [12, 7, 3, 19, 4, 11]

    print("Correctness Check:")
    print("Original:", sample)

    temp1 = sample.copy()
    insertion_sort(temp1)
    print("Insertion:", temp1)

    print("Merge:", merge_sort(sample.copy()))

    temp2 = sample.copy()
    quick_sort(temp2, 0, len(temp2) - 1)
    print("Quick:", temp2)

    print("\n--- PERFORMANCE TABLE ---")

    datasets = generate_data()

    for (size, dtype), values in datasets.items():
        print(f"\nSize: {size}, Type: {dtype}")

        t1 = measure(insertion_sort, values)
        t2 = measure(merge_sort, values)
        t3 = measure(quick_sort, values, True)

        print("Insertion Sort:", round(t1), "ms")
        print("Merge Sort:", round(t2), "ms")
        print("Quick Sort:", round(t3), "ms")