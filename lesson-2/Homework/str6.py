a=input()
b=input()
if a in b or b in a:
    if a in b:
        print(a,"in",b)
    else:
        print(b,"in",a)
else:
    print("Non of this strings comtains others")
    
