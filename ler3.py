'''n=int(input("enter a number: "))

for i in range(2,n):
    if(n%i)==0:
       print("number is not prime")


else:
    print("the number is prime")

n=int(input("enter a number: "))

i = 0
sum=0

while(i<=n):
    sum +=i
    i +=1
    print(sum)'''

n=int(input("enter a number: "))
product = 1
for i in range(1,n+1):
    product = product*i

print(f"the factorial of {n} is {product}")
  

