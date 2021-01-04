try:
    c=5//0
    print(c)
except(ZeroDivisionError):
    print("Error occured")
finally:
    print("Anyways execution")

