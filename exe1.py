def stack1(eum):
    kiss=0
    stack2(eum,kiss)
def stack2(eum,kiss):
    try:
     k=eum/kiss
     print(k)
    except ZeroDivisionError as msg:
     print(msg)
if __name__ == '__main__':
    eum=9
    stack1(eum)
    print('Program continuous')


