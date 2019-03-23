import random #Importing somoone else work
              #and using it in my own. Also
              #Known as modules.

#Creating a class that holds the information
#And functions of the game.
class Guess_Game:
    def __init__(self):
    #Setting Intial Values

        #The Number That Needs To Be Guessed
        self.magic_number = random.randint(0, 10)

        #The Number Of Guesses
        self.guesses = 0
        
        #Haven't Guessed The Number So The Game Is True
        self.game = True
    #All this part does is close
    #The main game loop
    def won(self):
        self.game = False

    def Guess(self):
    #Guessing the Number
        #Getting input from the user
        #Then changing it to an interger value
        self.gues = int(input("Guess: "))

        #Checking to see if the guesses number
        #Is less then the number that needs to be gussed
        if self.gues < self.magic_number:
            print("Guess Higher")#Giving the player a hint 
            self.guesses += 1 #Adding to the number of guesses
            self.Guess()#Recalling the guess function
            
        #The Guess was greater than the needed number
        if self.gues > self.magic_number:
            print("Lower")#Giving the player a hint
            self.guesses += 1#Adding to the number of guesses
            self.Guess()#Recalling the guess function

        #The guessed number is = to the needed number 
        if self.gues == self.magic_number:
            self.won() #Calling a function 
            #that closes the main game loop 

def Game():
    #Creates a an instance of the Gues Game class
    Game = Guess_Game()
    
    #Is saying that when the game is active
    #Then call the Guess Games Guess Function 
    while Game.game:
        Game.Guess()
        #Exits the loop if the Game 
        #Is no longer active
        if Game.game == False:
            break

    #Prints the the winning game message and stats
    print("You won in {} tries.".format(Game.guesses+1))
    print("The number was {}.".format(Game.magic_number))
        
# Checking to see if this program 
#Isn't being imported and is being
#Run from this file then calls Game Function
if __name__ == "__main__":
    Game()
