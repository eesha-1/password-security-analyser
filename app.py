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
 
    return render_template("index.html", score=score)

if __name__ == "__main__":
    app.run(debug=True)