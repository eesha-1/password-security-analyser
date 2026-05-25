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

for character in current_password:
    if character.isalpha(): #If alphabetical letter
        has_letter = True
    elif character.isdigit(): #If number
        has_number = True
    else: #Else symbol
        has_symbol = True 

if has_letter and has_number and has_symbol:
    score = score + 3 
elif has_letter and has_number:
    score = score + 2
elif has_letter and has_symbol:
    score = score + 2
elif has_symbol and has_number:
    score = score + 2
elif has_letter:
    score = score + 1
elif has_number:
    score = score + 1
elif has_symbol:
    score = score + 1
else:
    print("Invalid password, please enter your password again. ") #Prints if user did not enter a value


print(f"Your password strength score is: {score}") #Prints password score

