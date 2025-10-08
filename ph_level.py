def ph_level(ph):
    if ph > 7:
        print("Basic")
    elif ph < 7:
        print("Acidic")
    else:
        print("Neutral")
ph = float(input("Enter your pH level: "))
ph_level(ph)