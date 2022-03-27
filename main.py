from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("base.html")

@app.route("/",methods=['POST'])
def home_post():
    text=request.form['u']
    processed_text=text.upper()
    return processed_text

@app.route("/about.html")
def about():
    return render_template("about.html")

@app.route("/leaderboard.html")
def leaderboard():
    return render_template("leaderboard.html")


if __name__ == "__main__":
    app.run(debug=True)