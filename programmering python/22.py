import random


def roll_dice():
    """Simulate rolling two dice and return the total."""
    return random.randint(1, 6) + random.randint(1, 6)


def main():
    print("Welcome to the Dice Game!")

    # Ask for the number of rounds
    rounds = int(input("Enter the number of rounds you want to play: "))

    player_score = 0
    ai_score = 0
    player_rolls = []
    ai_rolls = []

    for round_number in range(1, rounds + 1):
        input(f"\n--- Round {round_number} ---\nPress Enter to roll the dice...")

        # Player's turn
        player_roll = roll_dice()
        player_rolls.append(player_roll)
        print(f"You rolled: {player_roll}")

        # AI's turn
        ai_roll = roll_dice()
        ai_rolls.append(ai_roll)
        print(f"AI rolled: {ai_roll}")

        # Determine the winner of the round
        if player_roll > ai_roll:
            print("You win this round!")
            player_score += 1
        elif player_roll < ai_roll:
            print("AI wins this round!")
            ai_score += 1
        else:
            print("It's a tie!")

        print(f"Current Score - You: {player_score}, AI: {ai_score}")

    # Calculate averages and highest/lowest rolls
    total_player_rolls = sum(player_rolls)
    total_ai_rolls = sum(ai_rolls)
    average_player_roll = total_player_rolls / rounds
    average_ai_roll = total_ai_rolls / rounds
    highest_roll = max(player_rolls + ai_rolls)
    lowest_roll = min(player_rolls + ai_rolls)

    # Determine the overall winner
    print("\n--- Game Over ---")
    print(f"Final Score - You: {player_score}, AI: {ai_score}")

    if player_score > ai_score:
        print("Congratulations! You are the overall winner!")
    elif player_score < ai_score:
        print("AI is the overall winner! Better luck next time.")
    else:
        print("It's a tie overall!")

    # Display averages and highest/lowest rolls
    print(f"Your Average Roll: {average_player_roll:.1f}")
    print(f"AI's Average Roll: {average_ai_roll:.1f}")
    print(f"Highest Roll in the Game: {highest_roll}")
    print(f"Lowest Roll in the Game: {lowest_roll}")


if __name__ == "__main__":
    main()
