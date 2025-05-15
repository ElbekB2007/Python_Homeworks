a=list(map(str,input("Enter the list: ").split()))

b=a.copy()
b.sort()

print(a==b)