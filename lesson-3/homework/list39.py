a=list(map(str,input("Enter the list: ").split()))
num=int(input("Enter the number: "))

if num>len(a):
    print(num, "is more then element of list")
else:
    print(a[0:num])