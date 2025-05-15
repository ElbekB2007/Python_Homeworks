a=list(map(str,input("Enter the list: ").split()))

# Creating the new sorted list
newl=a
newl.sort()

print("New sorted list:", *newl)