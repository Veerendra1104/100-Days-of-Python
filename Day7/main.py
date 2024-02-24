import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

end_of_game = False
wordlist = ["darshan","sudeep","punith","yash"]
chosen_word = random.choice(wordlist)
word_length= len(chosen_word)

lives = 6
print(f'')

display =[]
for _ in range(word_length):
    display += "_"


while not end_of_game:
    guess = input("Guess the letter : ").lower()
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f" Current position is {position} \n Current letter : {letter} \n Gussed letter : {guess} \n")
        if letter==guess:
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
        if lives==0:
            end_of_game = True
            print("You loose.")


    print(f"{' '.join(display)}")
    if "_" not in display:
        end_of_game = True
        print("You Win !!!!")

    print(stages[lives])









