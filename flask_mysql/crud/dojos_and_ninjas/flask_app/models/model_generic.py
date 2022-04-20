from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app


class Generic:
    def __init__(self, data) -> object:
        self.id = data['id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # Create
    @classmethod
    def save(cls, data) -> int:
        query = "INSERT INTO generic_table ( created_at, updated_at ) VALUES ( NOW() , NOW() );"
        return connectToMySQL(app.DATABASE).query_db(query, data)

    # Read
    @classmethod
    def get_all(cls) -> list[object]:
        query = "SELECT * FROM generic_table;"
        results = connectToMySQL(app.DATABASE).query_db(query)
        generic_objects = []
        for generic_data in results:
            generic_objects.append(cls(generic_data))
        return generic_objects

    @classmethod
    def get_one(cls, numId) -> object:
        query = "SELECT * FROM generic_table WHERE id=%(id)s;"
        result = connectToMySQL(app.DATABASE).query_db(
            query, {'id': int(numId)})
        return cls(result[0])

    # Update
    @classmethod
    def update(cls, data) -> None:
        query = "UPDATE generic_table SET updated_at=%(updated_at)d WHERE id=%(id)s;"
        return connectToMySQL(app.DATABASE).query_db(query, data)

    # Destroy
    @classmethod
    def delete(cls, numId) -> None:
        query = "DELETE FROM generic_table WHERE id=%(id)s;"
        return connectToMySQL(app.DATABASE).query_db(query, {'id': int(numId)})

    @property
    def generic_property(self) -> str:
        return f'{self.created_at} {self.updated_at}'
