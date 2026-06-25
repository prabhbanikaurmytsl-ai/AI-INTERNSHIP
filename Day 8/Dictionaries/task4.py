# Task 4: Inject a fresh Email key entry field into the existing 
# student dictionary structure.
d = {
    "name": "Shagun",
    "age": 20,
    "college": "LPU"
}
d1 = {"email": "shagun@example.com"}
d.update(d1)

print(d)