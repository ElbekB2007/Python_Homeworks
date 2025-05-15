main_list=list(map(str,input("Enter the list: ").split()))
r,l=map(int,input("Enter the sublist index: ").split())

print(max(main_list[r:l+1]))