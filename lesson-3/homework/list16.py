a=list(map(int,input("Enter the list: ").split()))

# Counting the odd elements
cnt_odd=0
for i in a:
    if i%2==1:
        cnt_odd+=1

print("The count of odd elements:", cnt_odd)