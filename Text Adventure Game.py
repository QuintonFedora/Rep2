print('Introduction'.center(51,'-'))

print('A quest game using text to communicate the missions')

print('A game that changes with the choices you make')

print('An adventure game with multiple outcomes')

print('Beyond Earth and the Galaxy'.center(51,'-'))

ASCII_ART = r'''
++++++++++++++++++++++++++++++++++++++++++++++++++++
+++++++++++++++++++++    πππ +++++++++++++++++++++++
+++++++++++++++++++≈ -≠π -     +++++++++++++++++++++
+++++++++++++++++ √√ ×≈≈ ≈       +++++++++++++++++++
++++++++++++++++  -≈π- - =  × π= π++++++++++++++++++
++++++++++++++- ≠÷÷ ÷≈π ≠    √π    π++++++++++++++++
+++++++++++++ π=≠≠ ≠≈ ≈ - -  =   ππ π+++++++++++++++
+++++++++++  ≈≠=≠ ∞≈≈+ ≈≠ +   +≠ππ    π+++++++++++++
+++++++++ ≈≈≈÷≈÷ =≈÷ ≈ --       ππ πππ  ++++++++++++
++++++++----×≈  ≈≈≈ ≈ -  - ≈π   ÷  ππ     π+++++++++
+++++++++++------≈ ≈≈ -     π       π----+++++++++++
+++++++++++++---+-+-- ≈ π    -++------++++++++++++++
++++++++++++++----------------------++++++++++++++++
++++++++++++++++-------------------+++++++++++++++++
++++++++++++++++++---------------+++++++++++++++++++
'''

print(ASCII_ART)
print('The Beginning...')
print("You slowly wake up to a warm orange glow that covers everything.")
print('Introduction'.center(30,'-'))
print("You hear a voice in the distance ask...")


Name = input("What is your name, adventurer?: ").title()
print(f"You tell the voice your name is {Name}. \nThere is no response.")
print("You are confused of where the voice went, and where you are...\nYou notice a shadow in the distance, maybe a building.")
Choice_1 = int(input("Do you get up and travel to the structure [press 1] or take off hazmat suit? [press 2]: "))

if Choice_1 == 1:
    print("You get up from the ground and notice a pain in your sholder.")
else:
    print("You take off your hazmat suit and suddenly die of asphyxia and radiation poisoning.")
    print('Game Over!'.center(82,'-'))
    exit()

Choice_2 = int(input("Do you keep going to structure [press 1] or inspect injury [press 2]?: "))
if Choice_2 == 1:
    print(f"{Name} keeps going to structure and starts to feel light headed...")
    Choice_2p = int(input("Do you stop and inspect injury [press 1] or ignore the light headedness and continue towards the structure? [press 2]?: "))
    if Choice_2p == 1:
        print(f"{Name} stops to inspect the injury and finds that he is bleeding out. In a few minutes {Name} will bleed out.")
    elif Choice_2p == 2:
        print("You start to lose consciousness. \nThe world fades to black.")
        print('Game Over!'.center(32,'-'))
        exit()
    Choice_2l = int(input("Do you sit down on the ground and accept your fate [press 1] or do you look for a quick fix? [press 2]: " ))
    if Choice_2l == 1:
        print(f"{Name} has accepted their fate and they are at peace as they watch the world fade away slowly...")
        print('Game Over!'.center(92,'-'))
        exit()
    elif Choice_2l == 2:
        print("You quickly look around for something to wrap the injury in to stop the bleeding. \nYou find nothing... \n{Name} Passes away in a panic while looking for a bandage...")
        print('Game Over!'.center(81,'-'))
        exit()

elif Choice_2 == 2:
    print(f"{Name} takes a moment to look at their injury, It is a cut that is bleeding. \n{Name} see's a bandage a few feet from him and uses it. \nThis helps but does not completely fix the problem...")

Choice_3 = int(input("Do you keep going to structure in hopes of finding help [press 1] or go back to the place you woke up at? [press 2]: "))
if Choice_3 == 1:
    print("You continue towards the structure and just before you get there you start to pass out. \nJust before you fully pass out you see someone walking towards you, \nbut you are unable to do anything.")
    Choice_3p = int(input("You wake up in a small hut in an unknown location, \nDo you look for someone [press 1] or look for information in the hut? [press 2]: "))
    if Choice_3p == 1:
        print("You exit the small hut and start looking for someone nearby. You see a truck moving in the distance, \nAs you come closer to the truck you realize that they are armed and may not be friendly.")
    elif Choice_3p == 2:
        print("You get up off the ground and look around for any information of where you are. You find a news paper dated 9/17/31, \nThe front headline says 'The End of Civilization?' under is a story about nuclear war between the U.S. and Russia.")
elif Choice_3 == 2:
    print(f"{Name} starts to run back to the place they woke up at. \nWhen they get there they find a bandage and use it to stop the bleeding. The only question now is what to do next.")

print('You Won!'.center(80,'-'))
#Choice_4 = int(input("Do you "))
