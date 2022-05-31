a=int(input("enter the number"))
for i in range(a):
    for j in range(a-i-1):
        print(" ",end=" ")
    for j in range(i+1):
        print(j+1,end=" ") 
    print()       