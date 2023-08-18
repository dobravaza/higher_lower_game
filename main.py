import random
from art import logo, vs
from game_data import data

def game_end(score):
    print(f"You've lost.. your score is {score}")
def get_data():
    random_data_one = random.choice(data)
    random_data_two = random.choice(data)
    return random_data_one, random_data_two

def main():
    game_over = False
    score = 0
    while not game_over:
        print(logo)
        random_data_one, random_data_two = get_data()
        if score >= 1:
            print(f"You're right! Current score: {score}")


        name_to_guess_one = random_data_one['name']
        name_to_guess_two = random_data_two['name']
        first_guy_followers = random_data_one['follower_count']
        second_guy_followers = random_data_two['follower_count']
        folower_list = []
        folower_list.append(first_guy_followers)
        folower_list.append(second_guy_followers)
        a = max(folower_list)
        b = min(folower_list)
        print(first_guy_followers, second_guy_followers)
        print(f"Compare A:{name_to_guess_one}, a {random_data_one['description']} from {random_data_one['country']}")

        print(vs)

        print(f"Compare A:{name_to_guess_two}, a {random_data_two['description']} from {random_data_two['country']}")
        print(folower_list)
        users_choice = input("Who has more followers? Type 'A' or 'B': ")
        if users_choice == "A" and first_guy_followers == a:
            score += 1
        elif users_choice == "B" and second_guy_followers == a:
            score += 1
        else:
            game_over = True
            game_end(score)
main()
