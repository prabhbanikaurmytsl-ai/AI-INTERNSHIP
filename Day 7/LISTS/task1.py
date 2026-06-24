# Q1. Print the lists of all positive and negative elements
l = [3, -1, 4, -5, 9]
pos = []
neg = []
for i in l:
    if i >=0:
        pos.append(i)
    else:
        neg.append(i)
print("Poitive: ", pos)
print("Negative: ", neg)