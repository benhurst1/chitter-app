from lib.user import User
import hashlib


class UserRepository:
    def __init__(self, connection):
        self._connection = connection

    def check_password(self, username, password_attempt):
        binary_password_attempt = password_attempt.encode("utf-8")
        hashed_password_attempt = hashlib.sha256(binary_password_attempt).hexdigest()
        rows = self._connection.execute(
            "SELECT * FROM users WHERE username = %s AND password = %s",
            [username, hashed_password_attempt],
        )
        if len(rows) == 0:
            return False
        return True

    def get_user(self, username):
        rows = self._connection.execute(
            "SELECT * FROM users WHERE username = %s",
            [username],
        )
        if len(rows) == 0:
            return False
        return User(rows[0]["id"], rows[0]["username"], rows[0]["password"])

    def create_user(self, username, password):
        binary_password = password.encode("utf-8")
        hashed_password = hashlib.sha256(binary_password).hexdigest()
        self._connection.execute(
            "INSERT INTO users (username, password) VALUES (%s, %s)",
            [username, hashed_password],
        )
        print("user created")
