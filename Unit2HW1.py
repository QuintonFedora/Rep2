'''
Name: Quinton Fedora
Date: 9/26/24
Description: Unit 2 Homework 1
'''
from isort.logo import ASCII_ART

print('Problem 1'.center(20,'-'))

print('A quest game using text to communicate the missions')

print('A game that changes with the choices you make')

print('An adventure game with multiple outcomes')

print('Problem 2'.center(20,'-'))

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

print('Problem 3'.center(20,'-'))

#173.8 mi from portland to seattle

distance_to_seattle = 173.8
miles_per_gallon = int(input("Enter your car's fuel efficiency in miles per gallon (whole number): "))
gas_price_per_gallon = float(input("Enter the price of gas per gallon: "))
tank_capacity = int(input("Enter the capacity of your gas tank in gallons: "))
gallons_needed = distance_to_seattle / miles_per_gallon
if gallons_needed > tank_capacity:
    print("Warning: You will need to refuel on your trip!")
total_cost = tank_capacity * gas_price_per_gallon
print(f"To drive from Portland to Seattle ({distance_to_seattle} miles):")
print(f"Gallons needed: {gallons_needed:}")
print(f"Total cost to fill your gas tank: ${total_cost:}")
