#x=-1
#if(x>2):
    #raise Exception("Number shouldn't be zero")

# initialize the amount variable
#marks=10000

# perform division with 0
#a=marks/0
#print(a)

#a=[1,2,3]
#t0ry:
    #print ("second number="%(a[1]))
    #print ("Fourth number="%(a[4]))
#except IndexError:
    #print(" An error occured")


try:
    a=3
    if(a<4):
      b=a/(a-3)
      print("value of b=",b)
except(ZeroDivisionError,NameError):
    print("Error occured and handled")
