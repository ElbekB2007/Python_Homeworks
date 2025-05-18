from random import*
tlist=["Y","YES","y","yes","ok"]
x=randint(1,100)
attepmts=0

while(True):
    n=int(input("Enter the number: "))
    attepmts+=1
    if(n > x):
        print("Too high!")
    elif n==x:
        print("You guessed it right!")
        break
    else:
        print("Too low!")

    if attepmts==10:
        print("You lost. Want to play again?")
        t=input()
        if t in tlist:
            attepmts=0
            x=randint(1,100)
            continue
        else:
            break
        