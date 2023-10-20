from lib.post import Post


class PostRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute(
            "SELECT posts.id AS post_id, posts.text, posts.user_id, posts.time, posts.date, users.username FROM posts JOIN users ON users.id = posts.user_id ORDER BY post_id DESC"
        )
        posts = []
        for row in rows:
            post = Post(
                row["post_id"],
                row["text"],
                row["user_id"],
                row["time"],
                row["date"],
                row["username"],
            )
            posts.append(post)
        return posts

    def add(self, post):
        self._connection.execute(
            "INSERT INTO posts (text, user_id, time, date) VALUES (%s, %s, %s, %s)",
            [post.text, post.user_id, post.time, post.date],
        )
