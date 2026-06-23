correct_password = "Python123"
attempts = 3

while attempts > 0:
    password = input("Enter password: ")

    if password == correct_password:
        print("Access Granted!")
        break
    else:
        attempts -= 1
        print("Incorrect password.")
        print("Attempts left:", attempts)

if attempts == 0:
    print("Account Locked!")