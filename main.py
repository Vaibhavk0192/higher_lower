from art import logo,vs
from data import data
import random


def getInfo(a_choice,b_choice):
    name_a=a_choice["name"]
    description_a=a_choice["description"]
    country_a=a_choice["country"]
    print(f"Compare A: {name_a}, a {description_a}, from {country_a}.")
    print(vs)
    name_b=b_choice["name"]
    description_b=b_choice["description"]
    country_b=b_choice["country"]
    print(f"Against B: {name_b}, a {description_b}, from {country_b}.")
    follower_a=a_choice["follower_count"]
    follower_b=b_choice["follower_count"]
    if follower_a>follower_b:
        return "a"
    else: 
        return "b"


score=0
b_choice=random.choice(data)
end_game=False


while not end_game:
    a_choice=b_choice
    b_choice=random.choice(data)
    while a_choice == b_choice:
        b_choice=random.choice(data)
    print(logo)
    result=getInfo(a_choice,b_choice)
    choice=input("Who has more followers? Type 'A' or 'B': ").lower()
    print("\033c")
    if choice==result:
        score+=1
        print(f"You're right! Current score: {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        end_game=True


    

        
    