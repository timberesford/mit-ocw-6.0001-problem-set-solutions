# Problem Set 2, hangman.py
# Name: Tim Beresford
# Collaborators:
# Time spent: 1 hour

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"

# secret_word = "banana"


def load_words():
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



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # Loop through characters in secret_word and check if found in letters_guessed
    for char in secret_word:
        if char in letters_guessed:
        
            # defining a boolean called "guess_status" for the function to return
            guess_status = True
        else:
            guess_status = False
            break
        
        
    return guess_status

# secret_word = "apple"
# letters_guessed = ["a", "p", "p", "l", "e", "s"]
# print(is_word_guessed(secret_word, letters_guessed))

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # create empty string display_word
    display_word = ""
    
    # loop through characters in secret word 
    for char in secret_word:
        # concatenate char to display_word if in letters guessed
        if char in letters_guessed:
            display_word += char
        
        # if char not found in letters guessed, place "_ "
        else:
            display_word += "_ "
            
    return display_word




def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # create string of complete lower case alphabet
    lower_case_alphabet = string.ascii_lowercase
    
    # create empty string to create string to be outputted
    output_string = ""

    # loop through complete alphabet and include char in output if char not found in letters guessed
    for char in lower_case_alphabet:
        if char not in letters_guessed:
            output_string += char
    return output_string


def print_guesses_and_letters(guesses_remaining, letters_guessed):
    '''
    Function to just print the number of guesses remaining and the available 
    letters to choose from
    
    
    '''
    
    print("You have ",guesses_remaining," guesses remaining...")
    print("Available letters: ", get_available_letters(letters_guessed))
    return

def is_guess_good (current_guess, letters_guessed, warnings_remaining, guesses_remaining):
    '''
    Function to just check if current guess conforms to requirements 
    (is a letter from the alphabet) and deducts a warning (& then a guess
    when all warnings used) if not
    
    

    '''
    # check input is alphabetic 
    if str.isalpha(current_guess):
        # convert current guess to lower case if not already
        current_guess = str.lower(current_guess)
        # check if current guess is a duplicate
        if current_guess not in letters_guessed:
            status = True
            # adds current guess to letters guessed
            letters_guessed += current_guess
        else:
            status = False
            # deduct a warning if still remaining
            if warnings_remaining > 0:
                warnings_remaining -= 1
                print("You have already guessed the letter", current_guess+ "!")
                print("You have lost a warning and now have", warnings_remaining, "warnings remaining.")
                status = False
            
            # deduct a guess if no warnings remaining
            else:
                print("You have already guessed the letter", current_guess + "!")
                print("You have no warnings left and have lost a guess!")
                guesses_remaining -= 1
                print("You now have",guesses_remaining,"guesses remaining.")
                status = False
            
    
    # deduct a warning if still remaining
    elif warnings_remaining > 0:
        warnings_remaining -= 1
        status = False
        print("Please only enter letters from the alphabet!")
        print("You have lost a warning and now have", warnings_remaining, "warnings remaining.")
    
    # deduct a guess if no warnings remaining
    else:
        print("Please only enter letters from the alphabet!")
        print("You have no warnings left and have lost a guess!")
        guesses_remaining -= 1
        print("You now have",guesses_remaining,"guesses remaining.")
        status = False
   
    return (status, warnings_remaining, guesses_remaining, letters_guessed)
       
def is_guess_correct (current_guess, secret_word, guesses_remaining):
    '''
    Check if current guess is containined in word
    '''
    # Define vowels
    vowels = ["a","e","i","o","u"]
          
    # test if current guess correct
    if current_guess not in secret_word:
        
        guess_correct = False
        
        # check if current guess is a vowel or consonant and assign appropriate penalty    
        if current_guess in vowels:
            # Deduct 2 guesses for incorrect vowel guess
            guesses_remaining -= 2
            print ("That is an incorrect vowel guess and you now have",guesses_remaining, "guesses remaining!")    
        else:
            # deduct 1 guess for incorrect consonant
            guesses_remaining -=1
            print ("That is an incorrect consonant guess and you now have",guesses_remaining,"guesses remaining!")
        
    # if guess is correct, no guesses deducted and guess_correct status True           
    else:
        print("That is a correct guess!",current_guess, "is in the word you are trying to guess!")
        guess_correct = True
        
    return (guess_correct, guesses_remaining)

    
    
        

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    
    # initiate some of the parameters required
    
    # letters_guessed created as empty list
    letters_guessed = []
    
    # initiate number of guesses given at start
    guesses_remaining = 6
    
    # assigning initial warnings remaining
    warnings_remaining = 3
    
    # Give welcome spiel and initiate game for user player
    
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is ",len(secret_word), " letters long.")
    print("---------------------------------------------------------------------")

    
    # only run game whilst player still has guesses remaining
    while guesses_remaining > 0:
        
        if is_word_guessed(secret_word, letters_guessed):
            print("Congratulations! You have guessed the word,", secret_word + ", and have won the game!")
            break
        
        print_guesses_and_letters(guesses_remaining, letters_guessed)
        current_guess = input("Please enter a guess: ")
        # run is guess good function and assign to temp data structure
        guess_good_data = is_guess_good(current_guess,letters_guessed,warnings_remaining,guesses_remaining)
        
        # re-assign output values from is guess good to variables
        guess_good_status = guess_good_data[0]
        warnings_remaining = guess_good_data[1]
        guesses_remaining = guess_good_data[2]
        letters_guessed = guess_good_data[3]
        
        if guess_good_status:
            guess_correct_data = is_guess_correct(current_guess,secret_word,guesses_remaining)
            guesses_remaining = guess_correct_data[1]
        
        print(get_guessed_word(secret_word, letters_guessed))
        
        
    if guesses_remaining <= 0:
        print("Unlucky! You have 0 guesses remaining and have lost the game")
        print("The secret word was",secret_word)
            
        
        
                
    return



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    
    # create parameter with default as True
    status = True
    
    # create copy of my_word with no spaces  
    
    my_word_condensed = my_word.translate({ord(i):None for i in ' '})
    
    
    # if lengths match, check character by character
    if len(other_word) == len(my_word_condensed):
        
        # create a counter to check letters against
        index = 0
        # create empty array to store letters already in correct position
        letter_store = []
        
        # loop through condensed word to find matches in word list
        for char in my_word_condensed:
            
            # if letter in secret word is known, check it against wordlist word
            if char != "_": 
            
                # add current letter to letter store
                letter_store.append(char)
            
                # check if known letter matches letter in wordlist word    
                if char != other_word[index]:
                    status = False
                    break
            # check if letter in this position in wordlist word has already been placed in secret word elsewhere but is blank here
            elif char == "_" and other_word[index] in letter_store:
                status = False
                break
                
                    
            index += 1
    else:
        status = False
        
    return status

            
    
        
        



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    
    #counter
    counter = 0
    
    for i in wordlist:
        if match_with_gaps(my_word,i):
            counter += 1
            print (i)
    if counter == 0:
        print("No matches found")
     
   



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # initiate some of the parameters required
    
    # letters_guessed created as empty list
    letters_guessed = []
    
    # initiate number of guesses given at start
    guesses_remaining = 6
    
    # assigning initial warnings remaining
    warnings_remaining = 3
    
    # Give welcome spiel and initiate game for user player
    
    print("---------------------------------------------------------------------")
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is ",len(secret_word), " letters long.")
    print("---------------------------------------------------------------------")

    
    # only run game whilst player still has guesses remaining
    while guesses_remaining > 0:
        
        if is_word_guessed(secret_word, letters_guessed):
            print("Congratulations! You have guessed the word,", secret_word + ", and have won the game!")
            break
        
        print_guesses_and_letters(guesses_remaining, letters_guessed)
        current_guess = input("Please enter a guess: ")
        
        if current_guess != "*":
           
        
            # run is guess good function and assign to temp data structure
            guess_good_data = is_guess_good(current_guess,letters_guessed,warnings_remaining,guesses_remaining)
            
            # re-assign output values from is guess good to variables
            guess_good_status = guess_good_data[0]
            warnings_remaining = guess_good_data[1]
            guesses_remaining = guess_good_data[2]
            letters_guessed = guess_good_data[3]
            
            if guess_good_status:
                guess_correct_data = is_guess_correct(current_guess,secret_word,guesses_remaining)
                guesses_remaining = guess_correct_data[1]
            
            print(get_guessed_word(secret_word, letters_guessed))
            
            
            if guesses_remaining <= 0:
                print("Unlucky! You have 0 guesses remaining and have lost the game")
                print("The secret word was",secret_word)
            
        else:   
            show_possible_matches(get_guessed_word(secret_word, letters_guessed))            
    
        
        
    return



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
