import secrets #imports secrets 

class NumberGuess:
    def __init__(self):
        self.difficulty = 1 #strt difficulty at 1 
        self.streak = 0 #sets streak to 0 
        self.number = 0 #defauly number 

    def generate_number(self):  #method for generating the numebr 
        if self.difficulty == 1:  #if number is 1 
            self.time = .5  #time for number shown is .5 seconds 
            self.number = secrets.choice(range(1, 10))  #generates the number 
        elif self.difficulty == 2:
            self.time = .6
            self.number = secrets.choice(range(10, 100))
        elif self.difficulty == 3:
            self.time = .7
            self.number = secrets.choice(range(100, 1000))
        elif self.difficulty == 4:
            self.time = .6
            self.number = secrets.choice(range(1000, 10000))
        elif self.difficulty == 5:
            self.time = .7
            self.number = secrets.choice(range(10000, 100000))
        elif self.difficulty == 6:
            self.time = 1.2
            self.number = secrets.choice(range(100000, 1000000))
        elif self.difficulty == 7:
            self.time = 1.9
            self.number = secrets.choice(range(1000000, 10000000))
        elif self.difficulty == 8:
            self.time = 2.1
            self.number = secrets.choice(range(10000000, 100000000))
        elif self.difficulty == 9:
            self.time = 2.5
            self.number = secrets.choice(range(100000000, 1000000000))
        elif self.difficulty == 10:
            self.time = 3
            self.number = secrets.choice(range(1000000000, 10000000000))

    def check_guess(self, guess):  #checks if the number is correct
        if int(guess) == self.number:  #if correct
            self.streak += 1   #adds 1 to  the streak 
            if self.streak == 3:  #if the streak reaches 3 
                if self.difficulty < 10:  #f the difficulty is below 10 
                    self.difficulty += 1   #add 1 to the difficulty 
                self.streak = 0   #reset streak to 0 
            return "correct"  #return corrrect
        else:  #or 
            self.streak = 0  
            return "incorrect"   #return incorrect 
        
        
