import random

# Constants
HANGMAN_PICS = ['''
    +---+
         |
         |
         |
        ===''', '''
    +---+
    O   |
        |
        |
       ===''', '''
    +---+
    O   |
    |   |
        |
       ===''', '''
    +---+
    O   |
   /|   |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
   /    |
       ===''', '''
    +---+
    O   |
   /|\  |
   / \  |
       ===''']

themes = {
    "1": 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split(),
    "2": 'apple banana cherry date elderberry fig grapefruit honeydew kiwi lemon mango nectarine orange papaya quince raspberry strawberry tomato ugli fruit vanilla bean watermelon'.split(),
    "3": 'artichoke beetroot carrot daikon eggplant fennel garlic horseradish iceberg lettuce jicama kale leek mushroom onion potato quinoa radish spinach turnip zucchini'.split(),
    "4": 'afghanistan brazil canada denmark ethiopia france germany hungary india japan kenya lebanon mexico netherlands oman poland qatar russia singapore thailand uruguay vietnam wales'.split(),
    "5": 'mercury venus earth mars jupiter saturn uranus neptune pluto ceres eris haumea makemake'.split()
}

# Difficulty levels and corresponding points
DIFFICULTY_POINTS = {'easy': 1, 'medium': 2, 'hard': 3}

def getRandomWord(wordList, difficulty):
    """
    Returns a random string from the passed list of strings based on difficulty level.
    """
    if difficulty == 'easy':
        wordList = [word for word in wordList if len(word) <= 4]
    elif difficulty == 'medium':
        wordList = [word for word in wordList if 4 < len(word) <= 6]
    elif difficulty == 'hard':
        wordList = [word for word in wordList if len(word) > 6]

    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]

def calculatePoints(word, missedLetters, correctLetters, attempts):
    """
    Calculates the score based on word length, missed letters, correct letters, and attempts made.
    """
    word_length = len(word)
    missed_penalty = len(missedLetters)
    correct_bonus = len(correctLetters)
    attempt_penalty = attempts
    return (word_length * DIFFICULTY_POINTS['medium']) - (missed_penalty + attempt_penalty) + correct_bonus

def displayBoard(missedLetters, correctLetters, secretWord):
    print()
    print(HANGMAN_PICS[len(missedLetters)])

    print()
    print('Missed letters: ', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')

    print()
    blanks = '_' * len(secretWord)
    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]
    # Display the secret word with spaces between the letters:
    for letter in blanks:
        print(letter, end =' ')
    print()

def getGuess(alreadyGuessed):
    """
    Returns the letter the player entered.
    Ensures the player enters a single letter and nothing else.
    """
    while True:
        print('Please guess a letter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Only a single letter is allowed.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a letter from the alphabet.')
        else:
            return guess

def selectDifficulty():
    """
    Returns the selected difficulty level.
    """
    while True:
        print("Choose difficulty level:")
        print("1. Easy")
        print("2. Medium")
        print("3. Hard")
        difficulty_choice = input("Enter the number corresponding to your difficulty choice: ")

        if difficulty_choice in DIFFICULTY_POINTS:
            return difficulty_choice
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

def playAgain():
    """
    Returns True if the player wants to play again, False otherwise.
    """
    print('Would you like to play again? (y)es or (n)o')
    return input().lower().startswith('y')

print('|H_A_N_G_M_A_N|')

# Choose theme
while True:
    print("Choose a theme:")
    print("1. Animals")
    print("2. Fruits")
    print("3. Vegetables")
    print("4. Countries")
    print("5. Planets")
    theme_choice = input("Enter the number corresponding to your theme choice: ")

    if theme_choice in themes:
        words = themes[theme_choice]
        difficulty = selectDifficulty()
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")

# Count the number of words
number_of_words = len(words)
print("Total number of words:", number_of_words)

# Now for the game itself:
while True:
    missedLetters = ''
    correctLetters = ''
    secretWord = getRandomWord(words, difficulty)
    attempts = 0

    while True:
        displayBoard(missedLetters, correctLetters, secretWord)
        # Let the player enter a letter:
        guess = getGuess(missedLetters + correctLetters)

        if guess in secretWord:
            correctLetters = correctLetters + guess
            # Check to see if the player has won:
            foundAllLetters = all(letter in correctLetters for letter in secretWord)
            if foundAllLetters:
                print('You guessed it!')
                print('The secret word is "' + secretWord + '"! You win!')
                score = calculatePoints(secretWord, missedLetters, correctLetters, attempts)
                print('Your score is:', score)
                break
        else:
            missedLetters = missedLetters + guess

            # Check if the player has guessed too many times and lost.
            if len(missedLetters) == len(HANGMAN_PICS) - 1:
                displayBoard(missedLetters, correctLetters, secretWord)
                print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' + str(len(correctLetters)) + '
