a=int(input("enter number"))
for i in range(a):
    for j in range(a-i-1):
        print(" ",end="")
    for j in range(i,-1,-1):
        print(i+1,end="")
    print()       