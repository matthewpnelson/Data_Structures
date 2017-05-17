# Assignment 3, Data Structures and Algorithms
# Matthew Nelson
# December 29, 2016

# Create Multiple Classes to play a specific Marble Game

import sys
import timeit


class MarblesBoard():

    def __init__(self, board):
        '''Initializes an instance of class MarblesBoard.'''

        self.length = len(board)
        self.ordered_board = [i for i in range(0,self.length)]

        # check quality of inputs before setting board attribute
        i = 0
        while i < self.length:
            if board[i] not in self.ordered_board:
                raise Exception("Please re-enter your marble sequence with marbles from 0 to N-1 only.")
            if board[i] in board[0:i]:
                raise Exception("Please ensure no duplicate marble numbers are entered.")
            i += 1
        self.board = list(board)

    def __str__(self):
        current = ""
        for each in self.board:
            current += str(each) + " "
        return current

    def __repr__(self):
        current = ""
        for each in self.board:
            current += str(each) + " "
        return current
        #return "<MarblesBoard({})>".format(current)

    # Specify __len__ special method for inherited classes
    def __len__(self):
        return len(self.board)

    # Main Marble Move #1
    def switch(self):
        '''Switches the marbles in positions 0 and 1.'''
        self.board[0] , self.board[1] = self.board[1] , self.board[0]
        return print(self)

    # Main Marble Move #2
    def rotate(self):
        '''Moves the marbles in position 0 to position N-1 and moves all other marbles one
        space to the left (one index lower).'''
        hover = self.board[0]
        i = 0
        while i < self.length-1:
            self.board[i] = self.board[i+1]
            i += 1
        self.board[-1] = hover
        return print(self)

    def is_solved(self):
        '''Call to determine if the marbles are in the correct order.'''
        i=0
        while i < self.length:
            if self.board[i] != self.ordered_board[i]:
                return False
                break
            else:
                i += 1
        return True


class Solver(MarblesBoard):

    def __init__(self,board_input):

        self.board = board_input.board
        self.length = len(board_input.board)
        self.ordered_board = [i for i in range(0,self.length)]

    def solve(self):
        print(self)
        steps = 0
        while self.is_solved() == False:
            if self.board[0] != 0 and self.board[1] != 0 and self.board[0] >= self.board[1]:
                self.switch()
            else:
                self.rotate()
            steps += 1
        return print("total steps: " + str(steps))


# Run the program using command line inputs
user_input = [int(i) for i in str(sys.argv[1:][0]).split(",")]

board = MarblesBoard(user_input)
player = Solver(board)
player.solve()



# Big O Running Time
## Running Time Results (completed in Jupyter Notebook also attached)

# N = 4, Best Time = 0.172ms
# N = 8, Best Time = 1400ms
# N = 12, Best Time = 5270ms
# N = 16, Best Time = 9980ms
#
# This algorithm appears to be increasing as Big O (N^3). Not very good...
