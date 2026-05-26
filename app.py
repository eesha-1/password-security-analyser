from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    score = None
    if request.method == "POST":
        current_password = request.form["password"]
        print(current_password)
    return render_template("index.html", score=score)

if __name__ == "__main__":
    app.run(debug=True)