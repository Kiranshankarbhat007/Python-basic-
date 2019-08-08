# s = int(input("enter the starting number:"))
# e = int(input("enter the end number :"))
# l = []

# for i in range (s,e+1):
#     l.append(i)

# # print l

# for x in range (2,e+1):
#     for y in xrange (2,e):
#         # for x in xrange(e-1):
#             if x%y == 0:
#                 l.remove(x)

# print l
        
n = int(input("Enter a range for Prime Numbers : "))
l = []
for i in range(2,n+1):
    l.append(i)
# print l

for x in l :
    for y in l :
        if y%x==0 and y!=x:
            # if y!=x:
            l.remove(y)

print l

