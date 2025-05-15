a=set(map(str,input().split()))
b=set(map(str,input().split()))

if a <= b:
    print(a <= b)
elif b <= a:
    print(b <= a)
else:
    print("False")