n=int(input())
x,y,z=n//100,n//10%10,n%10
if x!=y and x!=z and y!=z:
    print("True")
else:
    print("False")
