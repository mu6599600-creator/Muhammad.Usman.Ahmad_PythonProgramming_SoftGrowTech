import random
# List of words
words = ["python", "engineer", "laptop", "machine", "program"]

# Select random word
word = random.choice(words)

guessed_letters = []
incorrect_guesses = 0
max_incorrect = 6

print("Welcome To Hangman Game")
print("Guess the word one letter at a time")

while incorrect_guesses < max_incorrect:

    display_word = ""

    # Create display word
    for letter in word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_"

    print("\nWord:", display_word)
    print("Incorrect guesses left:", max_incorrect - incorrect_guesses)

    # Check win condition
    if display_word == word:
        print("Congratulations! You guessed the word:", word)
        break

    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct guess!")
    else:
        print("Wrong guess!")
        incorrect_guesses += 1

else:
    print("\nGame Over! The correct word was:", word)