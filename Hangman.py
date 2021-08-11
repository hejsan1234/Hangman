# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for char in secretWord:
      if (char in lettersGuessed) == False:
        guessed = False
        break
      else:
        guessed = True

    return guessed



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    str1 = ''
    word = []
    for i in secretWord:
        if i in lettersGuessed:
            word.append(i)
        else:
            word.append('_ ')
    return str1.join(word)



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    letters = 'abcdefghijklmnopqrstuvwxyz'
    unguessed = ""
    #for each item in letters, check if it's been guessed; if not, added to unguessed variable
    for char in letters:
      if char not in lettersGuessed:
        unguessed += char
    return unguessed
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    
    guesses = 8
    lettersGuessed = []
    print('Welcome to the game hangman')
    print('The word im thinking of is ' + str(len(secretWord)) + ' letters long!')
    
    while True:
        
        print('You have ' + str(guesses) + ' guesses left')
        guess = input('Guess with a letter: ')
        correct_guess = guess.lower()
        lettersGuessed.append(correct_guess)
    
        if isWordGuessed(secretWord, lettersGuessed) == True:
            print('You are correct, ' + secretWord + ' is my secret word and therefore you win!!!!\nCongratulations!!!')
            break
        
        elif guesses == 1:
            print('you have 0 guesses left and therefore you lost the game! \nThe secret word was ' + secretWord + '\n')
            break
        
        elif correct_guess in secretWord:
            print('you are correct, ' + correct_guess + ' is in my secret word')
            print(getGuessedWord(secretWord, lettersGuessed))
            print(getAvailableLetters(lettersGuessed))
            
        
        else:
            print('you are not correct, ' + correct_guess + ' is not in my secret word')
            print(getGuessedWord(secretWord, lettersGuessed))
            print(getAvailableLetters(lettersGuessed))
            guesses -= 1
            
        





# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
