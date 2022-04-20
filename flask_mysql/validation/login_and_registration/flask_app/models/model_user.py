from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app, bcrypt
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class User:
    def __init__(self, data) -> object:
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # Create
    @classmethod
    def save(cls, data) -> int:
        query = "INSERT INTO users ( first_name, last_name, email, password ) VALUES ( %(first_name)s, %(last_name)s, %(email)s, %(password)s );"
        return connectToMySQL(app.DATABASE).query_db(query, data)

    # Read
    @classmethod
    def get_one_from_id(cls, numId) -> object:
        query = "SELECT * FROM users WHERE id=%(id)s;"
        result = connectToMySQL(app.DATABASE).query_db(
            query, {'id': int(numId)})
        return cls(result[0])

    @classmethod
    def get_one_from_email(cls, email) -> object:
        query = "SELECT * FROM users WHERE email=%(email)s;"
        result = connectToMySQL(app.DATABASE).query_db(
            query, {'email': email})
        if result:
            return cls(result[0])
        return None

    @staticmethod
    def validate_new_user(data) -> bool:
        is_valid = True
        if not data['first_name']:
            flash("The first name field is required.", 'register')
            is_valid = False
        if not data['last_name']:
            flash("The last name field is required.", 'register')
            is_valid = False
        if not data['email']:
            flash("The email field is required.", 'register')
            is_valid = False
        if not data['password']:
            flash("The password field is required.", 'register')
            is_valid = False
        if not data['password_confirm']:
            flash("The confirm password field is required.", 'register')
            is_valid = False

        if not is_valid:
            return is_valid

        if len(data['first_name']) < 2:
            flash("First name must be at least 2 characters.", 'register')
            is_valid = False
        if not str.isalpha(data['first_name']):
            flash("First name can only contain letters.", 'register')
            is_valid = False
        if len(data['last_name']) < 2:
            flash("Last name must be at least 2 characters.", 'register')
            is_valid = False
        if not str.isalpha(data['last_name']):
            flash("Last name can only contain letters.", 'register')
            is_valid = False
        if not EMAIL_REGEX.match(data['email']):
            flash("Invalid email.", 'register')
            is_valid = False
        if User.get_one_from_email(data['email']):
            flash('Email is already in use.', 'register')
            is_valid = False
        if len(data['password']) < 8:
            flash("Password must be at least 8 characters.", 'register')
            is_valid = False
        if data['password'] != data['password_confirm']:
            flash("Passwords do not match.", 'register')
            is_valid = False
        return is_valid

    @staticmethod
    def validate_user_login(data) -> bool:
        is_valid = True
        if not data['email']:
            flash("The email field is required.", 'login')
            is_valid = False
        if not data['password']:
            flash("The password field is required.", 'login')
            is_valid = False

        if not is_valid:
            return is_valid

        potential_user = User.get_one_from_email(data['email'])

        if not potential_user:
            flash("Invalid Email/Password", 'login')
            return False

        if not bcrypt.check_password_hash(potential_user.password, data['password']):
            flash("Invalid Email/Password", 'login')
            return False
        return True

    @property
    def full_name(self) -> str:
        return f'{self.first_name} {self.last_name}'
