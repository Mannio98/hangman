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

#Displays above hangman banner when user opens game
print(hangman_banner)

#List of potential words for user to guess from
words = ["mango", "frolic", "turtle", "whisker", "puzzle", "guitar", "rabbit", "zebra", "orange", 
        "sunset", "banana", "drive", "candle", "rocket", "laptop", "orchid", "party", "jungle", "plaque", "fizzle"]

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

#This function picks a random word to be guessed by the user
def choose_word():
    return random.choice(words)


#This function takes the user guesses and either displays a correct letter or an undercore
def display_word(word, guesses):
    display = ""
    for letter in word:
        if letter in guesses:
            display += letter
        else:
            display += "_"
    return display


"""
This function sets the maximum amount of guesses,
uses the choose_word function to choose a random word and
stores the users guessed letters
"""
def play_hangman():
    max_attempts = 6
    word_to_guess = choose_word()
    guesses = []
    word_guessed = False

    print("Welcome to Hangman!")
    
    initial_hangman = (
        """
        ___________
        |/        |
        |         
        |        
        |         
        |        
        |
        
        """
    )
    print(initial_hangman)
    
    #This starts a loop that continues until the user runs out of guesses and displays the word with guessed letters and underscores
    while max_attempts > 0:
        current_display = display_word(word_to_guess, guesses)
        print(current_display)

        #Prompts the user to enter a guess
        guess = input("Guess a letter: ").lower()

        #Checks if a guess if valid
        if len(guess) != 1 or not guess.isalpha() or guess not in 'abcdefghijklmnopqrstuvwxyz':
            print("Invalid input. Please enter a lowercase letter.")
            continue

        if guess in guesses:
            print("You've already guessed that letter. Please guess again.")
            continue

        #Adds guess to list of guesses
        guesses.append(guess)

        if guess in word_to_guess:
            print("Good guess!")
        else:
            print("Incorrect guess.")
            max_attempts -= 1
            # Display the hangman figure for the current number of incorrect guesses
            print(hangman_figures[6 - max_attempts])


        if display_word(word_to_guess, guesses) == word_to_guess:
            print("Congratulations, you've saved hangman's life")
            break

    if max_attempts == 0:
        print("Sorry, you've run out of attempts. Hangman is no more. The word was:", word_to_guess)

"""
This allows the user to play multiple games
if they choose not to it displays a goodbye message
"""
while True:
    play_hangman()

    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again != 'y':
        print("Thanks for playing! Goodbye.")
        break

