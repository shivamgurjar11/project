'''n=int(input("enter a number: "))

for i in range (1,n+1):
    print(" "* (n-i), end="")
    print("*"*(2*i-1), end="")
    print("")

n=int(input("enter a number: "))

for i in range (1,n+1):
    print("*"* i, end="")
    
    print("")'''

n=int(input("enter a number: "))

for i in range (1,n+1):
    if(i==1 or i==n):
        print("*"* n, end="")

    else:
        print("*",end="")
        print(" "* (n-2),end="")
        print("*",end="")

    print("")