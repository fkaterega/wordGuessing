f = open('./wordList', 'r')
file = f.readlines()[0].strip()
print(file)

f.close()