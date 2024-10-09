cat_age = int(input("Enter your cats age in months:"))


#Approach #1 is correct because it starts with if and continues using elif.
if cat_age <= 6:
    print(f"The price of the kitten is $250")

elif cat_age <= 11:
    print(f"price of the Teen is $225")

elif cat_age <= 95:
    print(f"The price of the adult is $150")

elif cat_age <= 96:
    print(f"The price of this senior is $85")

#uses Cat_age input to trigger the if/else statements.
