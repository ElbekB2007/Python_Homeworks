main_list=list(map(str,input("Enter the list: ").split()))
num=input("Enter the element: ")

for i in range (len(main_list)):
    if main_list[i]==num:
        print(i,end=" ")