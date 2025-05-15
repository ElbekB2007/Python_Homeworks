a=list(map(str,input("Enter the list: ").split()))

# Creating the new unique list
unique_list=set(a)

print("New unique list:", *unique_list)