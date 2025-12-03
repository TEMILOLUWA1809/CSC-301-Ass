arr = [2, 5, 7,10, 14,20]
target = 2

found = False
for i in range(len(arr)):
    if arr[i] == target:
        print("Linear Search: Found at index", i)
        found = True
        break

if not found:
    print("Linear Search: Not Found")