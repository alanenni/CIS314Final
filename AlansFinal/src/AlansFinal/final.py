from tkinter import Tk #imports TK class
from numberGuess import NumberGuess #imports the numberGuess function
from gui import GUI   #imports the gui

if __name__ == "__main__": 
    game = NumberGuess()  #creates the game logic 
    root = Tk()  #creates the main window
    gui = GUI(root, game)  #creates the gui and uses the window and game logic 
    root.mainloop()  #starts the gui loop to keep the window runnning 
