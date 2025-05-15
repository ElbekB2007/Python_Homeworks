a=list(map(int,input("Enter the list: ").split()))

# Counting the even elements
cnt_even=0
for i in a:
    if i%2==0:
        cnt_even+=1

print("The count of even elements:", cnt_even)