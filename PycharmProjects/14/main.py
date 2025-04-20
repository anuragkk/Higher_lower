from game_data import data
import random


def random_account(account):
    account_2 = random.choice(data)
    if account == account_2:
        account_2 = random.choice(data)
    return account_2


def formatting(account):
    return f"{account['name']} from {account['country']}, profession: {account['profession']}"


def check_answer(account_1, account_2, answer):
    if account_1['follower_count'] > account_2['follower_count'] and answer == "a" \
            or account_2['follower_count'] > account_1['follower_count'] and answer == "b":
        return True
    else:
        return False


account_1 = random.choice(data)


def game():
    score = 0
    print("Welcome to higher lower Game")
    game_is_on = True
    questions_asked = 0
    while game_is_on:

        if questions_asked == len(data):
            break
        account_2 = random_account(account_1)
        print(f"compare A: {formatting(account_1)}")
        print("vs")
        print(f"Against B: {formatting(account_2)}")
        choice = input("who has more followers : 'A' or 'B'\n").lower()
        questions_asked += 1
        check_answer(account_1=account_1, account_2=account_2, answer=choice)
        is_correct = check_answer(account_1=account_1, account_2=account_2, answer=choice)
        if is_correct:
            score += 1
            print(f"you have got this right, current score is {score}")
            account_1 = account_2


        else:
            print("you have got this wrong ")
            still_wanna_play = input("Do you still want to continue\n").lower()
            if still_wanna_play != "y":
                game_is_on = False
                print(f"Game over! Your final score is {score}")


game()
