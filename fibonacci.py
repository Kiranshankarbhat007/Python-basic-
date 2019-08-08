n = int(input("enter the number:"))
a = 0
b = 1
for i in range (1,n):
	# a = [i]
	# b = [i+1]
	c = a + b 
	a = b
	b = c

print (c)