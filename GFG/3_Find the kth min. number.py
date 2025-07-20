arr = [5,8,3,9,2]

def kth_ele(arr):
    arr.sort()
    
    k = arr[0]
    
    if k < len(arr):
        n = arr[k - 1]
        print(f"The value of k is: {k} & the kth element is: {n}")
    else:
        print("The value of k is less then,the length of this array")

kth_ele(arr)
