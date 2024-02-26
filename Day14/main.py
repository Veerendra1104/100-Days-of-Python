from data import data
from art import logo,vs

import random

def get_random_data():
    return random.choice(data)

def format_data(account):
    account_name= account["name"]
    account_followers = account["follower_count"]
    account_description = account["description"]
    account_country = account["country"]
    return print(f"{account_name} is from {account_country} and is {account_description}")

def check(guess,account_1,account_2):
    if account_1 > account_2:
        return guess=="a"
    else:
        return guess=="b"

def game():
    print(logo)
    score = 0
    game_should_continue= True
    account_a= get_random_data()
    account_b = get_random_data()

    while game_should_continue:

        account_a = account_b
        account_b = get_random_data()

        while account_a == account_b:
            account_b = get_random_data()

        print(f"Compare a: {format_data(account_a)}.")

        print(vs)
        print(f"Against b: {format_data(account_b)}.")

        guess = input("Who has more followers? Type 'a'or 'b'" )
        a_follower_count= account_a["follower_count"]
        b_follower_count = account_b["follower_count"]
        is_correct = check(guess,a_follower_count,b_follower_count)

        if is_correct:
            score += 1
            print(f"Your right! Current score is : {score}.")
        else:
            game_should_continue=False
            print(f"Sorry, that's wrong. Final score is : {score}")


game()

