from flask import Flask

flask1 = Flask(__name__)

@flask1.route('/')
def index():
    print("hi, welcome to flask.")

@flask1.route('/user/<int:user_id>')
def user(user_id):
    return "profile page of user {}".format(user_id)

@flask1.route('/books/<genre>')
def books(genre):
    return "all books are in {} category".format(genre)

if __name__ == "__main__":
    flask1.run()
