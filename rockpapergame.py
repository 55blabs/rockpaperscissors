import random

player1 = 0 
player2 = 0

#the print statement prints the information above 
print("Three points will the game! ")

#this while block will contain the contents of the conditional
#statements needed to play the game
while player1 < 3 and player2 < 3:
    player2_choice = random.choice(["rock", "paper", "scissors"])
    player1_choice = input("Rock, Paper, or Scissors: ")
    
    print(f"Player2: {player2_choice} VS Player: {player1_choice}")
    
    if player1_choice.lower() == player2_choice:
        print("You are Tied! No points Awarded")
    elif player1_choice.lower() == "rock":
        if player2_choice == "scissors":
            player1 += 1
            print(f"Player wins!")
        elif player2_choice == "paper":
            player2 += 1
            print("Player 2 Wins! Point Awarded")
            
    elif player1_choice.lower() == "scissors":
        if player2_choice == "paper":
            player1 += 1
            print(f"Player wins!")
        elif player2_choice == "rock":
            player2 += 1
            print("Player 2 Wins! Point Awarded")
            
        elif player1_choice.lower() == "paper":
            if player2_choice == "rock":
                player1 += 1
            print(f"Player wins!")
        elif player2_choice == "scissors":
            player2 += 1
            print("Player 2 Wins! Point Awarded")
            
    else:
        print("Invalid input! New Round Available!")

print ("Player Wins! " if player1> player2 else "Player 2 Wins! ")

