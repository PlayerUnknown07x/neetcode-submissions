class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = {i:set() for i in range(9)}
        col_set = {i:set() for i in range(9)}
        sub_set = {i:set() for i in range(9)}

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                sub_index = (i // 3) * 3 + (j // 3)
                if int(board[i][j]) in row_set[i] or int(board[i][j]) in col_set[j] or int(board[i][j]) in sub_set[sub_index]:
                    return False
                row_set[i].add(int(board[i][j]))
                col_set[j].add(int(board[i][j]))
                sub_set[sub_index].add(int(board[i][j]))
        return True
