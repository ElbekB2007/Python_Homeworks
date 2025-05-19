def factor(num):
    for i in range(1,num+1):
        if num % i == 0:
            print(i, "is a factor of", num)

n=int(input("Enter a positive integer: "))
factor(n)