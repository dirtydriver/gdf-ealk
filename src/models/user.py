import uuid

from src.common.database import Database


class User():
    def __init__(self,email,password,_id=None):
        self.email=email
        self.password=password
        self._id= uuid.uuid4().hex if id is None else _id

    @classmethod
    def get_by_email(cls,email):
        data= Database.find_one("user",{"email" : email})
        if data is not None:
            return cls(**data)
        return None

    @classmethod
    def get_by_id(cls,_id):
        data= Database.find_one("user",{"_id" : _id})

    @staticmethod
    def login_valid(email,password):
        user = User.get_by_email(email)
        if user is not None:
            return user.password == password
        return False

    @staticmethod
    def register(self,email,password):
        user = User.get_by_email(email)
        if user is None:
            new_user= User(email,password)
            new_user.save_to_mongo()

    def login(self):
        pass

    def get_blogs(self):
        pass

    def json(self):
        pass

    def save_to_mongo(self):
        pass