# Q2. Find the mean (average) of all list elements.
l = [10, 20, 30, 40]
sum = 0
for i in l:
    sum = sum+i
avg = sum/len(l)
print(avg)