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
print("You are confused of where the voice went, and where you are...\n You notice a shadow in the distance, maybe a building.")
Choice_1 = int(input("Do you get up and travel to the structure [press 1] or take off hazmat suit? [press 2]: "))

if Choice_1 == 1:
    print("You get up from the ground and notice a pain in your sholder.")
else:
    print("You take off your hazmat suit and suddenly die of asphyxia and radiation poisoning.")
    print('Game Over!'.center(82,'-'))

Choice_2 = int(input("Do you keep going to structure [press 1] or inspect injury [press 2]?: "))

if Choice_2 == 1:
    print(f"{Name} keeps going to structure and starts to feel light headed...")
    Choice_2p = int(input("Do you stop and inspect injury [press 1] or ignore the light headedness and continue towards the structure? [press 2]"))
    if Choice_2p == 1:
        print(f"{Name} stops to inspect the injury and finds that he is bleeding out. In a few minutes {Name} will bleed out.")
    elif Choice_2p == 2:
        print("You start to lose consciousness. \n The world fades to black.")
        print('Game Over!'.center(82,'-'))
        Choice_2l = int(input("Do you keep going to structure in hopes of finding help [press 1] or go back to the place you woke up at? [press 2]: "))
elif Choice_2 == 2:
    print(f"{Name} takes a moment to look at their injury, It is a cut that is bleeding. \n{Name} see's a bandage a few feet from him and uses it.")

Choice_3 = int(input("Do you "))