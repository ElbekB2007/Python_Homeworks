from math import*

def is_prime(x):
    if x == 2:
        return True
    elif x == 1 or x % 2 == 0:
        return False
    else:
        for i in range(3,int(sqrt(x))+1,2):
            if x % i == 0:
                return False
        return True

num=int(input("Enter the number: "))
print(is_prime(num))