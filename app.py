from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")  # Redirects to a home page with a button

@app.route("/hearts")
def hearts():
    return render_template("hearts.html")  # The page where hearts appear

if __name__ == "__main__":
    app.run(debug=True)
