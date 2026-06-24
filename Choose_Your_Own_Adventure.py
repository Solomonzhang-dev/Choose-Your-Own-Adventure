### Print a welcome message
print("Welcome to the Haunted Mansion!")
print("You inherited this house from a relative of yours.")
print("The house appears old and decrepited. Yet, you walk in the front door fearlessly.")
print("Do you want to enter the living room or the dining room?")

### Prompt user for a choice
roomChoice = input("> ")

if(roomChoice == "living room"):
    print("You enter the living room")
    print("AS you walk in, you see a sleeping serpent guarding some gold jewelry.")
    print("Do you want to steal the jewelry from the serpent? (yes/no)")
    
    pitbullChoice = input("> ")
    
    if(pitbullChoice == "yes"):
        print("You attempt to steal the jewelry, but it wakes up and swallows you to whole.")
        print("You are now dead...")
    
    elif(pitbullChoice == "no"):
        print("You decide to not steal the serpent's jewelry")
        print("You turn around and leave the house safely")
    else:
        print("Invalid choice. Please enter yes or no.")
    
elif(roomChoice == "dining room"):
    print("You chose to go into the dining room.")
    print("As you walk in, you see an expensive-looking vase on the table.")
    print("Do you want to open the vase? (yes/no)")
    
    vaseChoice = input("> ")
    
    if(vaseChoice == "yes"):
        print("You open the vase and find a pile of bones")
        print("You fell unconcious afterwards from being grossed out.")
    elif(vaseChoice == "no"):
        print("You decide not to open the shiny vase.")
        print("As you turn to leave, you hear a cracking sound coming from the corner.")
        print("A dark figure with glowing red eyes launches at you, knocking you unconcious")
        print("You wake up in your bed. It was all a dream.")
    else:
        print("Invalid choice. Please enter yes or no.")
else:
    print("Invalid choice. Please enter living room or dining room.")
