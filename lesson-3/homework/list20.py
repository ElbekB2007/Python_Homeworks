a=list(map(str,input("Enter the list: ").split()))

a.sort()

print("The second largest element:", a[len(a)-2])