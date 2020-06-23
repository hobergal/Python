#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 14:15:07 2020

@author: alyxandrahoberg
"""

board = {'1': ' ', '2': ' ', '3': ' ', #dictionary
         '4': ' ', '5': ' ', '6': ' ',
         '7': ' ', '8': ' ', '9': ' '}

turn = 'X'

def drawBoard(board):

    print('   |   |')
    print(' ' + board['7'] + ' | ' + board['8'] + ' | ' + board['9'])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board['4'] + ' | ' + board['5'] + ' | ' + board['6'])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board['1'] + ' | ' + board['2'] + ' | ' + board['3'])
    print('   |   |')


def isWinner(bo, le):
    # Given a board and a player's letter, this function returns True if that player has won.
    # Use bo instead of board and le instead of letter 
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top
    (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle
    (bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom
    (bo[7] == le and bo[4] == le and bo[1] == le) or # down the left side
    (bo[8] == le and bo[5] == le and bo[2] == le) or # down the middle
    (bo[9] == le and bo[6] == le and bo[3] == le) or # down the right side
    (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
    (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal


def isSpaceFree(board, move):
    return board[move] == ' '


def isBoardFull(board):
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True

# starting game 
    
print('Welcome to Tic Tac Toe!')
input("Press ENTER to begin")

while True:
    for i in range(9):
        drawBoard(board)
        print(board)
        print('The ' + turn + ' will go first.')
        move = input()
        board[move] = turn
        if isWinner(board, turn) == True:
           drawBoard(board)
           print("No more moves left! You won!")
        else:
           if isBoardFull(board):
                drawBoard(board)
                print('The game is a tie!')
                break
        if turn == 'X':
           turn = 'O'
        else: 
           turn = 'X'
       
        

