first_list=list(map(str,input("Enter the list: ").split()))
second_list=list(map(str,input("Enter the list: ").split()))

# Combining the lists
third_list=first_list+second_list

print("Combined list:", *third_list)