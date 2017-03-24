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
    
    def isWordGuessed(secretWord, lettersGuessed):
        '''
        secretWord: string, the word the user is guessing
        lettersGuessed: list, what letters have been guessed so far
        returns: boolean, True if all the letters of secretWord are in lettersGuessed;
        False otherwise
        '''
        for char in secretWord:
            if char in lettersGuessed:
                return True
        return             
        
    def getGuessedWord(secretWord, lettersGuessed):
        '''
        secretWord: string, the word the user is guessing
        lettersGuessed: list, what letters have been guessed so far
        returns: string, comprised of letters and underscores that represents
        what letters in secretWord have been guessed so far.
        '''
        word = ""
        x = "_ "
        for char in secretWord:
            if char not in lettersGuessed:
                word += x
            else:
                word += (char)
        return word  
        
    def getAvailableLetters(lettersGuessed):
        '''
        lettersGuessed: list, what letters have been guessed so far
        returns: string, comprised of letters that represents what letters have not
        yet been guessed.
        '''
        import string 
        availableLetters = string.ascii_lowercase
        for char in lettersGuessed:
            availableLetters = availableLetters.replace(char,"")
        return availableLetters
            
    print "Welcome to the game, Hangman!"
    print "I am thinking of a word that is" , len(secretWord) , "letters long."
    numberGuesses = 8
    lineBreak = "-------------"
    lettersGuessed = []
    x = 8
    while x > 0:
        print lineBreak
        print "You have", numberGuesses, "guesses left"
        print "Available letters:", getAvailableLetters(lettersGuessed)
        g = raw_input("Please guess a letter: ")
        g = g.lower()
        if g in lettersGuessed:
            print "Oops! You've already guessed that letter: ", getGuessedWord(secretWord, lettersGuessed)
            numberGuesses += 1
        lettersGuessed += g
        numberGuesses -= 1
        x -= 1
        
        if g in secretWord:
            print "Good Guess:", getGuessedWord(secretWord, lettersGuessed)
            if isWordGuessed(secretWord, lettersGuessed) == True:
                print "Congratulations, you won!"
            x = 0
        if g not in secretWord:
            print "Oops! That letter is not in my word: ", getGuessedWord(secretWord, lettersGuessed)
        if numberGuesses == 0:
            print "Sorry, you ran out of guesses. The word was", secretWord, "."
            x = 0      
    return
    
print hangman(tom)   
    