import random

words = ["jaemin", "nuclear", "uzbekistan", "shotgun"]
word = random.choice(words)

# Create a list of underscores the same length as the word
display = ["_"] * len(word)

# Create a list to store guessed letters
guessed_letters = []

# Set the number of lives
lives = 6

while "_" in display and lives > 0:
    print(" ".join(display))
    print("Lives: ", lives)
    print("Guessed letters: ", guessed_letters)
    guess = input("Guess a letter: ").lower()
    if guess in guessed_letters:
        print("You already guessed that letter. Try again.")
    elif guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess
    else:
        lives -= 1
        print("Incorrect.")
    guessed_letters.append(guess)

if "_" not in display:
    print("Congratulations! You guessed the word.")
else:
    print("Sorry, you lost. The word was", word + ".")