#This is a number guessing game from the range of numbers between 1 and 100.
import random

#These are the variables assigned into the game as well as the play_again input.
#The game will keep track of how many guesses the player has made through the count variable and reset when the said player plays again.
#The secret variable is the range function in the random module in which it will pick a random number in the range from 1-100.
secret = random.randrange(1,100)
players_guess = 0
count = 1
play_again = "y"

#Welcomes the player and describes the rules of the game!
print("Welcome to Guess the Number Game 1-100!")
print("A number will be randomly picked between 1 and 100. Your goal is to guess the correct number!")
print("Good Luck Player!")
#while play_again == 'y' The Game will loop when the player guesses the correct number.
while play_again == "y":
    while players_guess != secret:
        players_guess = int(input("Please Enter A Number Between 1 and 100: "))
        if players_guess == "":
            print("Please enter a number or integer!")
        if players_guess > secret:
                print("Guess is too high, drop it like its hot, and guess again.")
                count += 1
        elif players_guess < secret:
                print("Guess is too low, raise the roof, and guess again.")
                count += 1
        else:
            print("Well Done! You guessed the correct number! The number was", secret, "You guessed in", count , "tries!")

# The Player's Guess must equal secret's random number here.
#Once the player guesses the correct number and is shown how many attempts it took to guess, the game will ask the player if they would like to play again.

    play_again = input("Wanna Go Again? y/n: ")
    if play_again == "y":
        secret = random.randrange(1,100)
        count = 1
        print("Alright, Here's another random number!")

# If the player inputs 'n' It will end the game and thanking them for playing!

    if play_again == "n":
        print("Thanks For Playing! Come Play Again Sometime!")


        
    

