# -*- coding: utf-8 -*-

from cmath import inf
from typing import List
from players import Player
from actions import *
from board import Board
from math import inf


class AIPlayer(Player):
    """Artificial Intelligence based player"""

    def __init__(self):
        super().__init__("Francis (IA)")
        self.__maxdepth = 6 #mettez ici la profondeur max de votre alpha beta en n'oubliant que vous devez répondre en 10s)

    def getNextMove(self, board: Board) -> Action:
        """Gets the next move to play"""
        return self.alphabeta(board)

    def heuristic(self, board:Board) -> float:
        """Heuristic for alpha-beta, to be modified by the students"""
        if board.getTop() == self.player or board.getMarbleCount(-self.player) == 0:
            return inf
        elif board.getTop() == -self.player or board.getMarbleCount(self.player) == 0:
            return -inf
        else:
            
            def compute_square_score(square):
                """Take a list of 4 cells and returns a list of 2 variables:
                • first number_of_marbles which equals to 0 if the square cannot be completed by only one-player marbles.
                If it can be, then it equals to the number of marbles already in the square with a minus sign
                if it is other player marbles. If the square is already complete;
                • The second variable is 1 if it a full square of the player, -1 if it is as full square of the other player 
                and 0 in other case."""
                nonlocal self
                cell_values = {0}
                number_of_marbles = 0
                i = 0
                while i < 4:
                    cell_values.add(square[i])
                    if len(cell_values) == 3:
                        return 0, 0
                    else:
                        number_of_marbles += square[i]*self.player
                        i += 1
                if number_of_marbles == 4 or number_of_marbles == -4:
                    return 0, (number_of_marbles//4)
                else:
                    return number_of_marbles, 0

            possible_square_score = 0
            square_score = 0
            for h in range(3): 
                for i in range(4 - h - 1):
                    for j in range(4 - h - 1):
                        if board.getCell(h + 1, i, j) == 0:
                            possible_square_score_to_add, square_score_to_add = compute_square_score([board.getCell(h, i, j), board.getCell(h, i, j + 1), board.getCell(h, i + 1, j), board.getCell(h, i + 1, j + 1)])
                            possible_square_score += possible_square_score_to_add
                            square_score += square_score_to_add

            move_score = 0
            for h in range(3):
                for i in range(4 - h):
                    for j in range(4 - h):
                        if Action._canBeMoved(board, h, i, j):
                            move_score += self.player*board.getCell(h, i, j)
            
            return 5*(board.getMarbleCount(self.player) - board.getMarbleCount(-self.player)) + 9*square_score + 2*possible_square_score + move_score

    def sortmoves(self, actionlist: List[Action]) -> List[Action]:
        """Sort the moves"""

        # Je n'ai pas le droit de mettre le plateau en argument, ce qui est dommage. Sinon je l'avais j'aurais fait ceci.

        # def future_square_indicator(square):
        #         """Return True if it a square that can be completed by only one player and 
        #         has already 2 or 3 marbles."""
        #         nonlocal self
        #         cell_values = {0}
        #         number_of_marbles = 0
        #         i = 0
        #         while i < 4:
        #             cell_values.add(square[i])
        #             if len(cell_values) == 3:
        #                 return False
        #             else:
        #                 number_of_marbles += square[i]
        #                 i += 1
        #         if number_of_marbles == 2 or number_of_marbles == 3:
        #             return True
        #         else:
        #             return False

        # future_square_moves = []

        # for h in range(3): 
        #     for i in range(4 - h - 1):
        #         for j in range(4 - h - 1):
        #             if board.getCell(h + 1, i, j) == 0 and future_square_indicator([board.getCell(h, i, j), board.getCell(h, i, j + 1), board.getCell(h, i + 1, j), board.getCell(h, i + 1, j + 1)]):
        #                 future_square_moves.append("-> Niv:%i, li:%i, col:%i"%(h, i, j))


        # future_square_actions = []
        add_marble_often_good_actions = []
        make_square_actions = []
        move_marble_actions = []
        other_actions = []

        for action in actionlist:
            if str(action) == "-> Niv:0, li:1, col:1" \
                or str(action) == "-> Niv:0, li:1, col:2" \
                or str(action) == "-> Niv:0, li:2, col:1" \
                or str(action) == "-> Niv:0, li:2, col:2" \
                or str(action) == "-> Niv:1, li:1, col:1":
                add_marble_often_good_actions.append(action)
            elif str(action)[0:4] == "Niv:":
                move_marble_actions.append(action)
            elif str(action)[0:4] == "Make":
                make_square_actions.append(action)
            else:
                other_actions.append(action)

        return make_square_actions + move_marble_actions + add_marble_often_good_actions + other_actions


    def alphabeta(self, board:Board) -> Action:
        """Decision made by alpha beta, returns the best action"""
        possiblemoves = self.sortmoves(Player.getPossibleMoves(self.player, board))
        if len(possiblemoves)==0:
            raise Exception("cannot have 0 possible play")
        elif len(possiblemoves)==1:
            return possiblemoves[0]
        else:
            best_score = -inf
            beta = inf
            coup = None
            for action in possiblemoves:
                action.apply(self.player, board)
                v = self.__minvalue(board, best_score, beta, 1)
                action.unapply(self.player, board)
                if v>best_score:
                    best_score = v
                    coup = action

            if coup == None:
                #we are going towards a defeat whatever the coup
                coup = possiblemoves[0]
            return coup

    def __maxvalue(self, board:Board, alpha:float, beta:float, depth:int) -> float:
        """For max nodes"""
        #terminal test
        if depth >= self.__maxdepth or board.isTerminal():
            return self.heuristic(board)
            
        v = -inf
        for action in Player.getPossibleMoves(self.player, board):            
            action.apply(self.player, board)
            v = max(v, self.__minvalue(board, alpha, beta, depth+1))
            action.unapply(self.player, board)
            if v>=beta:
                return v
            alpha = max(alpha,v)
        return v

    def __minvalue(self, board:Board, alpha:float, beta:float, depth:int) -> float:
        """For min nodes"""
        #terminal test
        if depth >= self.__maxdepth or board.isTerminal():
            return self.heuristic(board)
            
        v = inf
        for action in Player.getPossibleMoves(-self.player,board):
            action.apply(-self.player, board)
            v = min(v, self.__maxvalue(board, alpha, beta, depth+1))
            action.unapply(-self.player, board)
            if v<=alpha:
                return v
            beta = min(beta,v)
        return v

