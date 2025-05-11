n=input("Plese enter the string: ")
a='0123456789'
t="String don\'t have any digits"

for i in n:
    if i in a:
        t="String have a digits"
        break
print(t)
