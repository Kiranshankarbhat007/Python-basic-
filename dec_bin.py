l =[]
n = int(input("enter the decimal number :"))
s = n
while s >0:
    reminder = s%2
    l.append(reminder)
    qu =int(s/2)
    s = qu
print l[::-1]




