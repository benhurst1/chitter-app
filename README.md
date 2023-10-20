### Chitter App ###

https://chitter-app-mc6v.onrender.com/

Note: The database expires 18/01/24.

This application was built using a starter project during my Makers bootcamp.
The only significant file supplied was the database_connection.py, which abstracts away a lot of the psycopg methods and functions, but I still needed to adjust it with my own contributions to make this project work online.

This project was a challenge at the end of one of the modules, bringing together a lot of what I had learned up to that point. I did not use test driven development to build this, as it is supposed to be a prototype. I'd like to revisit this and try build the same (or better) using TDD.

seeds/chitter.sql
- has my queries for building and inserting some sample data.

templates
- my html pages with jinja templates taking arguments from the server and displaying content from the database.

lib
- classes are created for users and posts for easy manipulating when inserting or retrieving from the database.
- repositories which hold the methods and queries for the database.

app.py
- contains all my routes using Flask.
- I also use session to maintain users who have logged in and secrets to generated a random key for that session.

Dockerfile
- used a sample dockerfile to be able to deploy to render.


Learnings:
There were lots of learnings in the lead up to this project, such as using the repositories, how to use python to interact with the database, seeding data and testing the database.

But then there were lots of learnings in the production of this:
- I had to break down the project into smaller projects. First to understand how the routing works better, then another on how sessions work.
- encrypting passwords in the database using hashlib.
- adjusting the database_connection file url for the database and using environment variables to deploy.

Challenges:
- Biggest challenge by far was the cloud deployment, something I thought would be simple. I tried doing it first on Makers in-house system using Exoframe, but with little documentation and guidance, I switched to just using render. I initially tried using their python runtime using build and run commands, but after trying with docker, I had much better success.