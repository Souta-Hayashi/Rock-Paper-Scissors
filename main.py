# Rock-Paper-Scissors game
import random

# Starts
def play():
    user = input("Choose 'r' for rock, 'p' for paper and 's' for scissors: ")
    
    if type(user) is int:
        raise Exception("You have to choose 'r', 'p' and 's'.")
    
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return "It's a tie!"

    if is_win(user, computer):
        return "You won!"

    return "You lost!"

# Winning
def is_win(player, bot):
    if (player == 'r' and bot == 's') or (player == 'p' and bot == 'r') or (player == 's' and bot == 'p'):
        return True

print(play())