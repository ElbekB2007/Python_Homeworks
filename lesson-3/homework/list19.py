a=list(map(str,input("Enter the list: ").split()))

# Replacing the elements
a[0],a[1]=a[1],a[0]

print(*a)