# The Hangman Game

## 1. What is the Hangman Game?
Hangman is a classic word-guessing game where one player thinks of a word and the other player tries to guess it by suggesting letters. With each incorrect guess, a part of the hangman is drawn. The game's simplicity and suspense make it a timeless favorite among players of all ages.

## 2. Project Team
- Dipanshu Puri 2310991818 - Project Manager: Oversees project planning, coordinates team efforts, and ensures timely delivery.
- Anuj Yadav 2310991783 - Developer: Implements game logic, UI elements, and debugging.
- Anshul Phondni 2310991781 - Tester: Conducts rigorous testing to identify bugs, provides feedback for improvement, and ensures game stability.

## 3. Instructions for Playing the Hangman Game
I. Start the game by running the Python code provided in the repository. Ensure you have Python installed on your system.

II. Guess letters one by one to uncover the secret word. Keep in mind that only lowercase alphabets are accepted as valid inputs.

III. If the guessed letter is in the word, it will be revealed in its correct position; otherwise, a part of the hangman will be drawn. Aim to guess the word before the hangman is fully drawn to win the game.

IV. Continue guessing until you either reveal the entire word or the hangman is completely drawn. Exercise your deduction skills and vocabulary knowledge to increase your chances of winning.

V. After each game, you will be prompted to play again. Choose whether to continue playing or exit the game.

## 4. Additional Features & Notes
A. Scoring System: A scoring mechanism based on word difficulty and player performance adds a competitive element to the game. Compete with friends or challenge yourself to achieve high scores.

B. Replayability: The game offers a play again option, allowing users to restart after each round, enhancing user engagement. Challenge yourself to beat your previous score or try different word categories for a fresh experience.

C. Modular Structure: The code's organization into functions improves readability and maintainability. Each component of the game is encapsulated within functions, making it easier to understand and modify for future enhancements.


ERRORS IN VERSION 1 CODE:

1. *No input validation for theme choice*: If the user enters a non-numeric value for the theme choice, the program will throw an error or produce unexpected behavior. You could add input validation to ensure that the theme choice is a number between 1 and 5.

2. *Scoring calculation might be incorrect*: The scoring calculation in the calculatePoints function doesn't take into account the difficulty level chosen by the player. The function always uses the medium difficulty points regardless of the actual difficulty level selected. You could update the function to consider the difficulty level chosen by the player.


ERRORS IN VERSION 2 AND VERSION 3 CODE:

1. *Theme selection error handling*: If the user enters a non-numeric value for the theme choice, the program will not handle it gracefully and may throw an error. You could add input validation to ensure that the theme choice is a number between 1 and 5.

2. *Difficulty selection validation*: Although the difficulty level is selected through numbers 1, 2, or 3, there is no explicit indication of the corresponding difficulty level (easy, medium, hard) in the input prompt. This could lead to confusion for the player, and it would be better to clarify the difficulty levels in the prompt.
