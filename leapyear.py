year = int(input("Please Enter the Year : "))
if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("{0} is a leap year".format(year))
       else:
           print("{0} is not a leap year".format(year))
   else:
       print("{0} is a leap year".format(year))
else:
   print("{0} is not a leap year".format(year))
<<<<<<< HEAD




=======
>>>>>>> b34f4a4e4ad52a8ae0964d8c332c862a1bce2b40
