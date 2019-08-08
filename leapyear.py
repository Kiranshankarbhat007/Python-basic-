s = int(input("enter the year"))

def leap(s):
    if (s%4==0):
        return ("it is a leap year")
    else:
        return ("it is not a leap year")

result = leap(s)
print result