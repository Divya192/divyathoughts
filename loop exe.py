f=None
try:
    f=open('geek.txt','r')
    print("Opened the file successfully")
except:
    print("Some pblm occured during opening the file")
else:
    print("The data content in the file is:")
    print('#'*4)
    print(f.read())
finally:
    if f != None:
       f.close()

