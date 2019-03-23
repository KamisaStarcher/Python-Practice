
#The object the will act as a calculator 
class Calc:
    def __init__(self):
        #Intial Values
        self.times_used = 0; 

    #Adding Sums and returning it
    def add(self):
        return self.sum1 + self.sum2
    
    #Subtracting Sums and returning it
    def sub(self):
        return self.sum1 - self.sum2

    #Dividing sums and returning it
    def div(self):
        return self.sum1 / self.sum2

    #Multypling Sums and returning it
    def mult(self):
        return self.sum1 * self.sum2


    def Prompt_user(self):
        #Adding to times used
        self.times_used += 1

        #Getting input from the player
        self.sum1 = float(input("Sum1: "))
        self.sum2 = float(input("Sum2: "))
        self.operation = input("Operation: ")

        #Seeing wich operation the user chose 
        #then setting our sum to the result of that function
        if self.operation == "add":
            self.sum = self.add()

        if self.operation == "sub":
            self.sum = self.sub()
        
        if self.operation == "div":
            self.sum = self.div()
                
        if self.operation == "mult":
            self.sum = self.mult()

        self.Print_sum()
    
    def Print_sum(self):
        print(self.sum)
        print(" ")
        choice = input("Would you like to use again(y/n): ")
        if choice == "y":
            self.Prompt_user()

        else:
            exit()


def Init():
    Calculator = Calc()
    Calculator.Prompt_user()


if __name__ == "__main__":
    Init()