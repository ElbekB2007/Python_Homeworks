from random import*
a,b=map(int,input().split())

new_set=set()
for i in range(8):
    new_set.add(randint(a,b+1))

print(new_set)
