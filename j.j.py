for i in range(0,6-1):
    for j in range(6-i-1):
        print(" ",end="")
    for j in range(i,-1,-1):
        print(i+1,end=" ")
    print()