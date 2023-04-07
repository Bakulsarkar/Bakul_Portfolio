import random
import string
from words import words

def get_valid_word(words):
    word = random.choice(words)
    while '_' in word or ' ' in word:
        word = random.choice(words)
    
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 6

    #getting user input
    while len(word_letters)>0 and lives>0:
        #letters used
        #' '.join(['a', 'b', 'cd']) ---> 'a b cd'
        print('You have', lives, 'lives have used these letters: ', ' '.join(used_letters))
        
        #what current word is (W _ O R D)
        word_list = [letter if letter in used_letters else '_' for letter in word]
        print('current word: ', ' '.join(word_list))
        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives-1 #takes away a life if wrong
                print('Letter is not in word.')

        elif user_letter in used_letters:
            print("You have already used that character. Please try again.")
        
        else:
            print("Invalid character. Please try again.")
        if lives == 6:
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
        elif lives == 5:
            print("   _____ \n"
                  "  |     | \n"
                  "  |     | \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
        elif lives == 4:
            print("   _____ \n"
                  "  |     | \n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
        elif lives == 3:
            print("   _____ \n"
                  "  |     | \n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|  \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
        elif lives == 2:
            print("   _____ \n"
                  "  |     | \n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\  \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
        elif lives == 1:
            print("   _____ \n"
                  "  |     | \n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\  \n"
                  "  |    / \n"
                  "  |      \n"
                  "__|__\n")
        elif lives == 0:
            print("   _____ \n"
                  "  |     | \n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\  \n"
                  "  |    / \  \n"
                  "  |      \n"
                  "__|__\n")

    #gets here when len(word_letters) == 0 OR whwn lives = 0
    if lives == 0:
        print('You died, Sorry. The word was', word)
    else:
        print('you guessed the word', word, '!!')

hangman()