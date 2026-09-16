# write your code here
num_of_attendees = int(input("Enter the number of friends joining (including you):"))

attendees = {}

for i in range(num_of_attendees):
    current_attendee = input("")
    attendees[current_attendee] = 0

print(attendees)
