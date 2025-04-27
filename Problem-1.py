'''
    Time Complexity: O(n!)
    Space Complexity: O(n^2)
'''

import copy

class Solution:
    def __init__(self):
        self.board = []
        self.result = []

    def solveNQueens(self, n: int) -> List[List[str]]:
        self.board = [["." for j in range(n)] for i in range(n)]
        self.helper(0, n)
        return self.result

    def helper(self, row, n):
        # base case
        if row == n:
            return

        # logic
        for col in range(n):
            if self.checkValidPosition(row, col, n):
                self.board[row][col] = "Q"
                if row == n-1:
                    solution = copy.deepcopy(self.board)
                    self.result.append(self.modifySolution(self.board, n))
                else:
                    self.helper(row+1, n)
                self.board[row][col] = "."

    def checkValidPosition(self, row, col, n):
        for i in range(row, -1, -1):
            diff = row - i

            isPresentVertical = self.board[i][col] == "Q"
            isPresentLeftDiagonal = self.board[i][col-diff] == "Q" if col-diff >= 0 else False
            isPresentRightDiagonal = self.board[i][col+diff] == "Q" if col+diff < n else False
            
            if isPresentVertical or isPresentLeftDiagonal or isPresentRightDiagonal:
                return False

        return True

    def modifySolution(self, solution, n):
        modifiedSolution = []

        for i in range(n):
            row = ""
            for j in range(n):
                row += solution[i][j]

            modifiedSolution.append(row)

        return modifiedSolution