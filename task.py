import random
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', r'''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(chosen_word)
display_word = ["_"] * len(chosen_word)
error = 6
print("".join(display_word))
while "_" in display_word and error >= 0:
    guess = input("\nGuess a letter: ").lower()
    if guess in chosen_word:
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                display_word[i] = guess
    else:
        print(stages[error])
        error -= 1
        print(f"Wrong guess. You have {error + 1} lives left.")
    print("".join(display_word))
    if error < 0:
        print("Game Over. The word was:", chosen_word)
        break
if "_" not in display_word:
    print("You Won!")
