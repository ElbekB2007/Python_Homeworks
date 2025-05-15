l,r=map(int,input("Enter the range: ").split())

main_list=[]
for i in range(l,r+1):
    main_list.append(i)

print(*main_list)