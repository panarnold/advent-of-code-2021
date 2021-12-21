with open('example4.txt') as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]

nums = [int(num) for num in lines[0].split(',')]
lines = lines[1:]
print(nums)
print(lines)

boards = []

lines = filter(lambda a: a != '', lines)

print(lines)


# boards = []
# flags = []

# beg = 2

# while beg + 5 <= len(lines):
#     boards.append([[int(cell) for cell in row.split()] for row in lines[beg:beg+5]])
#     flags.append([[0 for cell in row.split()] for row in lines[beg:beg+5]])
#     beg +=6

# def isBingo(board):
#     for row in board:
#         if row.count(1) == 5:
#             return True
#     for i in range(0, 5):
#         if [row[i] for row in board].count(1) == 5:
#             return True
#     return False

# def calculateBingoScore(board, flag):
#     score = 0
#     for i in range(5):
#         for j in range(5):
#             if flag[i][j] == 0:
#                 score += board[i][j]
#     return score

# winners = []

# for num in nums:
#     for i in range(len(boards)):
#         for row in range(5):
#             for col in range(5):
#                 if boards[i][row][col] == num:



