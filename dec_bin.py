l =[]
<<<<<<< HEAD
=======
d =[]
>>>>>>> b34f4a4e4ad52a8ae0964d8c332c862a1bce2b40
n = int(input("enter the decimal number :"))
s = n
while s >0:
    reminder = s%2
    l.append(reminder)
    qu =int(s/2)
    s = qu
print l[::-1]




