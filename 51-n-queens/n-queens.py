class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = []
        for row in range(n):
            column = []
            for col in range(n):
                column.append(".")

            board.append(column)


        def conflictCheck(row, col, board):
            def lengthCheck(row, col):
                while row >= 0:
                    if board[row][col] == "Q":
                        return False
                    row-=1

                return True


            def colCheck(row, col):
                while col >= 0:
                    if board[row][col] == "Q":
                        return False
                    col-=1

                return True

            def diagnolCheck(row, col):
                curRow, curCol = row, col
                while curRow >= 0 and curCol >= 0:
                    if board[curRow][curCol] == "Q":
                        return False

                    curRow-=1
                    curCol-=1

                curRow, curCol = row, col
                while curRow >= 0 and curCol < n:
                    if board[curRow][curCol] == "Q":
                        return False

                    curRow -= 1
                    curCol+=1

                return True
            
            if lengthCheck(row, col) and colCheck(row, col) and diagnolCheck(row, col):
                return True

            return False


        def backtracking(row, board):
            
            if row == n:
                currRes = []
                for row in board:
                    currRes.append(''.join(row))
                res.append(currRes)
                return


            for col in range(0, n):
                if conflictCheck(row, col, board) == True:
                    board[row][col] = "Q"
                    backtracking(row+1, board)
                    board[row][col] = "."

                


        res = []
        backtracking(0, board)
        return res


        