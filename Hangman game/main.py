import random


def draw_hangman(attempts_left):
    stages = [
        """ 
           -----
           |   |
           |   O
           |  /|\\
           |  / \\
           |
        """,
        """ 
           -----
           |   |
           |   O
           |  /|\\
           |  / 
           |
        """,
        """ 
           -----
           |   |
           |   O
           |  /|\\
           |  
           |
        """,
        """ 
           -----
           |   |
           |   O
           |  /|
           |  
           |
        """,
        """ 
           -----
           |   |
           |   O
           |   |
           |  
           |
        """,
        """ 
           -----
           |   |
           |   O
           |  
           |  
           |
        """,
        """ 
           -----
           |   |
           |   
           |  
           |  
           |
        """
    ]
    print(stages[attempts_left])


def hangman():
    words = ['python', 'java', 'ruby', 'html', 'css', 'flask', 'django', 'react']
    word = random.choice(words)
    attempts = 6
    guessed_letters = []
    length = len(word)
    center_index = length // 2
    hint = " ".join("_" * center_index + word[center_index] + "_" * (length - center_index - 1))

    print("\nHint: The word looks like this →", hint)

    while attempts > 0:
        display_word = " ".join(letter if letter in guessed_letters else "_" for letter in word)
        print("\nWord to guess:", display_word)
        draw_hangman(attempts)

        if display_word.replace(" ", "") == word:
            print("\nYou won! The word was:", word)
            break

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print(f"Good job! '{guess}' is in the word.")
        else:
            attempts -= 1
            print(f"Wrong letter '{guess}'! You have {attempts} attempts left.")

        if attempts == 0:
            draw_hangman(attempts)
            print("\nGame Over! The word was:", word)


user_name = input("Enter your name: ")
print(f"\nHello, {user_name}!")
print("\nWelcome to Hangman! Try to guess the word.")
hangman()
