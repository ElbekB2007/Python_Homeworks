a=list(map(str,input("Enter the list: ").split()))
element=input("Enter the element: ")
index=int(input("Enter the index: "))

# Insert the element to the list
a.insert(index, element)

print("The list:", *a)