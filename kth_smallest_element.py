import random


def partition(arr, left, right):
    # Choose a random pivot to reduce worst-case probability
    pivot_index = random.randint(left, right)
    pivot_value = arr[pivot_index]

    # Move pivot to the end
    arr[pivot_index], arr[right] = arr[right], arr[pivot_index]

    store_index = left
    for i in range(left, right):
        if arr[i] < pivot_value:
            arr[store_index], arr[i] = arr[i], arr[store_index]
            store_index += 1

    # Move pivot to its final sorted position
    arr[right], arr[store_index] = arr[store_index], arr[right]
    return store_index


def quick_select(arr, left, right, k):
    if left == right:  # Base case: single element
        return arr[left]

    pivot_final_index = partition(arr, left, right)

    if k == pivot_final_index:
        return arr[k]
    elif k < pivot_final_index:  # Kth smallest is in the left partition
        return quick_select(arr, left, pivot_final_index - 1, k)
    else:  # Kth smallest is in the right partition
        return quick_select(arr, pivot_final_index + 1, right, k)


def find_kth_smallest_quickselect(arr, k):
    if not (1 <= k <= len(arr)):
        raise ValueError("k must be within the array's bounds")

    # We are looking for the element at index k-1 in a sorted array
    return quick_select(arr, 0, len(arr) - 1, k - 1)


# Example usage
arr = [7, 10, 4, 3, 20, 15]
k = 2
print(f"The {k}th smallest element (quickselect) is: {find_kth_smallest_quickselect(arr, k)}")