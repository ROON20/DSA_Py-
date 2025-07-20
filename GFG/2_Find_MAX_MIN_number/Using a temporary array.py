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
