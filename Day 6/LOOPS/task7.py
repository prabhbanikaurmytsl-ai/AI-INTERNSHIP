
largest = int(input("Enter number 1: "))

for i in range(2, 6):
    num = int(input(f"Enter number {i}: "))
    
    if num > largest:
        largest = num

print("Largest number is:", largest)