main_list=list(map(str,input("Enter the list: ").split()))
ind=int(input("Enter the index: "))

if len(main_list)>ind:
    main_list.remove(main_list[ind])

    print(*main_list)
else:
    print("This index don\'t exist!")