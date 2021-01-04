with open('geek','r') as reader:
    content=reader.readline()
    reversed(content)
    with open('geek','w') as writer:
        for line in reversed(content):
         writer.write(line)