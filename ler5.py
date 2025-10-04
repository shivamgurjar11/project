'''n = int(input("enter a number: "))

for i in range(1,11):
    print(f"{n}*{11-i}={n*(11-i)}")'''


n = int(input("enter a number: "))

table = []

for i in range(2, 11):
    table.append(f"{n}*{i}={n*i}")

for row in reversed(table):
    print(row)
