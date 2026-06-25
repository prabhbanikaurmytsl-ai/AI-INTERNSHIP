# Task 5: Execute safe deletion commands to drop the Age attribute
# out of the dictionary.
d = {
    "name": "Shagun",
    "age": 20,
    "college": "LPU"
}

d.pop("age")

print(d)