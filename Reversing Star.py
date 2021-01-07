a=int(input("Enter the number :"))
for i in range(a,0,-1):
    for j in range(0,a-1):
        print(end="")
    for j in range(0,i):
        print("*",end="")

    print()
