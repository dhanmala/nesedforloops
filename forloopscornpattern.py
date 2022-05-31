a=int(input("enter the number"))
for i in range(a):
    for j in range(a):
        if (i+j==4)or (j-i==4) or (i+j==6) or (i-j==3):
            print("*",end="")
        else:
            print(" ",end=" ")
    print()            