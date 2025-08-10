import random

# Predefined list of 5 words
WORDS = ['table', 'light', 'creme', 'drink', 'world']

def hangman():
    word = random.choice(WORDS)
    guessed_letters = []
    tries = 6
    word_display = ['_' for _ in word]

    print("Welcome to Hangman!")
    print("Guess the word: " + ' '.join(word_display))

    while tries > 0 and '_' in word_display:
        guess = input("Enter a letter: ").lower()
        
        # Validate input
        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single alphabetical character.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter. Try another.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            for idx, letter in enumerate(word):
                if letter == guess:
                    word_display[idx] = guess
            print("Correct! " + ' '.join(word_display))
        else:
            tries -= 1
            print(f"Incorrect! {tries} guesses left.")
            print(' '.join(word_display))

    if '_' not in word_display:
        print(f"Congratulations! You guessed the word: {word}")
    else:
        print(f"Game over! The word was: {word}")

if __name__ == "__main__":
    hangman()
