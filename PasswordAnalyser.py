current_password = input("Please enter your current password: ") #Prompts user to input their current password
print(f"Analysing: {current_password}") #Prints Analysing with the users current password

score = 0 #Initialises password score to zero

if len(current_password) < 6:
    score = score + 0 #Awards zero points for a password equal to or under 6 characters
elif len(current_password) >= 6 and len(current_password) <= 9:
    score = score + 1 #Awards one point if length is between six and nine characters
else:
    score = score + 2 #Awards two points if character length is equal to or over ten

#Initially sets the password to contain no letters, numbers or symbols
has_letter = False
has_number = False
has_symbol = False




print(f"Your score is: {score}") #Prints password score

