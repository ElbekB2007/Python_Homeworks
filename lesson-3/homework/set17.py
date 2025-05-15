a=set(map(int,input().split()))

b=set()
for i in a:
    if i%2==1:
        b.add(i)

print(b)