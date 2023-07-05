import random

# Open a word list file

file = open('./wordList', 'r')
word = file.readlines()
file.close()

# Select a random word from a list

random_word = word[random.randint(0, len(word) - 1)].strip()
#random_word = "process"
# print(random_word)

chances = 2
truth_tracker = False
winning_tracker = False

# Score

scoreCorrect = 10
scoreIncorrect = -5
scoreCurrent = 0 

#mask = [False for char in random_word]
mask = []
for char in random_word:
     mask.append(False)
# print(mask)
# mask = []
# for char in random_word:
#      mask.append(False)

# print(mask)
# exit()

while chances != 0  and  not winning_tracker:
    print("You have {} attempts left.".format(chances))
    print(scoreCurrent)
    for index, char in enumerate(random_word):
        if mask[index]:
            print(char, end=" ")
        else:
             print("_", end="")

    user_input = input("\nGuess a character > ")

    if len(user_input) > 1 or not user_input.isalpha():
            print('You gave a bad input')
            continue

    for index, char in enumerate(random_word):
         if user_input == char:
              mask[index] = True
              truth_tracker = True
    for item in mask:
         print(item)
         if not item:
              winning_tracker = False
              break
         else:
              winning_tracker = True

    if not truth_tracker:
         chances = chances - 1
         scoreCorrect += scoreIncorrect
if winning_tracker:
   print("You win!")
else:
    print("You lose!")

