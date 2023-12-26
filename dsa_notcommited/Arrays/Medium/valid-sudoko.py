# https://leetcode.com/problems/valid-sudoku/

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # for i in range(len(board)):
        #     hashmap = defaultdict(int)
        #     for j in range(len(board[i])):
        #         if board[i][j] != '.' and hashmap[board[i][j]]:
        #             return False
        #         hashmap[board[i][j]] += 1

        # for i in range(len(board)):
        #     hashmap = defaultdict(int)
        #     for j in range(len(board[j])):
        #         if board[j][i] != '.' and hashmap[board[j][i]]:
        #             return False
        #         hashmap[board[j][i]] += 1

        # hashmaps = [[defaultdict(int)] * 3] * 3
        # for i in range(0, len(board)):
        #     for j in range(0, len(board[j])):
        #         hashmap = hashmaps[int(i / 3)][int(j / 3)]
        #         if board[i][j] != '.' and hashmap[board[i][j]]:
        #             return False
        #         hashmap[board[i][j]] += 1

        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == ".":
                    continue
                if (board[i][j] in rows[i]) or (board[i][j] in cols[j]) or (board[i][j] in squares[(i // 3, j // 3)]):
                    return False
                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                squares[(i // 3, j // 3)].add(board[i][j])

        return True