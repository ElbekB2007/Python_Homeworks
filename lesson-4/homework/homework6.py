def prime(x):
    if x==2:
        return True
    elif x<=1 or x%2==0:
        return False
    else:
        for i in range(3,int(x**(1/2)+1),2):
            if x%i==0:
                return False
        return True

for i in range(1,100):
    if prime(i):
        print(i)