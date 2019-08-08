x= int(input("enter the first number:"))
y= int(input("enter the second number :"))
if x > y:  
   greater = x  
else:  
   greater = y  
while(True):
    if((greater % x == 0) and (greater % y == 0)):  
        lcm = greater  
        break  
    greater =  greater + 1
 
print ("Lcm of given numbers is", lcm)