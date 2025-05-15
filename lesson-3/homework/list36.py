main_list=list(map(int,input("Enter the list: ").split()))

sum=0
for i in main_list:
    if i>0:
        sum+=i

print(sum)