n=int(input("enter number"))
for i in range(n):
    for i in range(i):
        print(" ",end="")
    for j in range(2*(n-i)-1):
        print("*",end="")
    print()        