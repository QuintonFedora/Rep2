#Create a Story Template
#Design a story with placeholders for different types of words. For example:
#"Once upon a time, there was a [noun] who loved to [verb] with their [adjective] [noun]."
#Gather User Input
#Your program should ask the user to input the following:
#A person's name (make sure the name is formatted in title case).
#A month, day, and year (for a specific date).
#At least 5 nouns, 5 verbs, 3 adjectives, and 2 adverbs.
#Replace Placeholders
#Use the words provided by the user to replace the placeholders in your story template. This should be done using f-strings to format the output.
#Display the Final Story
#After gathering all the inputs, display their name, followed by a new line, the date (mm/dd/yy), followed by a new line, then the completed story to the user with the words they provided


def story_template():
    print(f"\n{name}\n{month} {day}, {year}")
    print(f"One {adjective1} day {noun1} was {verb1} and then {noun2} they went to the {noun3}. \nThe {noun3} was {adjective2}, {noun1} was {adverb1} that {noun4} would join them at the {noun3} and play {verb2}")

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
