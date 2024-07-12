# Project : Rock Paper Scissors Game

This is a Python implementation of the classic Rock, Paper, Scissors game. The game allows for different player strategies, including both human and computer-controlled players. The computer players can have various strategies like always playing rock, playing randomly, imitating the opponent's last move, or cycling through the moves.

## Features

- **Player Strategies**:
  - `AlwaysRockPlayer`: Always plays 'rock'.
  - `RandomPlayer`: Chooses moves randomly.
  - `ReflectPlayer`: Imitates the opponent's last move.
  - `CyclePlayer`: Cycles through the moves.

- **Human Player**: Allows a human to input their moves.
- **Score Tracking**: Tracks and displays the score after each round and at the end of the game.
- **Input Validation**: Ensures that user inputs for moves and number of rounds are valid.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Vrana710/ProjectRockPaperScissors-.git
    cd ProjectRockPaperScissors-
    ```

2. Make sure you have Python installed. This project is compatible with Python 3.x.

## Usage

1. Run the game:
    ```sh
    python3 rps.py
    ```

2. Follow the prompts to select player types and input the number of rounds.

3. Play the game by entering your move (if playing as a human) and see the results after each round.

## Example

- Choose the player type for Player 1:
- 0: AlwaysRockPlayer
- 1: RandomPlayer
- 2: ReflectPlayer
- 3: CyclePlayer
- Enter your choice: 1
- Choose the player type for Player 2:
- 0: AlwaysRockPlayer
- 1: RandomPlayer
- 2: ReflectPlayer
- 3: CyclePlayer
- Enter your choice: 0
- Enter the number of rounds to play: 3
- Game start!
- Round 1:
- Player 1: scissors Player 2: rock
- Player 2 wins the round!
- Score: Player 1 - 0, Player 2 - 1
- Round 2:
- Player 1: paper Player 2: rock
- Player 1 wins the round!
- Score: Player 1 - 1, Player 2 - 1
- Round 3:
- Player 1: rock Player 2: rock
- It's a tie!
- Score: Player 1 - 1, Player 2 - 1
- Game over!
- Final Score: Player 1 - 1, Player 2 - 1
- The game is a tie!

## Contributing

Contributions are welcome! If you find a bug or have a feature request, please open an issue. If you want to contribute code, please fork the repository and submit a pull request.

## Acknowledgments

This project was developed as part of the Udacity project for learning Python and implementing object-oriented programming concepts.

---

Feel free to customize this `README.md` file further as needed.
