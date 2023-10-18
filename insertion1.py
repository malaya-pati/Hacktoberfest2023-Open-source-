def insertion_sort(arr):
    """
    Perform insertion sort on the given array.

    Parameters:
    arr (list): An array of elements.

    Returns:
    list: The sorted array.
    """
    n = len(arr)

    # Traverse through all elements in the array
    for i in range(1, n):
        key = arr[i]
        j = i - 1

        # Move elements of arr[0..i-1], that are greater than key, to one position ahead of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr

# Example usage
unsorted_array = [64, 34, 25, 12, 22, 11, 90]

print("Unsorted array:", unsorted_array)
sorted_array = insertion_sort(unsorted_array)
print("Sorted array:", sorted_array)
