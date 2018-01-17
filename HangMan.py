
import random

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
setOfWords = '''ant baboon badger bat bear beaver camel cat clam cobra cougar
      coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk
      lion lizard llama mole monkey moose mouse mule newt otter owl panda
      parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep
      skunk sloth snake spider stork swan tiger toad trout turkey turtle
      weasel whale wolf wombat zebra'''

def getRandomWord(setOfWords):
    Words_Available = setOfWords.split()
    return random.choice(Words_Available)
    #secretWordIndex = random.randint(0, len(Words_Available) - 1)
    #return setOfWords[secretWordIndex]


def displayHangManBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print("Missed letters are: \n")
    for letters in missedLetters:
        print(letters, end =' ')
    print()

    #prints blanks
    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letters in blanks:
        print(letters, end=' ')
    print()

def guessValidate(alreadyGuessedWords):
    while True:
        print("Enter a letter")
        guessedLetter = input()
        guessedLetter = guessedLetter.lower()
        if(guessedLetter not in 'abcdefghijklmnopqrstuvwxyz'):
            print("You've not a letter. Please enter a letter.")
        elif(len(guessedLetter) > 1):
            print("Enter a single character")
        elif(guessedLetter in alreadyGuessedWords):
            print("You've guessed the letter "+ guessedLetter+ "already. Enter a new one.")
        else:
            return guessedLetter

def playAgain():
    print("Do you want to play again? (y/n)")
    return input().lower().startswith('y')


print('HANGMAN GAME BEGINS!')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(setOfWords)
gameOver = False

while True:
    displayHangManBoard(missedLetters,correctLetters,secretWord)
    guessedLetter = guessValidate(missedLetters + correctLetters)

    if guessedLetter in secretWord:
         correctLetters = correctLetters + guessedLetter

         foundAllLetters = True
         for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
         if(foundAllLetters == True):
            count = len(missedLetters) + len(correctLetters)
            print("Wohoo! You've won the game with total number of guesses" + str(count))
            gameOver = True

    else:
        missedLetters = missedLetters + guessedLetter
        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            displayHangManBoard(missedLetters, correctLetters, secretWord)
            print("Oops! You ran out of chances. :(")
            print("The word was" + secretWord)
            gameOver = True

    if(gameOver == True):
        if playAgain() == True:
            missedLetters = ''
            correctLetters = ''
            secretWord = getRandomWord(setOfWords)
            gameOver = False
        else:
            print("Until next time!")
            break



#check how close you are to the answer - give hints for missing letter
