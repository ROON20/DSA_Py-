# Take input from the user
aa = input("Enter elements of first array (space-separated): ")
a = list(map(int, aa.split()))

bb = input("Enter elements of second array (space-separated): ")
b = list(map(int, bb.split()))

# Define the union function
def union_of_array(a, b):
    set_a = set(a)
    set_b = set(b)
    union_of_ab = set_a | set_b
    return list(union_of_ab)

# Call the function
result = union_of_array(a, b)

# Print the result in sorted order
print("Union of array:", sorted(result))

