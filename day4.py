from functools import reduce

def getNumbers(data):
    return [int(x) for x in data[0].split(",")]

def getBoards(data):
    boards = []
    currentBoard = []
    for line in data[2:]:
        if not line:
            boards.append(currentBoard)
            currentBoard = []
            continue
        currentBoard.append([int(x) for x in line.split()])
    boards.append(currentBoard)
    return boards


def markBoards(number, boards, marked, winners):
    winner_temp = []
    for i in range(len(boards)):
        for j in range(5):
            for k in range(5):
                if boards[i][j][k] == number:
                    marked[i][j][k] = True
                    if i not in winners and (reduce((lambda x, y: x and y), getRow(marked[i], k)) or reduce((lambda x, y: x and y), marked[i][j])):
                        winner_temp.append(i)
    return winner_temp

def sol1(data):
    numbers = getNumbers(data)
    boards = getBoards(data)
    marked = [[[False] * 5 for _ in range(5)] for _ in range(len(boards))]
    winningBoard = []
    winningNum = -1
    for num in numbers:
        winningBoard = markBoards(num, boards, marked, set())
        if winningBoard:
            winningNum = num
            break
    sumUnmarked = 0
    for j in range(5):
        for k in range(5):
            if not marked[winningBoard[0]][j][k]:
                sumUnmarked += boards[winningBoard[0]][j][k]
    return sumUnmarked * winningNum

def sol2(data):
    numbers = getNumbers(data)
    boards = getBoards(data)
    marked = [[[False] * 5 for _ in range(5)] for _ in range(len(boards))]
    winners = set()
    winning_order = []
    winningBoard = -1
    winningNum = -1
    for num in numbers:
        winningBoard = markBoards(num, boards, marked, winners)
        [winners.add(w) for w in winningBoard]
        winning_order.extend(winningBoard)
        if len(winning_order) == len(numbers):
            winningNum = num
            break
    sumUnmarked = 0
    for j in range(5):
        for k in range(5):
            if not marked[winning_order[-1]][j][k]:
                sumUnmarked += boards[winning_order[-1]][j][k]
    return sumUnmarked * winningNum

def getRow(twoDArray, i):
    return [row[i] for row in twoDArray]



if __name__ == '__main__':
    with open("./inputs/day4") as file:
        data = [line.strip() for line in file]

    print(sol1(data))
    print(sol2(data))
