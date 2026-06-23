a = "1652637368739827"


digits = 0
for i in a:
    
    if ord(i) >= 48 and ord(i) <= 90:
        digits += 1
    else:
        spchar = spchar + 1

print(f" digits - {digits}")