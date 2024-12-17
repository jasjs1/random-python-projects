import random
import time
import os

game_status = True
score = 0

def play():
    os.system('cls' if os.name == 'nt' else 'clear')
    global score
    print("\nWelcome to Rock Paper Scissors.")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

    user_choice = input("Choose 1, 2, or 3: ")

    if user_choice not in ['1', '2', '3']:
        print("Invalid input, must choose from 1, 2, or 3.")
        return

    user_choice = int(user_choice)
    ai_choice = random.randint(1, 3)

    moves = {1: "Rock", 2: "Paper", 3: "Scissors"}

    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"You've chosen: {moves[user_choice]}")
    time.sleep(0.5)
    print(f"The computer has chosen: {moves[ai_choice]}")

    if user_choice == ai_choice:
        print(f"TIE, no winner.\nYour score: {score}")
    elif (user_choice == 1 and ai_choice == 3) or \
         (user_choice == 2 and ai_choice == 1) or \
         (user_choice == 3 and ai_choice == 2):
        score += 1
        print(f"You win! Your score: {score}")
    else:
        print(f"You lost. Your score: {score}")

while game_status:
    
    player_rank = ""
    
    play()
    again_input = input("New game? (Y/N): ").strip().lower()
    
    if again_input != "y":
        game_status = False
        os.system('cls' if os.name == 'nt' else 'clear')
        
        if score <= 5:
            player_rank = "beginner"
        elif score >= 10:
            player_rank = "intermediate"
        elif score > 20:
            player_rank = "pro"
        elif score >= 100:
            player_rank = "expert in the field."
            
        print(f"The game has ended. You're final score: {score}. You are ranked as a {player_rank} on our player ranking system.")
