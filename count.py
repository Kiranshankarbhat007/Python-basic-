s = str(input("enter the string: "))
l = list(s)
count = {}
for x in l:
    count[x] = count.get(x,0) + 1
print count 
  
