from flask_app.config.mysqlconnection import connectToMySQL


class User:
    def __init__(self, data) -> None:
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('dec_users').query_db(query)
        all_users = [] 
        for one_user_row in results:
            this_user_instance =  cls(one_user_row)
            all_users.append(this_user_instance)
        return all_users

    @classmethod
    def add_user(cls,data):
        query = """
            INSERT INTO users (first_name,last_name,email)
            VALUES (%(first_name)s,%(last_name)s,%(email)s);
        """
        return connectToMySQL('dec_users').query_db(query,data)


    @classmethod
    def get_one(cls,data):
        query = """
            SELECT * from users WHERE users.id = %(id)s;
        """
        results = connectToMySQL('dec_users').query_db(query,data)
        if results:
            return cls(results[0])
        return False


    @classmethod
    def update_user(cls,data):
        query = """
            UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s
            WHERE users.id = %(id)s;
        """
        return connectToMySQL('dec_users').query_db(query,data)

    @classmethod
    def delete(cls,data):
        query = """
            DELETE FROM users where users.id = %(id)s;
        """
        return connectToMySQL('dec_users').query_db(query,data)