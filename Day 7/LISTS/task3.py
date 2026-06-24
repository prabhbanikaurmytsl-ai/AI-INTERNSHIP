# Q3. Find the greatest element and print its index.
l = [4, 8, 2, 9, 1]
largest = l[0];
index = 0
for i in range(len(l)):
    if l[i]>largest:
        largest = l[i]
        index = i
print("Largest value is ", largest, "and its index is", index )

         
