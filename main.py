from art import logo
import random
import time
import os


def display_intro():
    print(logo)
    print("Welcome to Blackjack Game!")
    print("Get as close as you can to 21 without going over. The ace can count as 1 or 11.")


def get_player_choice():
    while True:
        choice = input("Type 's' to start the game, 'q' to quit: ").lower()
        if choice in ['s', 'q']:
            return choice
        else:
            print("Invalid input. Please enter 's' or 'q'.")


def start_game():
    ACE_VALUE = 11
    cards = [ACE_VALUE, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    def add_card(card_lst, n):
        """
        Appending cards randomly from the deck.
        card_list is the list to which the number will be added.
        n is the number of cards that will be added.
        """
        for _ in range(n):
            random_card = random.choice(cards)
            card_lst.append(random_card)

    def handle_ace(cards, current_score):
        if current_score > 21 and ACE_VALUE in cards:
            return current_score - 10
        return current_score

    def display_result(match_result):
        print(f"Your final hand: {user_cards}, your score: {user_score} \n "
              f"Computer final hand: {computer_cards}, computer score: {computer_score} \n"
              f"You {match_result}")

    should_continue = True

    while should_continue:
        user_cards = []
        computer_cards = []

        add_card(user_cards, 2)
        add_card(computer_cards, 2)

        user_score = sum(user_cards)
        computer_score = sum(computer_cards)

        print(f"Your cards: {user_cards}, your score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        hit = input("Type 'c' to get another card, type 'p' to pass: ").lower()
        if hit == 'c':
            add_card(user_cards, 1)
            user_score = sum(user_cards)
            user_score = handle_ace(user_cards, user_score)

        while computer_score < 17:
            add_card(computer_cards, 1)
            computer_score = sum(computer_cards)
            computer_score = handle_ace(computer_cards, computer_score)

        if user_score == computer_score:
            display_result("Draw!")
        elif computer_score == 21:
            display_result("Lose, opponent has Blackjack")
        elif user_score == 21:
            display_result("Win with a Blackjack 🤩")
        elif user_score > 21:
            display_result("You went over. You lose")
        elif computer_score > 21:
            display_result("Opponent went over. You win")
        elif user_score > computer_score:
            display_result("You win")
        else:
            display_result("You lose")

        input("Press Enter to continue...")  # Wait for user input before clearing the screen
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen

        another_game = input("Do you want another round? 'y' for another round, type 'n' to end the game: ")
        if another_game != "y":
            should_continue = False

# Main program flow
display_intro()
start_choice = get_player_choice()

if start_choice == 's':
    print("Let's start the game!\n")
    time.sleep(1)  # Introduce a delay for a smoother experience
    start_game()
else:
    print("Goodbye! Thanks for playing.")

