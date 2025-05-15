a=list(map(str,input("Enter the list: ").split()))

l=len(a)
if l%2==1:
    print("The middle element:", a[l//2])
else:
    print("The 2 middle element:", a[l//2-1], a[l//2])