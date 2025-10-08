import random

def fortune_cookie():
    fortunes = [
        "You will have a great day!",
        "Success is on the horizon.",
        "Happiness is a choice, choose wisely.",
        "Adventure awaits you this weekend.",
        "You will make a new friend soon.",
        "A thrilling time is in your immediate future.",
        "Your hard work will soon pay off.",
        "Expect the unexpected.",
        "You will find something valuable today.",
        "A fresh start will put you on your way."
    ]
    return random.choice(fortunes)

print("Your fortune cookie says:" , fortune_cookie())