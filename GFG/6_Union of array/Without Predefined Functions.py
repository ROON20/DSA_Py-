aa = input("Enter elements of first array (space-separated): ")
bb = input("Enter elements of second array (space-separated): ")

a = []                      # empty list
num = ""                    # Temporary string
for ch in aa + " ":         # Add extra space oon last number
    if ch != " ":
        num = num + ch
    else:
        if num != "":
            a.append(int(num))
            num = ""


b = []
num = ""
for ch in bb + " ":
    if ch != " ":
        num += ch
    else:
        if num != "":
            b.append(int(num))
            num = ""

union = []


for item in a:
    if item not in union:
        union.append(item)

for item in b:
    if item not in union:
        union.append(item)

for i in range(len(union)):
    for j in range(i + 1, len(union)):
        if union[i] > union[j]:
            union[i], union[j] = union[j], union[i]


print("Union of array:", union)
