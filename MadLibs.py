def story_template():
    print(f"\n{name}\n{month} {day}, {year}")
    print(f"One {adjective1} day {noun1} was {verb1} and then {noun2} and {noun1} went to the {noun3}.\nThe {noun3} was {adjective2}, {noun1} was {adverb1} that {noun2} would join them at the {noun3} and {verb2} to play a game.\n{noun2} {verb3} {adverb2} to go to {noun4} and {verb4}? {noun1} {verb5} want to leave the {noun3} so he was {adjective3}.\nLater {noun1} went {noun5} and {verb4} because {noun1} was tired. ")

name = input("Enter a person's name: ").title()
month = input("Enter a month (Ex: November): ").title()
day = int(input("Enter a day (Ex: 4): "))
year = int(input("Enter a year (Ex: 2024): "))

noun1 = input("Enter a noun: ")
noun2 = input("Enter a noun: ")
noun3 = input("Enter a noun: ")
noun4 = input("Enter a noun: ")
noun5 = input("Enter a noun: ")

verb1 = input("Enter a verb: ")
verb2 = input("Enter a verb: ")
verb3 = input("Enter a verb: ")
verb4 = input("Enter a verb: ")
verb5 = input("Enter a verb: ")

adjective1 = input("Enter an adjective: ")
adjective2 = input("Enter an adjective: ")
adjective3 = input("Enter an adjective: ")

adverb1 = input("Enter an adverb: ")
adverb2 = input("Enter an adverb: ")

story_template()
