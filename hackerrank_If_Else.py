
def hackone(number):
    if number % 2 == 1:
        print ("Weird")
    elif number % 2 ==0:
        if number >=2 and number <=5:
            print ("Not Weird")
        elif number >=6 and number <=20:
            print ("Weird")
        elif number >20:
            print ("Not Weird")
    else:
        print("Not Weird")

number = int(input("Enter number: "))
hackone(number)
