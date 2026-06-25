# Task 3: Modify the student dictionary to update the age value 
# dynamically.
d = {
    "name": "Shagun",
    "age": 20,
    "college": "LPU"
}
d1 = {"age":66}
d.update(d1)
print(d)