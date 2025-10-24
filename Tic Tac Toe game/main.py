# Advanced Tic Tac Toe Game (2-Player Console Version)

def print_board(board):
    print("\n")
    print("   1   2   3")
    for i, row in enumerate(board):
        print(f"{i + 1}  " + " | ".join(row))
        if i < 2:
            print("  ---+---+---")
    print("\n")


def check_winner(board, player):
    # All possible win combinations: rows, columns, diagonals
    win_states = (
        [row for row in board] +  # rows
        [[board[r][c] for r in range(3)] for c in range(3)] +  # columns
        [[board[i][i] for i in range(3)]] +  # diagonal top-left to bottom-right
        [[board[i][2 - i] for i in range(3)]]  # diagonal top-right to bottom-left
    )
    return [player] * 3 in win_states


def is_draw(board):
    # If all cells are filled and no winner
    return all(cell != ' ' for row in board for cell in row)


def get_move(player, board):
    while True:
        try:
            move = input(f"Player {player} - Enter your move as row and column (e.g., 1 3): ")
            row, col = map(int, move.strip().split())
            if row not in [1, 2, 3] or col not in [1, 2, 3]:
                print("❌ Row and column must be between 1 and 3. Try again.")
                continue
            if board[row - 1][col - 1] == ' ':
                return row - 1, col - 1
            else:
                print("❌ Cell is already taken. Choose a different spot.")
        except (ValueError, IndexError):
            print("❌ Invalid format. Please enter two numbers separated by a space (e.g., 2 3).")


def play_game():
    board = [[' '] * 3 for _ in range(3)]
    current_player = 'X'
    print("\n🎮 Welcome to Advanced Tic Tac Toe!")
    print("🕹️  Player X and Player O will take turns to play.")
    print_board(board)

    while True:
        row, col = get_move(current_player, board)
        board[row][col] = current_player
        print_board(board)

        if check_winner(board, current_player):
            print(f"🏆 Player {current_player} wins! Congratulations!")
            break
        elif is_draw(board):
            print("🤝 It's a draw! Great game.")
            break

        current_player = 'O' if current_player == 'X' else 'X'

    print("✅ Game Over. Thanks for playing!")


if __name__ == "__main__":
    play_game()
