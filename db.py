import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
from flask import current_app
import time


def GetDB():

    # Connect to the database and return the connection object
    db = sqlite3.connect(".database/gtg.db")
    db.row_factory = sqlite3.Row

    return db

# Helper functions


def GetUserByUsername(username):
    """Get user info from username"""
    db = GetDB()
    return db.execute("SELECT * FROM Users WHERE username=?", (username,)).fetchone()


def GetUserGuesses(user_id):
    """Return list of guess_id of user guesses"""

    db = GetDB()

    guesses = db.execute("SELECT id FROM Guesses WHERE user_id=?",
                         (user_id,)).fetchall()

    id_list = []

    for guess in guesses:
        id_list.append(guess["id"])
    return id_list


def CheckIfUserExists(username):
    """Return True if user with given username exists, else return False"""
    db = GetDB()
    user = db.execute("SELECT * FROM Users WHERE username=?",
                      (username,)).fetchone()
    if user:
        return True
    else:
        return False


def GetGuess(guess_id):
    db = GetDB()
    guess = db.execute("""SELECT Guesses.id, Guesses.date, Guesses.game, Guesses.score, Users.username
                            FROM Guesses JOIN Users ON Guesses.user_id = Users.id WHERE Guesses.id=?""",
                       (guess_id,)).fetchone()

    return guess


GetGuess(10)

# Main functions


def GetAllGuesses():

    # Connect, query all guesses and then return the data
    db = GetDB()
    guesses = db.execute("""SELECT Guesses.id, Guesses.date, Guesses.game, Guesses.score, Users.username
                            FROM Guesses JOIN Users ON Guesses.user_id = Users.id
                            ORDER BY date DESC""").fetchall()
    db.close()
    return guesses


def CheckLogin(username, password):

    db = GetDB()

    # Ask the database for a single user matching the provided name
    user = db.execute("SELECT * FROM Users WHERE username=?",
                      (username,)).fetchone()

    # Do they exist?
    if user is not None:
        # OK they exist, is their password correct

        if check_password_hash(user['password'], password):
            # They got it right, return their details
            return user

    # If we get here, the username or password failed.
    return None


def IncrementLoginAttempts(user_id):
    """Increment failed login attempts for one user and set lock time if failed attempts >= 5"""
    db = GetDB()

    user = db.execute(
        "SELECT failed_attempts FROM Users WHERE id=?", (user_id,)).fetchone()
    attempts = user["failed_attempts"] + 1

    if attempts >= 5:
        lock_until = int(time.time()) + 300  # 5 minutes
        db.execute(
            "UPDATE Users SET failed_attempts=0, lock_until=? WHERE id=?",
            (lock_until, user_id)
        )
    else:
        db.execute(
            "UPDATE Users SET failed_attempts=? WHERE id=?",
            (attempts, user_id)
        )

    db.commit()


def ResetLoginAttempts(user_id):
    """Reset failed login attempts and lock time for one user"""
    db = GetDB()
    db.execute(
        "UPDATE Users SET failed_attempts=0, lock_until=0 WHERE id=?",
        (user_id,)
    )
    db.commit()


def RegisterUser(username, password):

    # Check if they gave us a username and password
    if username is None or password is None:
        return False

    # Attempt to add them to the database
    db = GetDB()

    hash = generate_password_hash(
        password,
        method="pbkdf2:sha256",
        salt_length=16
    )
    db.execute("INSERT INTO Users(username, password) VALUES(?, ?)",
               (username, hash,))
    db.commit()

    user = db.execute("SELECT * FROM Users WHERE username=?",
                      (username,)).fetchone()

    # If registration is successful, send back user object for auto login
    return {"id": user["id"], "username": user["username"]}


def AddGuess(user_id, date, game, score):

    # Check if any boxes were empty
    if date is None or game is None:
        return False

    # Get the DB and add the guess
    db = GetDB()
    db.execute("INSERT INTO Guesses(user_id, date, game, score) VALUES (?, ?, ?, ?)",
               (user_id, date, game, score,))
    db.commit()

    return True


def UpdateGuess(guess_id, date, game, score):

    # Check if any boxes were empty
    if date is None or game is None:
        return False

    # Get the DB and add the guess
    db = GetDB()
    db.execute("UPDATE Guesses SET date=?, game=?, score=? WHERE id=?",
               (date, game, score, guess_id))
    db.commit()

    return True


def DeleteGuess(id):
    db = GetDB()
    db.execute("DELETE FROM Guesses WHERE id=?", (id,))
    db.commit()
