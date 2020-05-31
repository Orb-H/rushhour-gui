def solve(board_start):  # board format in a 2-dimensional list of cells
    visited = set()  # visited board state
    queue = []  # BFS queue

    queue.append((board_start, ''))

    while len(queue) > 0:
        board, path = queue.pop(0)
        if stringify_board(board) in visited:
            continue
        if board[2][5] == 'X':
            return path
        visited.add(stringify_board(board))

        checked = set()  # checked car symbols
        for i in range(6):
            for j in range(6):
                if board[i][j] != '.' and board[i][j] not in checked:
                    checked.add(board[i][j])
                    direction = None
                    length = 1

                    # check if horizontal car
                    if j != 5 and board[i][j + 1] == board[i][j]:
                        direction = 0
                        # check if horizontal truck
                        length = 3 if j != 4 and board[i][
                            j + 2] == board[i][j] else 2
                    # check if vertical car
                    elif i != 5 and board[i + 1][j] == board[i][j]:
                        direction = 1
                        # check if vertical truck
                        length = 3 if i != 4 and board[
                            i + 2][j] == board[i][j] else 2

                    # board without moving cars
                    new_board = [[
                        board[y][x] if board[y][x] != board[i][j] else '.'
                        for x in range(6)
                    ] for y in range(6)]
                    if direction == 0:  # for horizontal vehicles
                        for k in range(j - 1, -1, -1):
                            # check left moving, k meaning left end
                            if board[i][k] != '.':
                                break
                            next_board = [[new_board[y][x] for x in range(6)]
                                          for y in range(6)]
                            for l in range(k, k + length):
                                next_board[i][l] = board[i][j]
                            queue.append(
                                (next_board, path +
                                 "{}L{} ".format(board[i][j], str(j - k))))
                        for k in range(j + length, 6):
                            # check right moving, k meaning right end
                            if board[i][k] != '.':
                                break
                            next_board = [[new_board[y][x] for x in range(6)]
                                          for y in range(6)]
                            for l in range(k, k - length, -1):
                                next_board[i][l] = board[i][j]
                            queue.append((next_board, path + "{}R{} ".format(
                                board[i][j], str(k - length - j + 1))))
                    elif direction == 1:  # for vertical vehicles
                        for k in range(i - 1, -1, -1):
                            # check up moving, k meaning up end
                            if board[k][j] != '.':
                                break
                            next_board = [[new_board[y][x] for x in range(6)]
                                          for y in range(6)]
                            for l in range(k, k + length):
                                next_board[l][j] = board[i][j]
                            queue.append(
                                (next_board, path +
                                 "{}U{} ".format(board[i][j], str(i - k))))
                        for k in range(i + length, 6):
                            # check down moving, k meaning down end
                            if board[k][j] != '.':
                                break
                            next_board = [[new_board[y][x] for x in range(6)]
                                          for y in range(6)]
                            for l in range(k, k - length, -1):
                                next_board[l][j] = board[i][j]
                            queue.append((next_board, path + "{}D{} ".format(
                                board[i][j], str(k - length - i + 1))))


def stringify_board(board, l=6):  # collapse board into a short string
    return ''.join(''.join(board[x]) for x in range(l))


def format_board(board, l=6):  # change board to a list of string
    return '\n'.join(' '.join(board[x]) for x in range(l))


if __name__ == "__main__":
    board_str = input(
        "Enter cars and trucks in a format of (car symbol):(x-coordinate),(y-coordinate),(direction) separated by space. ex) X:2,3,x A:1,4,y\n"
    )
    board = [['.'] * 6 for x in range(6)]
    for s in board_str.split(" "):
        t = s.split(":")
        x, y, d = t[1].split(",")
        x, y = int(x), int(y)
        board[y - 1][x - 1] = t[0]
        if d == 'x':
            board[y - 1][x] = t[0]
            if ord(t[0]) >= ord('O') and ord(t[0]) <= ord('R'):
                board[y - 1][x + 1] = t[0]
        elif d == 'y':
            board[y][x - 1] = t[0]
            if ord(t[0]) >= ord('O') and ord(t[0]) <= ord('R'):
                board[y + 1][x - 1] = t[0]
        else:
            raise SyntaxError("wrong direction: " + d)
    print("Answer: {}".format(solve(board)))