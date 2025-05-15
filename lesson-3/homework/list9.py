a=list(map(str,input("Enter the list: ").split()))

# Creating the new reversed list
newl=a[::-1]

print("New reversed list:", *newl)