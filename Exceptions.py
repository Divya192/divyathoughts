#ItemsInCart=0
#if(ItemsInCart!=2): #raise Exception("The product count doesn't match")
    #pass

#assert(ItemsInCart==2)

def example1():
    while True:
        try:
         x = int( input( "enter a number: " ) )
         y = int( input( "enter another number: " ) )
         print( x, '/', y, '=', x/y )
         break
        except(ZeroDivisionError):
           print ("Can't divide by 0!")
        except(ValueError):
           print ("That doesn't look like a number!")
        except:
           print ("something unexpected happend!")
