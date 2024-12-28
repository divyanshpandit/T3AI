Tic Tac Toe with AI 🕹️🤖
A feature-rich Tic Tac Toe game implemented in Python. This game includes multiple modes, including a reward-learning AI that learns from its gameplay to improve its strategy over time. Save your game state, challenge a friend, or test your skills against a learning AI.

Features

Player vs Player Mode: Play Tic Tac Toe with a friend.

Player vs Simple AI Mode: Compete against a basic AI that makes logical moves.

Player vs Reward Learning AI Mode: Challenge an AI that uses Q-learning to improve its decisions.

Game Saving and Loading: Save your progress and resume from where you left off.

Q-Table Persistence: The learning AI retains its knowledge across sessions by saving its Q-table.

How It Works


Simple AI: Scans the board for the first available move.

Reward Learning AI:

Utilizes Q-learning to associate board states with moves.

Learns through exploration (random moves) and exploitation (optimal moves).

Updates its Q-table based on rewards for wins, losses, and draws.

Files

game_state.txt: Saves the current game state for resuming later.

q_table.json: Stores the Q-learning AI's knowledge for future use.

Installation


Clone the repository:

bash

Copy code

git clone https://github.com/divyanshpandiit/T3AI.git

cd tic-toc-toe-ai

Make sure Python 3 is installed on your system.

Run the program:


bash

Copy code

python tic_tac_toe.py

How to Play


Start the game by running tic_tac_toe.py.

Choose whether to load a saved game or start a new one.

Select your game mode:

1: Player vs Player

2: Player vs Simple AI

3: Player vs Reward Learning AI

Follow the prompts to make moves or let the AI play.

The game ends when there’s a winner or a draw. Results are displayed at the end.
Controls

Input your move as a number between 1-9:


diff

Copy code

1 | 2 | 3

---+---+---

4 | 5 | 6

---+---+---

7 | 8 | 9

Q-Learning Parameters

Alpha (Learning Rate): 0.1

Gamma (Discount Factor): 0.9

Epsilon (Exploration Rate): 0.1

These parameters can be modified in the reward_learning_ai_move and update_q_table functions.


Contributing

Contributions are welcome! Feel free to submit issues or pull requests for new features, bug fixes, or optimizations.


License

This project is open-source and available under the MIT License.


