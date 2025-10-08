def convert_to_jupiter_weight(earth_weight): 
    jupiter_weight = earth_weight * 2.53 
    return(jupiter_weight) 

earth_weight =float(input("Enter your weight: ")) 
print("Your weight on Jupiter is {:.2f}".format(convert_to_jupiter_weight(earth_weight)))