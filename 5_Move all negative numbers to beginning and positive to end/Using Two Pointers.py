arr = [-12, 11, -13, -5, 6, -7, 5, -3, -6]

def sort_arr(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        if arr[left] < 0:
            left = left + 1
        elif arr[right] > 0:
            right = right - 1
        else:
            arr[left], arr[right] = arr[right], arr[left]
            left = left + 1
            right = right -1
    return arr

n = sort_arr(arr)
print(n)
