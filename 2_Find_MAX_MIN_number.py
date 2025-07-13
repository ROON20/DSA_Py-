'''Maximum and minimum of an array using comparisons'''

# Array input
arr = [4, 9, 6, 5, 2, 3]

def find_min_max(arr):
    n = len(arr)

    if n == 0:
        return None, None

    # Set initial min and max
    if n % 2 == 0:
        if arr[0] < arr[1]:
            minimum = arr[0]
            maximum = arr[1]
        else:
            minimum = arr[1]
            maximum = arr[0]
        start = 2
    else:
        minimum = maximum = arr[0]
        start = 1                            # We'll start comparing from index 1

    # Check pairs
    while start < n - 1:
        if arr[start] < arr[start + 1]:
            small = arr[start]
            large = arr[start + 1]
        else:
            small = arr[start + 1]
            large = arr[start]

        if small < minimum:
            minimum = small
        if large > maximum:
            maximum = large

        start += 2

    return minimum, maximum

# Call function and display result
min_val, max_val = find_min_max(arr)


print("Minimum element is:", min_val)
print("Maximum element is:", max_val)




''' Maximum and minimum of an array using Sorting: '''

arr = [1,2,3,4,5,6,7,8]

def find_min_max(arr):
    
    arr.sort()

    
    minimum = arr[0]

    
    maximum = arr[-1]

    
    return minimum, maximum

min_val, max_val = find_min_max(arr)

# Print the results
print("Minimum element is", min_val)
print("Maximum element is", max_val)



