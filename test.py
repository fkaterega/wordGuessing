file = open('wordList', 'r')
item = file.readlines()[0].rstrip()
print(item)
file.close()