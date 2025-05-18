list1=list(map(str,input("Enter the first list: ").split()))
list2=list(map(str,input("Enter the second list: ").split()))

new_list=list()
for i in list1:
    if not i in list2:
        new_list.append(i)

for i in list2:
    if not i in list1:
        new_list.append(i)

print(*new_list)