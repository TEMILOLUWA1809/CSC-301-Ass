# Dynamic array simulation
capacity = 2
array = []
values = [10, 20, 30, 40, 50]

print("Initial capacity:", capacity)

for v in values:
    if len(array) == capacity:
        capacity *= 2  # double the capacity like dynamic arrays
        print("Capacity doubled to:", capacity)

    array.append(v)

print("Final array:", array)