import random

hangman_banner = """
  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                     __/ |                      
                    |___/                       
"""

print(hangman_banner)

words = ["Mango", "Frolic", "Turtle", "Whisker", "Puzzle", "Guitar", "Rabbit", "Zebra", "Orange", 
        "Sunset", "Banana", "Drive", "Candle", "Rocket", "Laptop", "Orchid", "Party", "Jungle", "Plaque", "Fizzle"]

hangman_figures = [
        """
        ___________
        |/        |
        |         
        |        
        |         
        |        
        |
        
        """,
        """
        ___________
        |/        |
        |         O
        |        
        |         
        |        
        |
        
        """,
        """
        ___________
        |/        |
        |         O
        |         |
        |         |
        |        
        |
        
        """,
        """
        ___________
        |/        |
        |         O
        |        /|
        |         |
        |
        | 
        """,
        """
        __________
        |/        |
        |         O
        |        /|\\
        |         |
        |
        |
        """,
        """
        __________
        |/        |
        |         O
        |        /|\\
        |         |
        |        /
        |
        """,
        """
        __________
        |/        |
        |         O
        |        /|\\
        |         |
        |        / \\
        |
        """
]

def choose_word():
    return random.choice(words)

def display_word(word, guesses):
    display = ""
    for letter in word:
        if letter in guesses:
            display += letter
        else:
            display += "_"
    return display



def play_hangman():
    max_attempts = 6
    word_to_guess = choose_word()
    guesses = []

    print("Welcome to Hangman!")

    while max_attempts > 0:
        current_display = display_word(word_to_guess, guesses)
        print(current_display)

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha() or guess not in 'abcdefghijklmnopqrstuvwxyz':
            print("Invalid input. Please enter a lowercase letter.")
            continue

        if guess in guesses:
            print("You've already guessed that letter. Please guess again.")
            continue

        guesses.append(guess)

        if guess in word_to_guess:
            print("Good guess!")
        else:
            print("Incorrect guess.")
            max_attempts -= 1
            print(hangman_figures[6 - max_attempts])


        if current_display == word_to_guess:
            print("Congratulations, you've saved hangman's life")
            break

    if max_attempts == 0:
        print("Sorry, you've run out of attempts. Hangman is no more. The word was:", word_to_guess)

while True:
    play_hangman()

    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again != 'y':
        print("Thanks for playing! Goodbye.")
        break

