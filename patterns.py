n = int(input("enter the number of maximum starts required:"))
def pat1(n):
    print('Pattern 1:')
    for i in range (1,n+1):
        print ('*'*i)
pat1(n)

def pat2(n):
    print('Pattern 2:')
    for x in range(1,n+1):
        c = n-x
        print (' '*c + '*'*x)
pat2(n)

def pat3(n):
    print('Pattern 3:')
    for z in range(1,n+1):
        c = n-z
        print (' '*c + '*'*z+' '+ '*'*z)
pat3(n)    

def pat4(n):
    print('Pattern 4:')
    r = n
    for i in range (n):
        print ('*'*r)
        r = r-1
pat4(n)

def pat5(n):
    print('Pattern 5:')
    v = n
    for i in range (n):
        print (' '*i+'*'*v)
        v = v-1
pat5(n)

