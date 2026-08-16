import random

# Create an empty board
board = [" " for _ in range(9)]


# Display the board
def print_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])


# Get player's move
def player_move():
    while True:
        try:
            move = int(input("Enter your move (1-9): "))

            if 1 <= move <= 9:
                if board[move - 1] == " ":
                    board[move - 1] = "X"
                    break
                else:
                    print("That position is already taken.")
            else:
                print("Please enter a number between 1 and 9.")

        except ValueError:
            print("Please enter a number.")


# Get AI's move
def ai_move():
    empty_positions = []

    for i in range(9):
        if board[i] == " ":
            empty_positions.append(i)

    if empty_positions:
        move = random.choice(empty_positions)
        board[move] = "O"


# Check whether a player has won
def check_winner(player):
    winning_combinations = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    for combination in winning_combinations:
        if (
            board[combination[0]] == player
            and board[combination[1]] == player
            and board[combination[2]] == player
        ):
            return True

    return False


# Check whether the board is full
def is_draw():
    return " " not in board


# Start the game
print("Tic-Tac-Toe")
print("You are X")
print("AI is O")

print_board()

while True:

    # Player's turn
    player_move()
    print_board()

    if check_winner("X"):
        print("You win! 🎉")
        break

    if is_draw():
        print("It's a draw!")
        break

    # AI's turn
    ai_move()
    print("AI's move:")
    print_board()

    if check_winner("O"):
        print("AI wins!")
        break

    if is_draw():
        print("It's a draw!")
        break
