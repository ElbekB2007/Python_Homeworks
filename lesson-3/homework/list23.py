num_list=list(map(int,input("Enter the list: ").split()))

for i in num_list:
    if i%2==0:
        num_list.remove(i)

print(*num_list)