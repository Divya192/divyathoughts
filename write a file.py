#with open('write file','r') as file:
     #var = file.readlines()

print('statement-1')

try:
     print(10 / 0)
     print('Nil')
except (ZeroDivisionError):
     print(10/2)
