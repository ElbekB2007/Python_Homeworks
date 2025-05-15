a=list(map(str,input("Enter the list: ").split()))

# Checking the count of elements of list
if len(a)<3:
    print("The count of elements in list less than 3!")
else:
    # Creating the new list
    newl=a[0:3]
    print("The first 3 elements of list:", *newl)