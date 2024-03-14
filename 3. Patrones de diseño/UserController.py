from flask import Flask, render_template, request
from UserRepository import UserRepository
from UserService import UserService


app = Flask(__name__)
user_repository = UserRepository()
user_service = UserService(user_repository)

@app.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = user_service.get_user(user_id)
    return render_template('user.html', user=user)

if __name__ == '__main__':
    app.run(debug=True)