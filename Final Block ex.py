import os

print("### Ex 1 ###")

try:
    print("trdy")
except:
    print("excepft")
finally:
    print("fibal \n")

print("### Ex2 ###")
try:
    print("nanio")
    print(10/0)
except:
    print("Exception arried")
finally:
    print("Bomb diggy \n")


print("### Ex3 ###")
try:
    print("nako")
    print(10/0)
except ZeroDivisionError:
    print("Meows")
finally:
    print("Traceback occurred")


try:
    print(10/0)

except:
    os._exit(0)
    print("excell")
finally:
    print("g")

print("state")




















































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































