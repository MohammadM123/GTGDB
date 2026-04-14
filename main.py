
from flask import Flask, render_template, request, session, redirect
import db
import secrets

app = Flask(__name__)
app.secret_key = "gtg"
app.config["PEPPER"] = secrets.token_hex(32)


@app.route("/")
def Home():
    guessData = db.GetAllGuesses()
    return render_template("index.html", guesses=guessData)


@app.route("/login", methods=["GET", "POST"])
def Login():

    if session.get("username"):
        return redirect("/")

    # They sent us data, get the username and password
    # then check if their details are correct.
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

        # Did they provide good details
        user = db.CheckLogin(username, password)
        if user:
            # Yes! Save their username and id then
            session['id'] = user['id']
            session['username'] = username

            # Send them back to the homepage
            return redirect("/")
        else:
            return render_template("login.html", error="Username or password incorrect")

    return render_template("login.html")


@app.route("/logout")
def Logout():
    session.clear()
    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def Register():

    # If they click the submit button, let's register
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

        if (not username) or (not password):
            return render_template("register.html", error="Please provide a username and password")

        if db.CheckIfUserExists(username):
            return render_template("register.html", error="Username already in use")

        # Try and add them to the DB
        new_user = db.RegisterUser(username, password)

        # Try and add them to the DB
        if new_user:

            print(new_user)
            # Update for auto login
            session['id'] = new_user['id']
            session['username'] = username
            # Success! Let's go to the homepage
            return redirect("/")

    return render_template("register.html")


@app.route("/add", methods=["GET", "POST"])
def Add():

    # Check if they are logged in first
    if session.get('username') == None:
        return redirect("/")

    # Did they click submit?
    if request.method == "POST":
        user_id = session['id']
        date = request.form['date']
        game = request.form['game']
        score = request.form['score']

        # Send the data to add our new guess to the db
        db.AddGuess(user_id, date, game, score)

    return render_template("add.html")


@app.route("/delete", methods=["POST"])
def Delete():

    guess_id = request.form["id"]

    if not int(guess_id) in db.GetUserGuesses(session["id"]):
        return redirect("/")

    db.DeleteGuess(guess_id)
    return redirect("/")


app.run(debug=True, port=5000)
