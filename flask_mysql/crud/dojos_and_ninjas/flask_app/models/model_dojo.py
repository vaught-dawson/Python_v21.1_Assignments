from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask_app.models import model_ninja


class Dojo:
    def __init__(self, data) -> object:
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    # Create
    @classmethod
    def save(cls, data) -> int:
        query = "INSERT INTO dojos ( name ) VALUES ( %(name)s );"
        return connectToMySQL(app.DATABASE).query_db(query, data)

    # Read
    @classmethod
    def get_all(cls) -> list[object]:
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(app.DATABASE).query_db(query)
        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos

    @classmethod
    def get_one(cls, dojo_id) -> object:
        query = "SELECT * FROM dojos WHERE id=%(id)s;"
        result = connectToMySQL(app.DATABASE).query_db(
            query, {'id': int(dojo_id)})
        return cls(result[0])

    # Update
    @classmethod
    def update(cls, data) -> None:
        query = "UPDATE dojos SET name=%(name)s WHERE id=%(id)s;"
        return connectToMySQL(app.DATABASE).query_db(query, data)

    # Destroy
    @classmethod
    def delete(cls, dojo_id) -> None:
        query = "DELETE FROM dojos WHERE id=%(id)s;"
        return connectToMySQL(app.DATABASE).query_db(query, {'id': int(dojo_id)})

    @classmethod
    def get_dojo_with_ninjas(cls, dojo_id):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id=%(id)s;"
        results = connectToMySQL(app.DATABASE).query_db(
            query, {'id': int(dojo_id)})
        dojo = cls(results[0])
        for row_data in results:
            ninja_data = {
                "id": row_data['ninjas.id'],
                "first_name": row_data['first_name'],
                "last_name": row_data['last_name'],
                "age": row_data['age'],
                "dojo_id": dojo.id,
                "created_at": row_data['ninjas.created_at'],
                "updated_at": row_data['ninjas.updated_at'],
            }
            dojo.ninjas.append(model_ninja.Ninja(ninja_data))
        return dojo
