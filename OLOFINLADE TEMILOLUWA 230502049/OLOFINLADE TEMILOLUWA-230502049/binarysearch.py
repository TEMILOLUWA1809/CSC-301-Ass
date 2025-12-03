arr = [1, 3, 5, 7, 9, 11, 13]
target = 9

low = 0
high = len(arr) - 1

while low <= high:
    mid = (low + high) // 2
    print(f"Checking middle index {mid}, value {arr[mid]}")

    if arr[mid] == target:
        print("Binary Search: Found at index", mid)
        break
    elif arr[mid] < target:
        low = mid + 1
    else:
        high = mid - 1