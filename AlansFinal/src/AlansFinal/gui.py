import tkinter as tk #imports tkinter
from tkinter import messagebox #imports messagebox
import time #imports time
import threading # imports threading
from numberGuess import NumberGuess  #Make sure you import the NumberGuess class

class GUI:
    def __init__(self, root, game):
        self.root = root  #creates root window
        self.root.title("Number Remembery Game")  #sets window title
        self.root.geometry("600x400")  #sets window size
        self.game = game  #holds game logic

        # label for difficulty
        self.diffLbl = tk.Label(root, text="Select Start Difficulty:", font=("Ayrial", 20))  #font/ size for diff label
        self.diffLbl.pack(pady=10)  #adds label to window

        # difficulty dropdown
        self.diffVar = tk.StringVar(value="1")  #default diff 1 
        self.diffMenu = tk.OptionMenu(root, self.diffVar, *[str(i) for i in range(1, 11)])  #creates dropdown 1-10 for difficulty
        self.diffMenu.config(font=("Ayrial", 14))  #font for dropdown
        self.diffMenu.pack()   #adds dropdown to window

        #start button 
        self.strtBtn = tk.Button(root, text="Start Game", command=self.diffStrt, font=("Ayrial", 20))  #game start button 
        self.strtBtn.pack(pady=10) #adds start button 

        #label for number 
        self.lbl = tk.Label(root, text="", font=("Ayrial", 53))   #font and size for number label
        self.lbl.pack(pady=30) #adds number label

        #guess entry 
        self.entry = tk.Entry(root, font=("Ayrial", 24), justify='center')  #input box for guess
        self.entry.pack(pady=10) #adds input box 
        self.entry.pack_forget()   #hides input box 

        #submit button 
        self.buttn = tk.Button(root, text="", command=None, font=("Ayrial", 21))  #empty button for submission
        self.buttn.pack(pady=10)  #adds button to window
        self.buttn.pack_forget()  #hides button

        #result label
        self.result = tk.Label(root, text="", font=("Ayrial", 21))  #result label font
        self.result.pack(pady=10)  #adds padding to the window 

    # sets difficulty
    def diffStrt(self):  
        selected = self.diffVar.get() #gets difficulty frm dropdown menu
        if selected.isdigit(): #checks if the guess is a numebr 
            self.game.difficulty = int(selected) #sets difficulty 
            self.diffLbl.pack_forget() #hides difficulty label
            self.diffMenu.pack_forget() #hides label
            self.strtBtn.pack_forget() #hides start button 
            self.startGame() #starts game

    #start game method
    def startGame(self):
        self.result.config(text="")#resets result label 
        self.buttn.pack_forget()#hides next button 
        self.entry.pack_forget() #hides input 
        self.game.generate_number() #generates random number 
        self.lbl.config(text=str(self.game.number)) #displays number 
        self.root.update()  #update GUI
        threading.Thread(target=self.hideNum).start() #thread to hide numebr after certain time 

#hide number 
    def hideNum(self):
        time.sleep(self.game.time) #waits for time from difficulty 
        self.lbl.config(text="What was the number?", font=("Ayrial", 32)) #changes label text to ask for the number 
        self.entry.delete(0, tk.END) #clear input from entry
        self.entry.pack() #show entry box 
        self.buttn.config(text="Submit", command=self.chkAns) #change button text to submit 
        self.buttn.pack()#shows submit nutton 

#checks users guess 
    def chkAns(self):
        guess = self.entry.get()#gets guess from the entry box 
        if not guess.isdigit(): #checks if the guess is valid 
            messagebox.showwarning("INVALID INPUT", "ENTER A NUMBER!") #warning for invalid guess 
            return
        result = self.game.check_guess(guess) #checks if guess is correct 

        #show correct numeber 
        if result == "incorrect":   #if the result is wrong 
            self.result.config(text=f"INCORRECT!\nYour guess: {guess}\nCorrect Guess: {self.game.number}")  #shows the correct number with the wrong guess
        else:# if right
            self.result.config(text=f"CORRECT!\nCurrent Difficulty: {self.game.difficulty}")

    #clear numebr label 
        self.lbl.config(text="")  #removes number from label
        self.entry.pack_forget()#hide entry box 
        self.buttn.config(text="Next", command=self.startGame) #change button to next and repeat game 
