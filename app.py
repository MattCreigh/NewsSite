from flask import Flask
app = Flask(__name__)

@app.route('/')
def Home():
    return render_template("home.html")

@app.route('/')
def About():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug = True)
