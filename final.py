#This is a standard game of Hangman, A word will be chosen at random from a list containing either a random word, Person/Character, and or Movie Title and the player must guess the word/words letter by letter before said player runs out of attempts.
import random

def main():
    welcome = ['Welcome to Hangman! A word (random word, person/character, or movie title) will be chosen randomly and',
               'you must try to guess the word correctly letter by letter',
               'before you run out of guesses. Good Luck Player!'
               ]

    for line in welcome:
        print(line, sep='\n')

    #This sets up the play_again at the end of the game

    play_again = True

    while play_again:
        #Sets up game loop

        words = ["hangman", "chairs", "backpack", "bodywash", "clothing",
                 "computer", "python", "program", "glasses", "sweatshirt",
                 "sweatpants", "mattress", "friends", "clocks", "biology",
                 "algebra", "suitcase", "knives", "ninjas", "shampoo", "abruptly",
                 "foxglove", "subway", "thumbscrew", "sapphire", "matrix", "galaxy",
                 "naphtha", "nightclub", "unknown", "vaporize", "peekaboo", "oxygen",
                 "numbskull", "pneumonia", "voyeurism", "psyche", "jawbreaker", "buxom",
                 "bandwagon", "phlegm", "caliph", "vodka", "bagpipes", "witchcraft", "xylophone",
                 "zephyr", "daiquiri", "rhythm", "rhubarb", "schnapps", "kayak", "scratch",
                 "razzmatazz", "yippee", "duplex", "stronghold", "flyby", "jukebox", "squawk", "jumbo",
                 "keyhole", "disvow", "snazzy", "shiv", "wristwatch", "sphinx", "zipper", "zigzag", "zilch", "zodiac",
                 "zombie", "stymied", "larynx", "knapsack", "quiz", "wimpy", "wizard", "country", "wave", "cockiness", "croquet",
                 "jumbo", "juicy", "George Washington", "fixable", "jackpot", "puppy", "kitty", "parrot", "espionage", "exodus",
                 "crusade", "kilobyte", "kiosk", "fluffiness", "buffalo", "icebox", "iatrogenic", "bookworm", "oxidize", "vixen",
                 "voodoo", "grogginess", "boggle", "hyphen", "buckaroo", "jazziest", "blizzard", "triphthong", "mnemonic", "transgress",
                 "gazebo", "galvanize", "azure", "haiku", "onyx", "naphtha", "gnarly", "gnostic", "giaour", "microwave", "pajama", "bayou",
                 "buxom", "jelly", "jaundice", "jaywalk", "crypt", "undead", "puzzling", "haphazard", "injury", "coma", "heart", "transplant",
                 "art", "paint", "draw", "color", "rainbow", "Pocahontas", "wellspring", "gizmo", "Star Wars", "Indiana Jones", "Luke Skywalker",
                 "Force", "Leia", "Yoda", "guild", "raid", "zenith", "wavy", "walkaway", "Cardi B", "Morgan Wallen", "Rihanna", "Rolling Stones",
                 "Whitney Houston", "outlook", "presence", "ouija", "haunted", "university", "queen", "king", "Ghandi", "Justin Bieber", "Katy Perry", "Lady Gaga", "Donald Duck",
                 "Hugh Jackman", "Madonna", "Miley Cyrus", "Christopher Colombus", "Justin Timberlake", "Goofy", "Johnny Depp", "Paris Hilton", "Daniel Radcliffe", "Harry Potter",
                 "Brittney Spears", "Harrison Ford", "Brad Pitt", "Angelina Jolie", "Julia Roberts", "Top Gun", "Peter Pan", "Elemental", "Cinderella", "Hercules", "Alice in Wonderland",
                 "Doctor Dolittle", "Mulan", "Princess and the Frog", "Finding Nemo", "Maleficent", "Cars", "Toyota", "Chevrolet", "Dodge", "Shrek", "Jungle Book", "Ace Ventura",
                 "Ghostbusters", "Pitch Perfect", "Garfield", "Jurassic Park", "Jeff Goldblum", "Lord of the Rings", "Game of Thrones", "Spiderman", "Titanic", "Toy Story", "Terminator",
                 "Robo Cop", "Hunger Games", "Kung Fu Panda", "Pirates of the Caribbean", "Camp Rock", "Madagascar", "Ratatouille", "Mean Girls", "Forrest Gump", "Tom Hanks", "Christmas", "Tarzan",
                 "Twilight", "Enchanted", "The Godfather", "High School Musical", "Inside Out", "Napoleon Dynamite", "Aladdin", "Shawshank Redemption", "Pink Panther", "Bugs Bunny", "Daffy Duck",
                 "Bodyguard", "",
                  ]

        chosen_word = random.choice(words).lower()
        player_guess = None #Holds the current players guesses
        guessed_letters = [] #list of letters guess so far
        word_guessed = []
        for letter in chosen_word:
            word_guessed.append("-") #creates unguessed, blank version of the word
        joined_word = None #joins words in the list word_guessed

        HANGMAN = (
"""
-----
|   |
|
|
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
|
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
|  -+-
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|  |
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|  | 
|  | 
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|  | | 
|  | 
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|  | | 
|  | | 
|
--------
""")

        print(HANGMAN[0])
        attempts = len(HANGMAN) - 1


        while (attempts != 0 and "-" in word_guessed):
            print(("\nYou have {} letter guesses remaining").format(attempts))
            joined_word = "".join(word_guessed)
            print(joined_word)

            try:
                player_guess = str(input("\nPlease select a letter between A-Z" + "\n> ")).lower()
            except: #checking for valid input
                print("That isn't a valid input. Try again.")
                continue                
            else: 
                if not player_guess.isalpha(): #checks input is a letter and if input has been done.
                    print("That isn't a letter. Try again.")
                    continue
                elif len(player_guess) > 1: #checks if the input is one letter
                    print("That's more than one letter. Try again.")
                    continue
                elif player_guess in guessed_letters: #checks if letter was guessed already.
                    print("You already guessed that. Try again, and GET IT TOGETHER!")
                    continue
                else:
                    pass

            guessed_letters.append(player_guess)

            for letter in range(len(chosen_word)):
                if player_guess == chosen_word[letter]:
                    word_guessed[letter] = player_guess #replaces all letters in chosen word that matches players guess
            if player_guess not in chosen_word: #no blanks remaining
                attempts -= 1
                print(HANGMAN[(len(HANGMAN) - 1) - attempts])

        if "-" not in word_guessed: 
            print(("\nRight on! {} was the word").format(chosen_word))
        else: #the loop ended with the attempts reaching 0
            print(("\nBummer! The word was {}.").format(chosen_word))

        print("\nWanna have another go at it?")

        response = input("> ").lower()
        if response not in ("yes", "y"):
            play_again = False

if __name__ == "__main__":
    main()
