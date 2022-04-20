from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app


class Ninja:
    def __init__(self, data) -> object:
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']

    # Create
    @classmethod
    def save(cls, data) -> int:
        query = "INSERT INTO ninjas ( first_name, last_name, age, dojo_id ) VALUES ( %(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s );"
        return connectToMySQL(app.DATABASE).query_db(query, data)

    # Read
    @classmethod
    def get_all(cls) -> list[object]:
        query = "SELECT * FROM ninjas;"
        results = connectToMySQL(app.DATABASE).query_db(query)
        ninjas = []
        for ninja in results:
            ninjas.append(cls(ninja))
        return ninjas

    @classmethod
    def get_one(cls, numId) -> object:
        query = "SELECT * FROM ninjas WHERE id=%(id)s;"
        result = connectToMySQL(app.DATABASE).query_db(
            query, {'id': int(numId)})
        return cls(result[0])

    # Update
    @classmethod
    def update(cls, data) -> None:
        query = "UPDATE ninjas SET first_name=%(first_name)s, last_name=%(last_name)s, age=%(age)d, dojo_id=%(dojo_id)d WHERE id=%(id)s;"
        return connectToMySQL(app.DATABASE).query_db(query, data)

    # Destroy
    @classmethod
    def delete(cls, numId) -> None:
        query = "DELETE FROM ninjas WHERE id=%(id)s;"
        return connectToMySQL(app.DATABASE).query_db(query, {'id': int(numId)})
