from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    score = None
    if request.method == "POST":
        current_password = request.form["password"]
        score = 0
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

        #Checking lowercase and uppercase characters in the password
        #initially sets the password to contain no lowercase or uppercase letters
        has_lowercase = False 
        has_uppercase = False

        for character in current_password:
            if character.islower():
                has_lowercase = True
            elif character.isupper():
                has_uppercase = True

        if has_lowercase and has_uppercase: #If password contains mix of uppercase and lowercase letters
            score = score + 2
        elif has_lowercase:
            score = score + 1
        elif has_uppercase:
            score = score + 1

    return render_template("index.html", score=score)

if __name__ == "__main__":
    app.run(debug=True)