import random
def magic_8_ball(question):
    num = random.randint(1, 9)
    if num == 1:
        return ('Yes - definitely.')
    elif num == 2:
        return ("It is decidedly so.")
    elif num == 3:
        return ("Without a doubt.")
    elif num == 4:
        return ("Reply hazy, try again.")
    elif num == 5:
        return ("Ask again later.")
    elif num == 6:
        return ("Better not tell you now.")
    elif num == 7:
        return ("My sources say no.")
    elif num ==8:
        return ("Outlook not so good.")
    elif num == 9:
        return ("Very doubtful.")

question = input('Ask me:')
print("The answer to our question is: ",magic_8_ball(question))
