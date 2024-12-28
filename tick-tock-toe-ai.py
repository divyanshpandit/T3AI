import os
import random
import json

GAME_STATE_FILE = "game_state.txt"
Q_TABLE_FILE = "q_table.json"


def display_board(board):
    print("\nCurrent Board:")
    for i in range(3):
        print(" | ".join(board[i]))
        if i < 2:
            print("---+---+---")


def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != "-":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != "-":
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != "-":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != "-":
        return board[0][2]
    return None


def save_game(board, turn, mode):
    with open(GAME_STATE_FILE, "w") as file:
        for row in board:
            file.write(",".join(row) + "\n")
        file.write(f"Player Turn: {turn}\n")
        file.write(f"Mode: {mode}\n")
    print("\nGame state automatically saved!")


def load_game():
    if not os.path.exists(GAME_STATE_FILE):
        print("No saved game found.")
        return None, None, None
    with open(GAME_STATE_FILE, "r") as file:
        lines = file.readlines()
        board = [line.strip().split(",") for line in lines[:3]]
        turn = int(lines[3].split(":")[1].strip())
        mode = lines[4].split(":")[1].strip()
    print("\nGame state loaded!")
    return board, turn, mode


def ai_simple_move(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == "-":
                return i, j


def board_to_state(board):
    return "".join(["".join(row) for row in board])


def reward_learning_ai_move(board, q_table, epsilon=0.1):
    state = board_to_state(board)
    if state not in q_table:
        q_table[state] = {move: 0 for move in range(9) if board[move // 3][move % 3] == "-"}
    if random.random() < epsilon:
        move = random.choice(list(q_table[state].keys()))
    else:
        move = max(q_table[state], key=q_table[state].get)
    move = int(move)
    return divmod(move, 3), state, move


def update_q_table(q_table, prev_state, move, reward, next_board, alpha=0.1, gamma=0.9):
    next_state = board_to_state(next_board)
    if next_state not in q_table:
        q_table[next_state] = {m: 0 for m in range(9) if next_board[m // 3][m % 3] == "-"}
    if prev_state not in q_table:
        q_table[prev_state] = {m: 0 for m in range(9)}
    if move not in q_table[prev_state]:
        q_table[prev_state][move] = 0
    max_future_q = max(q_table[next_state].values(), default=0)
    q_table[prev_state][move] += alpha * (reward + gamma * max_future_q - q_table[prev_state][move])


def load_q_table():
    if os.path.exists(Q_TABLE_FILE):
        with open(Q_TABLE_FILE, "r") as file:
            return json.load(file)
    return {}


def save_q_table(q_table):
    with open(Q_TABLE_FILE, "w") as file:
        json.dump(q_table, file)
    print("\nQ-table saved!")


def main():
    print("Welcome to Tic Tac Toe!")
    print("Player 1: X\nPlayer 2: O\n")
    q_table = load_q_table()

    if input("Do you want to load a saved game? (yes/no): ").lower() == "yes":
        board, turn, mode = load_game()
        if board is None:
            board = [["-" for _ in range(3)] for _ in range(3)]
            turn = 1
            mode = "1"
    else:
        board = [["-" for _ in range(3)] for _ in range(3)]
        turn = 1
        print("Choose Game Mode:")
        print("1. Player vs Player")
        print("2. Player vs Simple AI")
        print("3. Player vs Reward Learning AI")
        mode = input("Enter 1, 2, or 3: ").strip()

    prev_state, prev_move = None, None

    while True:
        display_board(board)

        if mode == "2" and turn == 2:
            print("Simple AI is making its move...")
            row, col = ai_simple_move(board)
        elif mode == "3" and turn == 2:
            print("Reward Learning AI is making its move...")
            (row, col), prev_state, prev_move = reward_learning_ai_move(board, q_table)
        else:
            print(f"Player {turn}, enter your move (1-9): ", end="")
            try:
                move = int(input().strip()) - 1
                if move < 0 or move >= 9:
                    raise ValueError("Move out of range.")
                row, col = divmod(move, 3)
                if board[row][col] != "-":
                    print("Cell already occupied. Try again.")
                    continue
            except ValueError:
                print("Invalid input. Try again.")
                continue

        board[row][col] = "X" if turn == 1 else "O"
        save_game(board, turn, mode)

        winner = check_winner(board)
        if winner:
            display_board(board)
            print(f"\n{'Player' if (mode == '1' or turn == 1) else 'AI'} {turn} ({winner}) wins!")
            if mode == "3" and turn == 2:
                update_q_table(q_table, prev_state, prev_move, 1, board)
            break

        if all(cell != "-" for row in board for cell in row):
            display_board(board)
            print("\nIt's a draw!")
            if mode == "3" and prev_state:
                update_q_table(q_table, prev_state, prev_move, 0.5, board)
            break

        if mode == "3" and prev_state:
            update_q_table(q_table, prev_state, prev_move, 0, board)

        turn = 3 - turn

    if mode == "3":
        save_q_table(q_table)


if __name__ == "__main__":
    main()
