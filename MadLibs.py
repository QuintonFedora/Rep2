
def mad_libs():
    # Story
    story_template = (
        "Once upon a time, there was a {noun1} named {name} who loved to {verb1} "
        "with their {adjective1} {noun2}. One day, they decided to {verb2} to the "
        "{noun3} and {verb3} all day long. They were so {adjective2} that they "
        "even {adverb1} {verb4} with a {noun4}!")

    # user input
    name = input("Enter a person's name: ").title()
    month = input("Enter a month (Ex: October): ")
    day = input("Enter a day (Ex: 8): ")
    year = input("Enter a year (Ex: 2024): ")

    nouns = [input(f"Enter noun: ") for i in range(5)]
    verbs = [input(f"Enter verb: ") for i in range(5)]
    adjectives = [input(f"Enter adjective: ") for i in range(3)]
    adverbs = [input(f"Enter adverb: ") for i in range(2)]

    # Replace placeholders
    story = story_template.format(
        name=name,
        noun1=nouns[0],
        noun2=nouns[1],
        noun3=nouns[2],
        noun4=nouns[3],
        verb1=verbs[0],
        verb2=verbs[1],
        verb3=verbs[2],
        verb4=verbs[3],
        adjective1=adjectives[0],
        adjective2=adjectives[1],
        adverb1=adverbs[0]
    )

    # date
    date = f"{month}/{day}/{year}"

    # print story
    print(f"\n{name}\n{date}\n{story}")


mad_libs()