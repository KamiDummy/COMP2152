import random

choices = ["Rock", "Paper", "Scissors"]

def main():

    user_input = input("Enter your choice: ").capitalize()

    if user_input not in choices:
        raise ValueError("Invalid choice")

    player_choice = choices.index(user_input)
    computer_choice = random.randint(0, 2)

    print(f"Player: {choices[player_choice]}")
    print(f"Computer: {choices[computer_choice]}")

    if player_choice == computer_choice:
        print("Draw")
    elif (player_choice == 0 and computer_choice == 2) or (player_choice == 2 and computer_choice == 1) or (player_choice == 1 and computer_choice == 0):
        print("You win")
    else :
        print("You lose")


if __name__ == main:
    main()