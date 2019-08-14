n = 5
for x in range (1,n+1):
    z = 1
    for y in range (1,x+1):
        print (z, end='')
        z = int(z * (x-y) /y)
    print (" ")

