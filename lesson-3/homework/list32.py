first_list=list(map(str,input("Enter the first_list: ").split()))
second_list=list(map(str,input("Enter the second list: ").split()))

main_list=first_list+second_list
main_list.sort()

print(*main_list)