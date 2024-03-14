class UserService:
    def __init__(self, user_repository):
        self.user_reposirtory = user_repository

    def get_user(self, id):
        return self.user_reposirtory.get_user(id)
        