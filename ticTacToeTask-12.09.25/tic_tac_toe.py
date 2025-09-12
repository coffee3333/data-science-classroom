BOARD = [[" "]*3 for _ in range(3)]

def show():
    print("\n")
    for r in range(3):
        print(" | ".join(BOARD[r]))
        if r < 2: print("--+---+--")
    print()

def winner():
    b = BOARD
    lines = [
        # rows
        (b[0][0], b[0][1], b[0][2]),
        (b[1][0], b[1][1], b[1][2]),
        (b[2][0], b[2][1], b[2][2]),
        # cols
        (b[0][0], b[1][0], b[2][0]),
        (b[0][1], b[1][1], b[2][1]),
        (b[0][2], b[1][2], b[2][2]),
        # diagonals
        (b[0][0], b[1][1], b[2][2]),
        (b[0][2], b[1][1], b[2][0]),
    ]
    for a, c, d in lines:
        if a != " " and a == c == d:
            return a
    return None

def full():
    return all(cell != " " for row in BOARD for cell in row)

def ask_move(player):
    while True:
        try:
            r, c = map(int, input(f"Player {player} (row col 1-3): ").split())
            r -= 1; c -= 1
            if 0 <= r < 3 and 0 <= c < 3 and BOARD[r][c] == " ":
                return r, c
            print("Bad move. Try again.")
        except:
            print("Enter two numbers like: 2 3")

def main():
    turn = "X"
    while True:
        show()
        r, c = ask_move(turn)
        BOARD[r][c] = turn

        w = winner()
        if w:
            show(); print(f"Player {w} wins!")
            break
        if full():
            show(); print("Draw!")
            break

        turn = "O" if turn == "X" else "X"

if __name__ == "__main__":
    main()
