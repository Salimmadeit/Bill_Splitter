# write your code here
import random

num_of_attendees: int = int(input("Enter the number of friends joining (including you):\n> "))
attendees: dict = {}
personal_bill_value: int | float = 0

if num_of_attendees <= 0:
    print("\nNo one is joining for the party")
else:

    print("")
    print("Enter the name of every friend (including you), each on a new line:")
    for i in range(num_of_attendees):
        current_attendee: str = input("> ")
        attendees[current_attendee] = personal_bill_value

    total_bill_value: int = int(input("Enter the total bill value:\n> "))
    personal_bill_value += round((total_bill_value / num_of_attendees), 2)

    # assigned the average bill evenly to everyone
    for name, bill_value in attendees.items():
        attendees[name] = personal_bill_value

    # who_is_lucky feature
    who_is_lucky = input('Do you want to use the "Who is lucky?" feature? Write Yes / No:\n> ')
    luck = False
    lucky_one = random.choice([key for key in attendees.keys()])
    if who_is_lucky == "Yes" or who_is_lucky == "yes":
        luck = True
        print(f"{lucky_one} is the lucky one!")
        lucky_ones_bill = ( attendees[lucky_one] / ( num_of_attendees - 1 ) )
        for key in attendees.keys():
            attendees[key] += lucky_ones_bill
        attendees[lucky_one] = 0

        print(attendees)

    else:
        luck = False
        print("No one is going to be lucky")
        print(attendees)




