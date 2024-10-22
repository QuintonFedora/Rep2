#Spring = month(March, april, may)
#Summer = month(June, July, August)
#Fall = month("September" , + "October" , + "November")
#Winter = "December", + "January", +"February"

user_month = input(" Enter the name of the month: ")
month = user_month.title()
day = int(input("Enter the day (1-31): "))

if month == "January" and day <= 31 and day >= 1:
    print(f"January {day} is in winter")
elif "January" and day > 31:
    print("this is not a valid day. Please try again.")

if month == "February" and day <= 29 and day >= 1:
    print(f"February {day} is in winter")
elif "February" and day > 29:
    print("this is not a valid day. Please try again.")

if month == "March" and day <= 31 and day >= 1:
    print(f"March {day} is in spring")
elif "March" and day > 31:
    print("this is not a valid day. Please try again.")

if month == "April" and day <= 30 and day >= 1:
    print(f"April {day} is in spring")
elif "April" and day > 30:
    print("this is not a valid day. Please try again.")

if month == "May" and day <= 31 and day >= 1:
    print(f"May {day} is in spring")
elif "May" and day > 31:
    print("this is not a valid day. Please try again.")

if month == "June" and day <= 30 and day >= 1:
    print(f"June {day} is in summer")
elif "June" and day > 30:
    print("this is not a valid day. Please try again.")

if month == "July" and day <= 31 and day >= 1:
    print(f"July {day} is in summer")
elif "July" and day > 31:
    print("this is not a valid day. Please try again.")

if month == "August" and day <= 31 and day >= 1:
    print(f"August {day} is in summer")
elif "August" and day > 31:
    print("this is not a valid day. Please try again.")

if month == "September" and day <= 30 and day >= 1:
    print(f"September {day} is in Fall")
elif "September" and day > 30:
    print("this is not a valid day. Please try again.")

if month == "October" and day <= 31 and day >= 1:
    print(f"October {day} is in Fall")
elif "October" and day > 31:
    print("this is not a valid day. Please try again.")

if month == "November" and day <= 30 and day >= 1:
    print(f"November {day} is in Fall")
elif "November" and day > 30:
    print("this is not a valid day. Please try again.")

if month == "December" and day <= 31 and day >= 1:
    print(f"December {day} is in Winter")
elif "December" and day > 31:
    print("this is not a valid day. Please try again.")

else:
    print("This is not valid. Please try again.")