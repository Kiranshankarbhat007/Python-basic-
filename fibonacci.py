n = int(input("enter the number:"))
a = 0
b = 1
for i in range (2,n):
	# a = [i]
	# b = [i+1]
	c = a + b 
	a = b
	b = c
print (c)

# n = int(input("enter the number:"))
# def fibonacci(n): 
#     a = 0
#     b = 1
#     if n < 0: 
#         print("Incorrect input") 
#     elif n == 0: 
#         return a 
#     elif n == 1: 
#         return b 
#     else: 
#         for i in range(2,n): 
#             c = a + b 
#             a = b 
#             b = c 
#         return b 
# print(fibonacci(n)) 


# def Fibonacci(n): 
#     if n<0: 
#         print("Incorrect input")
#     elif n==1: 
#         return 0 
#     elif n==2: 
#         return 1
#     else: 
#         return Fibonacci(n-1)+Fibonacci(n-2) 

# x = int(input("enter the number :"))
# print(Fibonacci(x)) 
