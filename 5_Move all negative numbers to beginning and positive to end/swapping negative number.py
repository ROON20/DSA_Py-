arr = [-12, 11, -13, -5, 6, -7, 5, -3, -6]

def sort_arr(arr):
    j = 0

    for i in range(len(arr)):
        if arr[i] < 0:
            arr[i], arr[j] = arr[j], arr[i]
            j = j + 1
    return arr

n = sort_arr(arr)

print(n)
