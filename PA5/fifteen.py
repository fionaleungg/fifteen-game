# assignment: programming assignment 5
# author: Fiona Leung
# date: 3/8/2023
# file: fifteen.py
# input: input a number(integer) 1-15 to play game or q (string) to quit game
# output: outputs game board (strings)

import numpy as np
from random import choice

class Fifteen:
    
    def __init__(self, size = 4):
        self.tiles = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]
        self.adj = [[1, 4], [0, 2, 5], [1, 3, 6], [2, 7], [0, 5, 8], [1, 4, 6, 9], [2, 5, 7, 10],
                    [3, 6, 11], [4, 9, 12], [5, 8, 10, 13], [6, 9, 11, 14], [7, 10, 15], [8, 13], 
                    [9, 12, 14], [10, 13, 15], [11, 14]]

    def update(self, move):
        move_index = self.tiles.index(move)
        empty_index = self.tiles.index(0)
        if self.is_valid_move(move):
            self.transpose(move_index, empty_index)
        
    def transpose(self, i, j):
        self.tiles[i], self.tiles[j] = self.tiles[j], self.tiles[i]

    def shuffle(self, steps = 100): 
        # index = np.where(self.tiles == 0)[0][0]
        index = self.tiles.index(0)
        for i in (range(steps)):
            move_index = choice (self.adj[index])
            self.tiles[index],self.tiles[move_index] = self.tiles[move_index],self.tiles[index]
            index = move_index
        
    def is_valid_move(self, move):
        # get location of empty space and tiles adjacent to it
        empty = self.tiles.index(0)
        adj_to_empty = self.adj[empty]

        # checking if the move in the adjacent tiles list <-- these are indices
        for tile in adj_to_empty:
            if self.tiles[tile] == move:
                return True
        return False

    def is_solved(self):
        # if 0 is not in the last spot, then it's not solved
        if self.tiles[15] != 0:
            return False
        
        # checking if each tile is in numerical order
        for i, space in enumerate(self.tiles[:len(self.tiles) - 1]):
            if (space != (i + 1)):
                return False
        return True
            
    def draw(self):
        # +---+---+---+---+
        # | 1 | 2 | 3 | 4 |
        # +---+---+---+---+
        # | 5 | 6 | 7 | 8 |
        # +---+---+---+---+
        # | 9 |10 |11 |12 |
        # +---+---+---+---+
        # |13 |14 |15 |   |
        # +---+---+---+---+
        row = ""
        print ("+---+---+---+---+")
        for i, num in enumerate(self.tiles):
            row += "|"
            if num == 0:
                row += "   "
            elif (num < 10) and num != 0:
                row += " " + str(num) + " "
            else:
                row += str(num) + " "
            # row += "|"
            if (i + 1) % 4 == 0:
                row += "|"
                print (row)
                print ("+---+---+---+---+")
                row = ""

        # tiles = [x for x in self.tiles]
        # empty_index = tiles.index(0)
        # tiles[empty_index] = "  "
        # print (f' {tiles[0]}  {tiles[1]}  {tiles[2]}  {tiles[3]} \n {tiles[4]}  {tiles[5]}  {tiles[6]}  {tiles[7]} \n {tiles[8]} {tiles[9]} {tiles[10]} {tiles[11]} \n{tiles[12]} {tiles[13]} {tiles[14]} {tiles[15]} \n')
        
    def __str__(self):
        tiles = [x for x in self.tiles]
        empty_index = tiles.index(0)
        tiles[empty_index] = "  "
        return (f' {tiles[0]}  {tiles[1]}  {tiles[2]}  {tiles[3]} \n {tiles[4]}  {tiles[5]}  {tiles[6]}  {tiles[7]} \n {tiles[8]} {tiles[9]} {tiles[10]} {tiles[11]} \n{tiles[12]} {tiles[13]} {tiles[14]} {tiles[15]} \n')
    

if __name__ == '__main__':

    game = Fifteen()
    print (game.tiles)
    # print (str(game))
    # game.draw()

    assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
    assert game.is_valid_move(15) == True
    assert game.is_valid_move(12) == True
    assert game.is_valid_move(14) == False
    assert game.is_valid_move(1) == False
    game.update(15)
    # game.draw()
    assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14    15 \n'
    game.update(15)
    assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
    assert game.is_solved() == True
    game.shuffle()
    # game.draw()           
    assert str(game) != ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
    assert game.is_solved() == False
    
    game.shuffle()
    game.draw()
    while True:
        move = input('Enter your move or q to quit: ')
        if move == 'q':
            break
        elif not move.isdigit():
            continue
        game.update(int(move))
        game.draw()
        if game.is_solved():
            break
    print('Game over!')

    
    
        
