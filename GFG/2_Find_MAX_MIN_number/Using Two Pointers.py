# Predefined array
arr = [1, 4, 3, 2, 6, 5]

def reverseArray(arr):
    left = 0                  # Start from the beginning
    right = len(arr) - 1     # Start from the end

    # Swap elements until the two pointers meet
    while left < right:
        # Swap the values at left and right positions
        arr[left], arr[right] = arr[right], arr[left]

        # Move the pointers towards each other
        left += 1
        right -= 1
        
    return arr

print(reverseArray(arr))
