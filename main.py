import tkinter as tk
from tkinter import messagebox
import random

# Constants
HANGMAN_PICS = [
    '''
    +---+
         |
         |
         |
        ===''',
    '''
    +---+
    O   |
        |
        |
       ===''',
    '''
    +---+
    O   |
    |   |
        |
       ===''',
    '''
    +---+
    O   |
   /|   |
        |
       ===''',
    '''
    +---+
    O   |
   /|\  |
        |
       ===''',
    '''
    +---+
    O   |
   /|\  |
   /    |
       ===''',
    '''
    +---+
    O   |
   /|\  |
   / \  |
       ==='''
]

themes = {
    "1": ('Animals', 'Ant Baboon Badger Bat Bear Beaver Camel Cat Clam Cobra Cougar Coyote Crow Deer Dog Donkey Duck Eagle Ferret Fox Frog Goat Goose Hawk Lion Lizard Llama Mole Monkey Moose Mouse Mule Newt Otter Owl Panda Parrot Pigeon Python Rabbit Ram Rat Raven Rhino Salmon Seal Shark Sheep Skunk Sloth Snake Spider Stork Swan Tiger Toad Trout Turkey Turtle Weasel Whale Wolf Wombat Zebra'),
    "2": ('Fruits', 'Apple Banana Cherry Date Elderberry Fig Grapefruit Honeydew Kiwi Lemon Mango Nectarine Orange Papaya Quince Raspberry Strawberry Tomato Ugli Fruit Vanilla Bean Watermelon'),
    "3": ('Vegetables', 'Artichoke Beetroot Carrot Daikon Eggplant Fennel Garlic Horseradish Iceberg Lettuce Jicama Kale Leek Mushroom Onion Potato Quinoa Radish Spinach Turnip Zucchini'),
    "4": ('Countries', 'Afghanistan Brazil Canada Denmark Ethiopia France Germany Hungary India Japan Kenya Lebanon Mexico Netherlands Oman Poland Qatar Russia Singapore Thailand Uruguay Vietnam Wales'),
    "5": ('Planets', 'Mercury Venus Earth Mars Jupiter Saturn Uranus Neptune Pluto Ceres Eris Haumea Makemake')
}

# Difficulty levels and corresponding points
DIFFICULTY_POINTS = {'Easy': 1, 'Medium': 2, 'Hard': 3}

class HangmanGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("THE HANGMAN GAME")
        self.master.geometry("400x400")  # Adjusted initial window size

        self.theme_choice = tk.StringVar()
        self.difficulty_choice = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Font for heading
        heading_font = ("Roboto", 24, "bold")
        # Font for other text
        other_font = ("Roboto Mono", 12)  # Reduced font size

        self.heading_label = tk.Label(self.master, text="THE HANGMAN GAME", font=heading_font)
        self.heading_label.pack(pady=10)  

        self.created_by_label = tk.Label(self.master, text="Created by Team Terabyte", font=other_font)
        self.created_by_label.pack()  
        self.created_by_label.config(font=("Roboto Mono", 8))  # Reduced font size

        self.theme_label = tk.Label(self.master, text="Choose the Theme", font=other_font)
        self.theme_label.pack()  

        theme_options = [f"{key}. {theme[0]}" for key, theme in themes.items()]
        self.theme_menu = tk.OptionMenu(self.master, self.theme_choice, *themes.keys(), command=self.update_theme_label)
        self.theme_menu.config(font=other_font)
        self.theme_menu.pack()  

        self.difficulty_label = tk.Label(self.master, text="Choose the Difficulty", font=other_font)
        self.difficulty_label.pack()  

        self.difficulty_menu = tk.OptionMenu(self.master, self.difficulty_choice, *DIFFICULTY_POINTS.keys())
        self.difficulty_menu.config(font=other_font)
        self.difficulty_menu.pack()  

        self.start_button = tk.Button(self.master, text="Start Game", font=other_font, command=self.start_game)  # Adjusted font size
        self.start_button.pack(pady=10)  

    def update_theme_label(self, value):
        selected_theme = themes.get(value)
        if selected_theme:
            self.theme_label.config(text=f"Choose the Theme: {selected_theme[0]}")

    def start_game(self):
        theme = self.theme_choice.get()
        difficulty = self.difficulty_choice.get()

        words = themes[theme][1]

        self.theme_label.destroy()
        self.theme_menu.destroy()
        self.difficulty_label.destroy()
        self.difficulty_menu.destroy()
        self.start_button.destroy()

        self.game = HangmanGame(self.master, words, difficulty)

class HangmanGame:
    def __init__(self, master, words, difficulty):
        self.master = master
        self.words = words.split()  # Split the words string into a list
        self.difficulty = difficulty
        self.score = 0  # Track the score

        self.secretWord = self.getRandomWord()  # Now calling getRandomWord method
        self.missedLetters = ''
        self.correctLetters = ''
        self.attempts = 0

        self.create_widgets()
        self.displayBoard()  # Display the initial board including hangman ASCII art

    # Method to get a random word from the list of words
    def getRandomWord(self):
        return random.choice(self.words)

    def create_widgets(self):
        # Font for other text
        other_font = ("Roboto Mono", 12)  # Reduced font size

        # Adjust the hangman art size and position
        self.hangman_pic = tk.Label(self.master, text="", font=("Courier", 18))  # Adjusted font size
        self.hangman_pic.pack(pady=10)  

        # Adjust missed letters label size and position
        self.missed_letters_label = tk.Label(self.master, text="Missed letters: ", font=other_font)  # Adjusted font size
        self.missed_letters_label.pack()  

        # Adjust missed letters display size and position
        self.missed_letters = tk.Label(self.master, text="", font=other_font)  # Adjusted font size
        self.missed_letters.pack()  

        # Adjust secret word display size and position
        self.secret_word_label = tk.Label(self.master, text="", font=other_font)  # Adjusted font size
        self.secret_word_label.pack(pady=10)  

        # Adjust guess label size and position
        self.guess_label = tk.Label(self.master, text="Guess a letter: ", font=other_font)  # Adjusted font size
        self.guess_label.pack()  

        # Adjust guess entry size and position
        self.guess_entry = tk.Entry(self.master, font=other_font)  # Adjusted font size
        self.guess_entry.pack()  

        # Adjust submit button size and position
        self.submit_button = tk.Button(self.master, text="Submit", font=other_font, command=self.check_guess)  # Adjusted font size
        self.submit_button.pack(pady=10)  

        # Add label to display score
        self.score_label = tk.Label(self.master, text="Score: 0", font=other_font)
        self.score_label.pack()

        # Adjust window size to fit all elements
        self.master.geometry("400x600")  # Adjusted window size

    def displayBoard(self):
        self.hangman_pic.config(text=HANGMAN_PICS[len(self.missedLetters)])
        self.missed_letters.config(text=' '.join(self.missedLetters))  # Add space between missed letters

        blanks = ''
        for letter in self.secretWord:
            if letter in self.correctLetters:
                blanks += letter
            else:
                blanks += '_ '
        self.secret_word_label.config(text=blanks)

        # Update the score
        self.score_label.config(text=f"Score: {self.score}")

    def check_guess(self):
        guess = self.guess_entry.get().lower()

        if guess in self.missedLetters + self.correctLetters:
            messagebox.showinfo("Hangman", "You have already guessed that letter. Choose again.")
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            messagebox.showinfo("Hangman", "Please enter a letter from the alphabet.")
        else:
            if guess in self.secretWord:
                self.correctLetters += guess
                if all(letter in self.correctLetters for letter in self.secretWord):
                    self.score += DIFFICULTY_POINTS[self.difficulty]  # Increase score
                    self.displayBoard()
                    messagebox.showinfo("Hangman", f"You guessed it! The secret word is '{self.secretWord}'. You win!")
                    self.score_label.config(text=f"Score: {self.score}")  # Update score label
                    self.master.destroy()
                else:
                    self.score += DIFFICULTY_POINTS[self.difficulty]  # Increase score for correct guess
                    self.displayBoard()  # Update display including hangman ASCII art
            else:
                self.missedLetters += guess
                if len(self.missedLetters) == len(HANGMAN_PICS) - 1:
                    self.displayBoard()
                    messagebox.showinfo("Hangman", f"You have run out of guesses! The word was '{self.secretWord}'.")
                    self.master.destroy()
                else:
                    self.displayBoard()

                self.attempts += 1



root = tk.Tk()
app = HangmanGUI(root)
root.mainloop()
