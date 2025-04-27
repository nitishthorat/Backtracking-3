'''
    Time Complexity: O(m*n)
    Space Complexity: O(m*n)
'''
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        for i in range(m):
            for j in range(n):
                if self.helper(board, i, j, m, n, directions, word, 0):
                    return True

        return False

    def helper(self, board, i, j, m, n, directions, word, k):
        # base case
        if board[i][j] != word[k]:
            return False
        if k == len(word) - 1:
            return True

        # logic
        letter = board[i][j]
        board[i][j] = "0"
        for dir in directions:
            r = i + dir[0]
            c = j + dir[1]

            if 0 <= r < m and 0 <= c < n and board[r][c] != "0":
                if self.helper(board, r, c, m, n, directions, word, k+1):
                    board[i][j] = letter
                    return True

        board[i][j] = letter
        return False