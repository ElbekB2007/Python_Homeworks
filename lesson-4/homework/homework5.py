def check_upp(x):
    upplist="QWERTYUIOPASDFGHJKLZXCVBNM"
    for i in range(26):
        if upplist[i] in x:
            return True
    return False

n=input("Enter the password: ")

if len(n)<8:
    print("Password is too short.")
elif not check_upp(n):
    print("Password must contain an uppercase letter.")
else:
    print("Password is strong.")