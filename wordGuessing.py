import random


words = ["process", "thread", "forks", "signal"]

random_word = words[random.randint(0, len(words) - 1)]
#random_word = "process"
# print(random_word)

chances = 2
truth_tracker = False
winning_tracker = False

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
if winning_tracker:
   print("You win!")
else:
    print("You lose!")

