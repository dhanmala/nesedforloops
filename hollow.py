a=int(input("enter the number"))
for i in range(a):
    for j in range(a):
        if i+j==2 or i-j==2 or j-i==2 or i+j==6:
            print("*",end=" ")
        else:
            print("",end=" ")
    print()