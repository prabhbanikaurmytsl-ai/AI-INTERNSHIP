import os
from pathlib import Path

def create_file():
    try:
        name = input("Enter the name of the file to create: ")
        path = Path(name)
        if not path.exists():
            with open(path, 'w') as f:
                data = input("Enter the content to write to the file: ")
                f.write(data)  # Create an empty file
                print(f"File '{name}' created successfully.")
        else:
            print(f"File '{name}' already exists.")
    except Exception as e:
        print(f"An error occurred while creating the file: {e}")

def read_file():
    try:
        name = input("Enter the name of the file to read: ")
        path = Path(name)
        if path.exists():
            with open(path, 'r') as f:
                content = f.read()
                print(f"Content of '{name}':\n{content}")
        else:
            print(f"File '{name}' does not exist.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")

def update_file():
    try:
        name = input("Enter the name of the file to update: ")
        path = Path(name)
        if path.exists():
            print("operations")
            print("1. Append to the file")
            print("2. Overwrite the file")
            print("3. Rename the file")

            choice = int(input("Enter your choice: "))
            if choice == 1:
                with open(path, 'a') as f:
                    data = input("Enter the content to append to the file: ")
                    f.write(data)
                    print(f"Content appended to '{name}' successfully.")
            elif choice == 2:
                with open(path, 'w') as f:
                    data = input("Enter the new content for the file: ")
                    f.write(data)
                    print(f"File '{name}' updated successfully.")
            elif choice == 3:
                new_name = input("Enter the new name for the file: ")
                new_path = Path(new_name)
                if not new_path.exists():
                    os.rename(path, new_path)
                    print(f"File '{name}' renamed to '{new_name}' successfully.")
                else:
                    print(f"File '{new_name}' already exists.")
        else:
            print(f"File '{name}' does not exist.")
    except Exception as e:
        print(f"An error occurred while updating the file: {e}")

def delete_file():
    try:
        name = input("Enter the name of the file to delete: ")
        path = Path(name)
        if path.exists():
            os.remove(path)
            print(f"File '{name}' deleted successfully.")
        else:
            print(f"File '{name}' does not exist.")
    except Exception as e:
        print(f"An error occurred while deleting the file: {e}")







print("Press 1 for creating a file")
print("Press 2 for reading a file")
print("Press 3 for updating a file")
print("Press 4 for deleting a file")


a = int(input("Enter your choice: "))

if a == 1:
    create_file()
elif a == 2:
    read_file()
elif a == 3: 
    update_file()
elif a == 4:
    delete_file()   
else:
    print("Invalid choice. Please select a valid option.")