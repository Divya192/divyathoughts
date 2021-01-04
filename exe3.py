try:
   x= int(input("Enter the 1st number:"))
   y= int(input("Enter the second number:"))
   print("The result is ",x/y)

except ZeroDivisionError:
   print(" Cannot divide by zero")

except:
   print(" Cannot divide by int")