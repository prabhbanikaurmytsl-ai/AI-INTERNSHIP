# Q4. Find the second greatest element.


l = [4, 8, 2, 9, 1]

largest = l[0]
seclargest = l[0]

for i in range(len(l)):
    if l[i] > largest:
        seclargest = largest
        largest = l[i]
    elif l[i] > seclargest and l[i] != largest:
        seclargest = l[i]

print("Second Largest:", seclargest)
    