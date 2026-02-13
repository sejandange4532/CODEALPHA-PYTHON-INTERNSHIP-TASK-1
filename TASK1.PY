import random

print("Welcome to Hangman!")

words = ["apple", "banana", "tiger", "chair", "robot"]
word = random.choice(words)

display = []
for letter in word:
    display.append("_")

attempts = 6

while attempts > 0:
    print("\nWord:", " ".join(display))
    guess = input("Guess a letter: ")

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess
    else:
        attempts -= 1
        print("Wrong! Attempts left:", attempts)

    if "_" not in display:
        print("\nYou Win! Word was:", word)
        break

if attempts == 0:
    print("\nGame Over! Word was:", word)
