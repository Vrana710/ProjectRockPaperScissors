import random

# Global moves list
moves = ['rock', 'paper', 'scissors']

def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))

# Base Player class
class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass

# RandomPlayer class
class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)

# HumanPlayer class with input validation
class HumanPlayer(Player):
    def move(self):
        move = input("Enter your move (rock, paper, or scissors): ").lower()
        while move not in moves:
            move = input("Invalid move. Enter your move (rock, paper, or scissors): ").lower()
        return move

# ReflectPlayer class that imitates opponent's last move
class ReflectPlayer(Player):
    def __init__(self):
        self.their_last_move = None

    def move(self):
        if self.their_last_move:
            return self.their_last_move
        else:
            return random.choice(moves)

    def learn(self, my_move, their_move):
        self.their_last_move = their_move

# CyclePlayer class that cycles through moves
class CyclePlayer(Player):
    def __init__(self):
        self.my_last_move = None

    def move(self):
        if self.my_last_move:
            next_move = moves[(moves.index(self.my_last_move) + 1) % len(moves)]
            return next_move
        else:
            return random.choice(moves)

    def learn(self, my_move, their_move):
        self.my_last_move = my_move

# Game class to manage the game
class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.score_p1 = 0
        self.score_p2 = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        if beats(move1, move2):
            print("Player 1 wins the round!")
            self.score_p1 += 1
        elif beats(move2, move1):
            print("Player 2 wins the round!")
            self.score_p2 += 1
        else:
            print("It's a tie!")
        print(f"Score: Player 1 - {self.score_p1}, Player 2 - {self.score_p2}")

    def play_game(self):
        print("Game start!")
        rounds = int(input("Enter the number of rounds to play: "))
        for round in range(rounds):
            print(f"Round {round + 1}:")
            self.play_round()
        print("Game over!")
        if self.score_p1 > self.score_p2:
            print("Player 1 wins the game!")
        elif self.score_p2 > self.score_p1:
            print("Player 2 wins the game!")
        else:
            print("The game is a tie!")

if __name__ == '__main__':
    strategies = [Player(), RandomPlayer(), ReflectPlayer(), CyclePlayer()]
    print("Choose the player type for Player 1:")
    for idx, strategy in enumerate(strategies):
        print(f"{idx}: {strategy.__class__.__name__}")
    p1_choice = int(input("Enter your choice: "))
    p1 = strategies[p1_choice]

    print("Choose the player type for Player 2:")
    for idx, strategy in enumerate(strategies):
        print(f"{idx}: {strategy.__class__.__name__}")
    p2_choice = int(input("Enter your choice: "))
    p2 = strategies[p2_choice]

    game = Game(p1, p2)
    game.play_game()