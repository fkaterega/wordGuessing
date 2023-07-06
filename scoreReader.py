import csv

file = open('highscore', 'r')
#data = file.readlines()

csvFile = csv.reader(file)

# for lines in csvFile:
#     print(lines)
print(list(csvFile))
file.close()

