a=input("Enter the username: ").strip()
b=input("Enter the password: ").strip()

if not a and not b:
    print("Both of them empty")
elif not a:
    print("username is empty")
elif not b:
    print("password is empty")
else:
    print("Both of them not empty")
