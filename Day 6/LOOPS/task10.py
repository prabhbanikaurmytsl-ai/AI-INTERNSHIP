currentpin = 1223
attempt = 3

while attempt>0:
    pin = int(input("Enter your pin"))

    if pin == currentpin:
        print("Access Granted")
        break
    else:
        attempt = attempt-1
        print("Try again")

if attempt == 0:
    print("Account Locked!")