def hogwarts_sorting_hat(q1, q2, q3):
    gryffindor = 0
    ravenclaw = 0
    hufflepuff = 0
    slytherin = 0

    # Question 1
    if q1 == 1:
        gryffindor += 1
        ravenclaw += 1
    elif q1 == 2:
        hufflepuff += 1
        slytherin += 1
    else:
        return "Wrong input for question 1."

    # Question 2
    if q2 == 1:
        hufflepuff += 2
    elif q2 == 2:
        slytherin += 2
    elif q2 == 3:
        ravenclaw += 2
    elif q2 == 4:
        gryffindor += 2
    else:
        return "Wrong input for question 2."

    # Question 3
    if q3 == 1:
        slytherin += 4
    elif q3 == 2:
        hufflepuff += 4
    elif q3 == 3:
        ravenclaw += 4
    elif q3 == 4:
        gryffindor += 4
    else:
        return "Wrong input for question 3."

    # House scores
    scores = {
        "Gryffindor": gryffindor,
        "Ravenclaw": ravenclaw,
        "Hufflepuff": hufflepuff,
        "Slytherin": slytherin
    }

    best_house = max(scores, key=scores.get)
    return best_house


# Questions
q1 = int(input("Do you like Dawn or Dusk? 1) Dawn 2) Dusk: "))
q2 = int(input("When I’m dead, I want people to remember me as: 1) The Good 2) The Great 3) The Wise 4) The Bold: "))
q3 = int(input("Which kind of instrument most pleases your ear? 1) The violin 2) The trumpet 3) The piano 4) The drum: "))

house = hogwarts_sorting_hat(q1, q2, q3)
print(f" You belong to... {house}!")
