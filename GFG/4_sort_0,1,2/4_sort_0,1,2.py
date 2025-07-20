
def sort_012(arr):
    low = 0         # Pointer for 0s
    mid = 0         # Current element
    high = len(arr) - 1  # Pointer for 2s

    # Traverse the array
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:  # arr[mid] == 2
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    return arr

# Example usage
arr = [0, 1, 2, 0, 1, 2]
sorted_arr = sort_012(arr)
print("Sorted array:", sorted_arr)
