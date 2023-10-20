DROP TABLE IF EXISTS posts;
DROP TABLE IF EXISTS users;

CREATE TABLE users (id SERIAL PRIMARY KEY, username TEXT, password TEXT);
CREATE TABLE posts (id SERIAL PRIMARY KEY, text TEXT, user_id INT, time TIME, date DATE, CONSTRAINT fk_users foreign key(user_id) references users(id) on delete cascade);

INSERT INTO users (username, password) VALUES ('benhurst', 'password');

INSERT INTO posts (text, user_id, time, date) VALUES ('a message!', 1, '12:51:36', '2023-09-30');