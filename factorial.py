# n = int(input("enter the number to find factorial:"))
# f = 1

# for x in range (1,n+1):
# 	f = f*x
# 	# n = n-1
# 	print f

# print (f)

# def fact(n):
# 	# n = int(input("enter the number:"))
# 	f = 1
# 	if n <0:
# 		print ("we can't find the factorial for negetive numbers")
# 	elif n == 1:
# 		print ("the factorial of 1 is 1")
# 	else:
# 		f = f*n
# 		n = n-1
# 	print ('the factorial of the given number is',f)


# n = int(input("enter the number :"))
# fact(n)

import even_or_odd 

n = int(input("enter the number to find factorial:"))

def fac(n):
	f = 1
	for z in range (1,n+1):
		f = f*n
		n = n-1
	print "the factorial of the given number is",f

fac(n)

# using recursion 

num = int(input("enter the number "))
def fact(num):
	# f = 1
	# for z in range (1,n+1):
	# while n >:
	if num == 1:
		return 1
	else:
		return (num*fact(num-1)) 

result = (fact(num))
print ("the factorial of number is",result)

