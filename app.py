import os
from flask import Flask, request, render_template, session, redirect
import secrets

from lib.database_connection import get_flask_database_connection
from lib.user_repository import UserRepository
from lib.post_repository import PostRepository
from lib.post import Post
from datetime import datetime, date

# Create a new Flask app
app = Flask(__name__)
secret = secrets.token_urlsafe(32)
app.secret_key = secret


# == Your Routes Here ==


@app.route("/")
def get_home():
    if not session.get("user_id"):
        session["user_id"] = False
    connection = get_flask_database_connection(app)
    post_repo = PostRepository(connection)
    posts = post_repo.all()
    if "user" in session:
        return render_template(
            "/index.html", message=f"Logged in as {session['user_id']}", posts=posts
        )
    return render_template("/index.html", posts=posts)


@app.route("/", methods=["POST"])
def post_post():
    post_text = request.form["post"]
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    current_date = date.today()
    connection = get_flask_database_connection(app)
    post_repo = PostRepository(connection)
    post_repo.add(Post(None, post_text, session["user_id"], current_time, current_date))
    return redirect("/")


@app.route("/login")
def get_login():
    return render_template("/login.html")


@app.route("/login", methods=["POST"])
def post_login():
    username = request.form["username"]
    password = request.form["password"]

    connection = get_flask_database_connection(app)
    repo = UserRepository(connection)

    if repo.check_password(username, password):
        user = repo.get_user(username)
        session["user_id"] = user.id
        return redirect("/")
    else:
        return redirect("/")


@app.route("/logout")
def post_logout():
    session["user_id"] = None
    return redirect("/")


@app.route("/create")
def get_create():
    if "user" in session:
        return redirect("/")
    return render_template("/create.html")


@app.route("/create", methods=["POST"])
def post_create():
    username = request.form["username"]
    password = request.form["password"]
    connection = get_flask_database_connection(app)
    repo = UserRepository(connection)
    if repo.get_user(username) == False:
        repo.create_user(username, password)
        return redirect("/")
    return redirect("/")


# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == "__main__":
    app.run(
        debug=True,  # Optional but useful for now
        host="0.0.0.0",  # Listen for connections directed _to_ any address
    )
