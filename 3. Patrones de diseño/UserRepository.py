
from UserEntity import UserEntity

class UserRepository:

    def __init__(self, db):
        self.db = db
    

    def get_user(self, id):
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM users WHERE id = %s", (id,))
        result =cursor.fetchone()
        return UserEntity(result[0], result[1], result[2])