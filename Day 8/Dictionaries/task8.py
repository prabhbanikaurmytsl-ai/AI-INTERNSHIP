# Contact Book

contacts = {
    "Aman": "9876543210",
    "Shagun": "9123456780",
    "Rahul": "9988776655",
    "Priya": "9871234567",
    "Karan": "9012345678"
}

name = input("Enter contact name: ")

if name in contacts:
    print("Phone Number:", contacts[name])
else:
    print("Contact not found!")