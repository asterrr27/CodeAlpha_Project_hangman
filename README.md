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
    
    # Select a random word from the list
    word = random.choice(words)
    guessed = set()  # Set to keep track of guessed letters
    tries = 6  # Number of tries the player has

    print("Welcome to Hangman!")  # Welcome message

    while tries > 0:
        # Display the current state of the word, with unguessed letters as underscores
        display = ' '.join([c if c in guessed else '_' for c in word])
        print(f"\nCurrent word: {display}")
        print(f"Tries left: {tries}")
        
        # Get user's guess and convert it to uppercase
        guess = input("Guess a letter: ").upper()
        # Check if the input is valid (single letter)
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        # Check if the letter was already guessed
        if guess in guessed:
            print("You already guessed that letter. Try another.")
        else:
            guessed.add(guess)  # Add the letter to the set of guessed letters
            # Check if the guessed letter is in the word
            if guess in word:
                print(f"Good guess! The letter {guess} is in the word.")
            else:
                tries -= 1  # Decrease tries if the guess was incorrect
                print(f"Incorrect! The letter {guess} is not in the word.")

        # Check if all letters in the word have been guessed
        if all(c in guessed for c in word):
            print(f"\nCongratulations! You guessed the word: {word}")
            break
    else:
        # If the player runs out of tries, reveal the word
        print(f"\nGame over! You've run out of tries. The word was: {word}")

# Run the game if this file is executed as a script
if __name__ == "__main__":
    hangman()
