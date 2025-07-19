arr = [1, 4, 3, 2, 6, 5]

def reverse_array(arr):
    arr.reverse()     # Reverses the list in-place
    return arr        # Optional return, since arr is modified directly

reverse_array(arr)

print(arr)            # Prints the reversed array
