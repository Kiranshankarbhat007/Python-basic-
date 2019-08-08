x = int(input("enter the first number:"))
y = int(input("enter the second number :"))
if x > y:
    smaller = y
else:
    smaller = x
for i in range(1, smaller+1):
    if((x % i == 0) and (y % i == 0)):
        gcd = i

print ("gcd of given number is",gcd )
