try:
    x=int(input("The first number is:"))
    y=int(input("The second number is :"))
    print("The result is:",x/y)
except ZeroDivisionError:
    print("Error caused by Arithmetic")
except ArithmeticError:
    print("The exception type")
