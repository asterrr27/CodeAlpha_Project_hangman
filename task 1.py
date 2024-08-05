import random

def hangman():
    words = [
        'PYTHON', 'JAVA', 'HANGMAN', 'PROGRAMMING', 'ALGORITHM', 'COMPUTER',
        'NETWORK', 'CYBERSECURITY', 'ENCRYPTION', 'DECRYPT', 'INTERNET', 'SOFTWARE',
        'HARDWARE', 'DATABASE', 'SYSTEMS', 'APPLICATION', 'DEBUGGING', 'FUNCTION',
        'VARIABLE', 'CONDITION', 'LOOPING', 'JAVA_SCRIPT', 'HTML', 'CSS', 'REACT',
        'ANGULAR', 'FLASK', 'DJANGO', 'TENSORFLOW', 'PYTORCH', 'MACHINE_LEARNING',
        'ARTIFICIAL_INTELLIGENCE', 'STATISTICS', 'MATHEMATICS', 'GRAPHICS', 'DESIGN',
        'ENGINEERING', 'SCIENCE', 'RESEARCH', 'INNOVATION', 'TECHNOLOGY', 'DEVELOPMENT'
    ]
    word = random.choice(words)
    guessed = set()
    tries = 6

    print("Welcome to Hangman!")

    while tries > 0:
        display = ' '.join([c if c in guessed else '_' for c in word])
        print(f"\nCurrent word: {display}")
        print(f"Tries left: {tries}")
        
        guess = input("Guess a letter: ").upper()
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed:
            print("You already guessed that letter. Try another.")
        else:
            guessed.add(guess)
            if guess in word:
                print(f"Good guess! The letter {guess} is in the word.")
            else:
                tries -= 1
                print(f"Incorrect! The letter {guess} is not in the word.")

        if all(c in guessed for c in word):
            print(f"\nCongratulations! You guessed the word: {word}")
            break
    else:
        print(f"\nGame over! You've run out of tries. The word was: {word}")

if __name__ == "__main__":
    hangman()

