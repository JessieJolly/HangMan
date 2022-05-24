# HangMan
A simple hangman game created using pygame module in python

## Requirements
Make sure you have the pygame module along with Python. If not, use the package manager [pip](https://pip.pypa.io/en/stable/) to install.

` 
pip install pygame
` 

also do download the .ttf file given along and keep it in the same folder as the python file.

## Instructions
The game consists of the user guessing the word on screen. Upon guessing a letter, the guessed_words list is updated which the user can see on pygame window. 
If the guessed letter is present in the word, it appears on screen. Else the stick figure of hangman begins to take shape. Correctly guessing the words awards the
user 10 points. If the stick figure completes before, the game ends. Following are the features of the game:

* Each correct guess of the words awards you 10 points.
* The user gets a strikes for each wrong letter. With each strike, the stick figure takes shape. If it completes(10 strikes), then the game ends.
* When the user guesses the correct word, he/she is automatically taken to next word to guess.
* Each guessed letter is displayed for the user to see.

## How to run
Run the game by simply executing the python file(make sure the font file is in the same directory).

` 
python game.py
`

## Screenshots
<img width="598" alt="image" src="https://user-images.githubusercontent.com/68645801/170106422-619599b6-9c5e-4883-b70c-c3aa4467ed12.png">
<img width="594" alt="image" src="https://user-images.githubusercontent.com/68645801/170106619-57f8ddb3-1e7b-405d-a899-182dc87a7e38.png">
<img width="595" alt="image" src="https://user-images.githubusercontent.com/68645801/170106792-69f326db-d831-4b69-8d09-0e6b5b03c138.png">
<img width="595" alt="image" src="https://user-images.githubusercontent.com/68645801/170106898-2cffa6b4-de52-4ef1-bab9-2f8a680f9284.png">


## Contribution
Jessica Jolly UwU

I'm still a beginner in programming, so I know there are better ways to implement some of these features. 
If you know an easier and more efficient way to do so, do let me know!
