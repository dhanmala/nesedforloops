n=int(input("enter the number"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if j==n or i==1 or j==i:
            print("*",end=" ")
        else:
            print(" ",end=" ")    
    print()        