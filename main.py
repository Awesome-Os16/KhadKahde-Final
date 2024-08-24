from termcolor import colored
import random
import time
import os

# Define the symbols on the dice
symbols = ["Chidi", "Pan", "Hukum", "Ekka", "Ghandi", "Bhurja"]

# tO R0LL dice
def roll_dice():
    return random.choice(symbols)

# Aesthetism is crazy/Dicce animation
def roll_dice_with_animation():
    for _ in range(10):  
        print(colored(random.choice(symbols), 'green'), end='\r')
        time.sleep(0.1)  
    final_symbol = roll_dice()
    print(colored(final_symbol, 'green'))
    return final_symbol

# Roll all of em 
def roll_dices_with_animation():
    rolled_dices = []
    for _ in range(6):
        rolled_dices.append(roll_dice_with_animation())
    return rolled_dices

# Checking the symbols and we have a winner!!
def calculate_winnings(rolled_dices, bet_symbol, bet_amount):
    # FIND FIND  FIND
    most_frequent_symbol = max(set(rolled_dices), key=rolled_dices.count)
    count = rolled_dices.count(most_frequent_symbol)
    
    if bet_symbol == most_frequent_symbol:
        return count * bet_amount
    return 0

# I don't believe in chances
def calculate_winning_chances():
    return round(1 / len(symbols) * 100, 2)

def display_title():
    title = r"""
  KhadKhade!
    """
    print(colored(title, 'green'))
    print("\n" * 2)

def display_menu():
    print(colored("1. Play KhadKhade", 'green'))
    print(colored("2. Exit", 'green'))
    print(colored("Credits: Awesome Dahal (Creator/Owner)", 'green'))
    print("\n" * 2)

def display_welcome():
    print(colored("Welcome to KhadKhade!", 'green'))
    print(colored("In this game, you can bet on one of the following symbols:", 'green'))
    print(colored(f"Symbols: {', '.join(symbols)}", 'green'))
    print(colored("""
    Rules:
    1. You place a bet on one of the symbols.
    2. Six dice are rolled, each with one of the symbols.
    3. The symbol that appears most frequently among the rolled dice wins.
    4. If your bet matches the most frequent symbol, you win based on the frequency:
       - 3 matching symbols = 3x your bet
       - 4 matching symbols = 4x your bet
       - 5 matching symbols = 5x your bet
       - 6 matching symbols = 6x your bet
    """, 'green'))

def khadkhade_game():
    display_welcome()

    bet_symbol = input(colored("Place your bet on one of the symbols(From abv): ", 'green')).strip()
    print("\n")
    if bet_symbol not in symbols:
        print(colored("Invalid symbol. Please try again.", 'green'))
        return

    bet_amount = input(colored("Enter your bet amount: ", 'green')).strip()
    if not bet_amount.isdigit():
        print(colored("Invalid amount. Please enter a number.", 'green'))
        return

    bet_amount = int(bet_amount)
    print("\n")
    
    print(colored(f"Betting on: {bet_symbol}", 'green'))
    print(colored(f"Bet amount: {bet_amount}", 'green'))
    
    # Display function of chances (above)
    winning_chances = calculate_winning_chances()
    print(colored(f"Your initial winning chances are: {winning_chances}%", 'green'))
    print("\n")
    
    # Use the thing
    print(colored("Rolling the dice...", 'green'))
    rolled_dices = roll_dices_with_animation()
    print(colored(f"The rolled dice symbols are: {', '.join(rolled_dices)}", 'green'))
    
    # Calculate duh chancess
    winnings = calculate_winnings(rolled_dices, bet_symbol, bet_amount)
    
    if winnings > 0:
        print(colored(f"Congratulations! You won {winnings}!", 'green'))
    else:
        print(colored("Sorry, you lost this time.", 'green'))
    print("\n" * 2)

def start_game():
    display_title()
    display_menu()
# Save the file(dont forget) I beg u
    while True:
        choice = input(colored("Enter your choice: ", 'green')).strip()
        print("\n")
        
        if choice == "1":
            while True:
                khadkhade_game()
                play_again = input(colored("Do you want to play again? (yes/no): ", 'green')).strip().lower()
                print("\n")
                if play_again != "yes":
                    print(colored("Thank you for playing KhadKhade!", 'green'))
                    print("\n")
                    return
        elif choice == "2":
            print(colored("Thank you for playing KhadKhade!", 'green'))
            print("\n")
            break
        else:
            print(colored("Invalid choice. Please try again.", 'green'))
            print("\n")
          # Awesome is the GOAT
#thx
# Start the game
start_game()
