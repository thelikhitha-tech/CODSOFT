import math

# Initialize the board
board = [" " for _ in range(9)]

# Print the board
def print_board():
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print("| " + " | ".join(row) + " |")

# Check for winner
def is_winner(player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    return any(all(board[i] == player for i in combo) for combo in win_conditions)

# Check for tie
def is_board_full():
    return " " not in board

# Get valid moves
def get_valid_moves():
    return [i for i in range(9) if board[i] == " "]

# Minimax algorithm
def minimax(is_maximizing):
    if is_winner("O"): return 1
    if is_winner("X"): return -1
    if is_board_full(): return 0

    if is_maximizing:
        best_score = -math.inf
        for move in get_valid_moves():
            board[move] = "O"
            score = minimax(False)
            board[move] = " "
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for move in get_valid_moves():
            board[move] = "X"
            score = minimax(True)
            board[move] = " "
            best_score = min(score, best_score)
        return best_score

# Best move for AI
def best_move():
    best_score = -math.inf
    move = None
    for i in get_valid_moves():
        board[i] = "O"
        score = minimax(False)
        board[i] = " "
        if score > best_score:
            best_score = score
            move = i
    board[move] = "O"

# Main game loop
def play_game():
    print("Welcome to Tic-Tac-Toe!")
    print_board()

    while True:
        # Human move
        try:
            move = int(input("Enter your move (0-8): "))
        except ValueError:
            print("Invalid input.")
            continue
        if board[move] != " ":
            print("Invalid move. Try again.")
            continue
        board[move] = "X"

        print_board()
        if is_winner("X"):
            print("You win!")
            break
        if is_board_full():
            print("It's a tie!")
            break

        # AI move
        best_move()
        print("AI has made its move:")
        print_board()
        if is_winner("O"):
            print("AI wins!")
            break
        if is_board_full():
            print("It's a tie!")
            break

# Run the game
if __name__ == "__main__":
    play_game()