current_password = input("Please enter your current password: ") #Prompt user to input their current password
print("Analysing: " + current_password) #Print Analysing with the users current password

score = 0 #Initialise password score to zero

if len(current_password) < 6:
    score = score + 0 #Award zero points for a password equal to or under 6 characters
elif len(current_password) >= 6 and len(current_password) <= 9:
    score = score + 1 #Award one point if length is between six and nine characters
else:
    score = score + 2 #Award two points if character length is equal to or over ten

