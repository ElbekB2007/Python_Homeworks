from random import*

pc=0
hm=0
mylist=["rock","scissors","paper"]

while max(pc,hm)!=5:
    s=choice(mylist)
    n=input("Enter the choice: ")
    print("Computer choice:", s)

    if (n=="rock" and s=="paper") or (n=="scissors" and s=="rock") or (n=="paper" and s=="scissors"):
        pc+=1
        print("Computer score +1!")
    elif (n=="rock" and s=="scissors") or (n=="scissors" and s=="paper") or (n=="paper" and s=="rock"):
        hm+=1
        print("Human score +1!")
    else:
        print("Both did not geet points!")
    
    if pc==5:
        print("The computer win!")
    elif hm==5:
        print("The human win!")
