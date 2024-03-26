# assignment: programming assignment 5
# author: Fiona Leung
# date: 3/8/2023
# file: game.py
# input: event-driven program: takes in input in the form of a button press
# output: game board as tkinter window

from tkinter import *
import tkinter.font as font
from fifteen import Fifteen
    
def add_button(gui, entrybox, value):
    return Button(gui, text=value, height=4, width=9, command = lambda: clickButton(entrybox, value), bg = "#f5f0dc", fg = "#ba8494")

def clickButton(entrybox, value):
    global labels
    f = Fifteen()

    # setting f.tiles list to labels list except where value == space, replace it with a 0
    if len(f.tiles) == 16:
        f.tiles = []
        # for val in labels:
        #     f.tiles.append(val)
        f.tiles = [val for val in labels]

    for i, val in enumerate(f.tiles):
        if val == " ":
            f.tiles[i] = 0
    
    if value != " ":
        move_index = f.tiles.index(value)
        empty_index = f.tiles.index(0)

    # if it's a valid move, switch the values
        if f.is_valid_move(value):
            labels[move_index], labels[empty_index] = labels[empty_index], labels[move_index]

    # updating the board
            buttons = [add_button(gui, entrybox, labels[x]) for x in range(len(labels))] # use method add_button()
            buttons[move_index].configure(bg="#f2c7d4")
            k = 4           
            for i in range(k):
                for j in range(k):
                    buttons[i*k+j].grid(row=i+1, column=j, columnspan=1)

def shuffle_board(steps = 100):
    global labels
    f = Fifteen()

    if len(f.tiles) == 16:
        f.tiles = []
        # for val in labels:
        #     f.tiles.append(val)
        f.tiles = [val for val in labels]

    for i, val in enumerate(f.tiles):
        if val == " ":
            f.tiles[i] = 0

    f.shuffle(steps)
    
    labels = []
    for val in f.tiles:
        if val == 0:
            labels.append(" ")
        else:
            labels.append(val)

    buttons = [add_button(gui, entrybox, labels[x]) for x in range(len(labels))] # use method add_button()
    buttons[f.tiles.index(0)].configure(bg="#f2c7d4")
    k = 4           
    for i in range(k):
        for j in range(k):
            buttons[i*k+j].grid(row=i+1, column=j, columnspan=1)

def reset_board():
    f = Fifteen()
    #locating the empty tile to set pink
    empty = f.tiles.index(0)

    # resetting labels and tiles lists
    f.tiles = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]
    labels = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, " "]

    # showing the new board
    buttons = [add_button(gui, entrybox, labels[x]) for x in range(len(labels))] # use method add_button()
    buttons[empty].configure(bg="#f2c7d4")
    k = 4           
    for i in range(k):
        for j in range(k):
            buttons[i*k+j].grid(row=i+1, column=j, columnspan=1)



# for GUI
if __name__ == '__main__':
    # make a board with tiles
    board = Fifteen()
    empty = board.tiles.index(0) # index where the empty space is located

    # make a GUI window
    gui = Tk()
    gui.title("Fifteen")

    entrybox = Entry(gui, width=36, borderwidth=5)
    # position the entry text box in the gui window using the grid manager
    entrybox.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

    # make fonts
    font1 = font.Font(family='Helveca', size='25', weight='bold')

    # make buttons with labels
    # labels = StringVar(gui, "1") # use StringVar() 
    labels = [x for x in range(1, 17)]
    labels[15] = (' ')
    # you can update labels
    #  for example, labels[15].set(' ')

    buttons = [add_button(gui, entrybox, labels[x]) for x in range(len(labels))] # use method add_button()

    # you can modify buttons
    buttons[empty].configure(bg="#f2c7d4")

    # arrange buttons on the grid
    k = 4           
    for i in range(k):
        for j in range(k):
            buttons[i*k+j].grid(row=i+1, column=j, columnspan=1)
            
    # add a button shuffle to shuffle the tiles
    shuffle_button = Button(gui, text="shuffle", height=4, width=9, command = lambda: shuffle_board(100), bg = "#f5f0dc", fg = "#ba8494")
    shuffle_button.grid(row = 5, column = 2, columnspan = 1)

    # when reset_button pressed, board returns to original order (1-15 + empty) aka solved board
    reset_button = Button(gui, text="reset", height=4, width=9, command = lambda: reset_board(), bg = "#f5f0dc", fg = "#ba8494")
    reset_button.grid(row = 5, column = 1, columnspan = 1)

    # spacer buttons
    spacer_button1 = Button(gui, text="♡ ⋆ ˚｡⋆୨୧˚", height=4, width=9, bg = "#f5f0dc", fg = "#ba8494")
    spacer_button1.grid(row = 5, column = 0, columnspan = 1)

    spacer_button2 = Button(gui, text="˚୨୧⋆｡˚ ⋆ ♡", height=4, width=9, bg = "#f5f0dc", fg = "#ba8494")
    spacer_button2.grid(row = 5, column = 3, columnspan = 1)

    
    # # update the window
    gui.mainloop()