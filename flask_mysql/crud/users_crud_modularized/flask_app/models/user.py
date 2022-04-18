from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app


class User:
    def __init__(self, data) -> object:
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls) -> list[object]:
        query = "SELECT * FROM users;"
        results = connectToMySQL(app.DATABASE).query_db(query)
        users = []
        for user in results:
            users.append(cls(user))
        return users

    @classmethod
    def get_one(cls, numId) -> object:
        query = "SELECT * FROM users WHERE id=%(id)s;"
        result = connectToMySQL(app.DATABASE).query_db(
            query, {'id': int(numId)})
        user = cls(result[0])
        return user

    @classmethod
    def save(cls, data) -> int:
        query = "INSERT INTO users ( first_name , last_name , email , created_at, updated_at ) VALUES ( %(first_name)s , %(last_name)s , %(email)s , NOW() , NOW() );"
        return connectToMySQL(app.DATABASE).query_db(query, data)

    @classmethod
    def update(cls, data) -> None:
        query = "UPDATE users SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s WHERE id=%(id)s;"
        return connectToMySQL(app.DATABASE).query_db(query, data)

    @classmethod
    def delete(cls, numId) -> None:
        query = "DELETE FROM users WHERE id=%(id)s;"
        return connectToMySQL(app.DATABASE).query_db(query, {'id': int(numId)})

    @property
    def full_name(self) -> str:
        return f'{self.first_name} {self.last_name}'
