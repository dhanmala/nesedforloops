a=int(input("enter number"))
for i in range(a,0,-1):
    for j in range(i,5,1):
        print(" ",end="")
    for j in range(0,i,1):
        print("*",end="")    
    print()    