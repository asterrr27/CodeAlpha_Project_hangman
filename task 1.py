import random

def hangman():
    # List of words to choose from
    words = [
        'PYTHON', 'JAVA', 'HANGMAN', 'PROGRAMMING', 'ALGORITHM', 'COMPUTER',
        'NETWORK', 'CYBERSECURITY', 'ENCRYPTION', 'DECRYPT', 'INTERNET', 'SOFTWARE',
        'HARDWARE', 'DATABASE', 'SYSTEMS', 'APPLICATION', 'DEBUGGING', 'FUNCTION',
        'VARIABLE', 'CONDITION', 'LOOPING', 'JAVA_SCRIPT', 'HTML', 'CSS', 'REACT',
        'ANGULAR', 'FLASK', 'DJANGO', 'TENSORFLOW', 'PYTORCH', 'MACHINE_LEARNING',
        'ARTIFICIAL_INTELLIGENCE', 'STATISTICS', 'MATHEMATICS', 'GRAPHICS', 'DESIGN',
        'ENGINEERING', 'SCIENCE', 'RESEARCH', 'INNOVATION', 'TECHNOLOGY', 'DEVELOPMENT'
    ]
    # Randomly select a word from the list
    word = random.choice(words)
    guessed = set()  # Set to store guessed letters
    tries = 6  # Number of tries the player has

    print("Welcome to Hangman!")

    # Game loop
    while tries > 0:
        # Display the current state of the word
        display = ' '.join([c if c in guessed else '_' for c in word])
        print(f"\nCurrent word: {display}")
        print(f"Tries left: {tries}")
        
        # Get a guess from the player
        guess = input("Guess a letter: ").upper()
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        # Check if the letter has already been guessed
        if guess in guessed:
            print("You already guessed that letter. Try another.")
        else:
            guessed.add(guess)  # Add the letter to the set of guessed letters
            if guess in word:
                print(f"Good guess! The letter {guess} is in the word.")
            else:
                tries -= 1  # Decrement the number of tries if the guess is incorrect
                print(f"Incorrect! The letter {guess} is not in the word.")

        # Check if the player has guessed all the letters
        if all(c in guessed for c in word):
            print(f"\nCongratulations! You guessed the word: {word}")
            break
    else:
        # If the player runs out of tries, display the correct word
        print(f"\nGame over! You've run out of tries. The word was: {word}")

# Entry point of the program
if __name__ == "__main__":
    hangman()


