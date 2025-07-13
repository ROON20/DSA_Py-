"""Array Reverse 

Given an array arr[], the task is to reverse the array. 
Reversing an array means rearranging the elements such that the first element becomes the last, the second element becomes second last and so on."""

''' Using a temporary array - O(n) Time and O(n) Space  '''

arr = [10, 20, 30, 40, 50]  # Predefined array

# Function to reverse an array using a temporary array
def reverseArray(arr):
    n = len(arr)  # Step 1: Get the number of elements in the array

    # Step 2: Create a new temporary array of the same size
    temp = [0] * n

    # Step 3: Copy elements from original array to temp in reverse order
    for i in range(n):
        temp[i] = arr[n - i - 1]

    # Step 4: Copy the reversed elements back to the original array
    for i in range(n):
        arr[i] = temp[i]
        
    return arr


 # Call the function
print(reverseArray(arr))


''' Using Two Pointers - O(n) Time and O(1) Space   '''

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



''' Array reverse   '''

arr = [1, 4, 3, 2, 6, 5]

def reverse_array(arr):
    arr.reverse()     # Reverses the list in-place
    return arr        # Optional return, since arr is modified directly

reverse_array(arr)

print(arr)            # Prints the reversed array
