#Vincent Macri
#CS175L-01
#Restaurants

vegetarian = False
vegan = False
gluten_free = False
keepGoing = True

while(keepGoing):
    #Vegetarian
    vegetarianInput = input("Is anyone in your party vegetarian? ")
    if vegetarianInput.lower() == "yes":
        vegetarian = True
       
    elif vegetarianInput.lower() == "no":
        vegetarian = False

    elif vegetarianInput.lower() != "yes" or "no":
        reask = True
        while(reask):
            print("Please enter either 'yes' or 'no'")
            vegetarianInput = input("Is anyone in your party vegetarian? ")
            if(vegetarianInput.lower() != 'yes' and vegetarianInput.lower() != 'no'):
                reask = True
            else:
                reask = False
        if vegetarianInput.lower() == "yes":
            vegetarian = True
            
        elif vegetarianInput.lower() == "no":
            vegetarian = False
            

    #Vegan
    veganInput = input("Is anyone in your party vegan? ")
    if veganInput.lower() == "yes":
        vegan = True
        
    elif veganInput.lower() == "no":
        vegan = False
        
    elif veganInput.lower() != "yes" or "no":
        reask = True
        while(reask):
            print("Please enter either 'yes' or 'no'")
            veganInput = input("Is anyone in your party vegan? ")
            if(veganInput.lower() != 'yes' and veganInput.lower() != 'no'):
                reask = True
            else:
                reask = False
        if veganInput.lower() == "yes":
            vegan = True
            
        elif veganInput.lower() == "no":
            vegan = False
            

    #Gluten Free
    glutenInput = input("Is anyone in your party gluten free? ")
    if glutenInput.lower() == "yes":
        gluten_free = True
        
    elif glutenInput.lower() == "no":
        gluten_free = False
        
    elif glutenInput.lower() != "yes" or "no":
        reask = True
        while(reask):
            print("Please enter either 'yes' or 'no'")
            glutenInput = input("Is anyone in your party gluten free? ")
            if(glutenInput.lower() != 'yes' and glutenInput.lower() != 'no'):
                reask = True
            else:
                reask = False
        if glutenInput.lower() == "yes":
            gluten_free = True
            
        elif glutenInput.lower() == "no":
            gluten_free = False
            

            
    print("")
    print("Here are your restaurant choices:")
    if(not vegetarian and not vegan and not gluten_free):
        print("Joe's Gourmet Burgers")
        print("Mama's Fine Italian")
        print("Main Street Pizza")
    elif(not vegan and not gluten_free):
        print("Mama's Fine Italian")
        print("Main Street Pizza")
    elif(not vegan):
        print("Main Street Pizza")
    print("Corner Cafe")
    print("Chef's Kitchen")
    
    keepGoing = input("Would you like to search for a restaurant again? ")
    if keepGoing.lower() == "yes":
        keepGoing = True
    elif keepGoing.lower() == "no":
        keepGoing = False
    elif keepGoing.lower() != "yes" or "no":
        askAgain = True
        while(askAgain):
            print("Please enter 'yes' or 'no'")
            keepGoing = input("Would you like to search for a restaurant again? ")
            if(keepGoing.lower() != 'yes' and keepGoing.lower() != 'no'):
                askAgain = True
            else:
                askAgain = False
        if keepGoing.lower() == "yes":
            keepGoing = True
        elif keepGoing.lower() == "no":
            keepGoing = False
print("Thanks for searching for a restaurant!")
