from flask_app.config.mysqlconnection import connectToMySQL

class Author():
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def select_all_authors(cls):
        query = "SELECT * FROM authors;"
        results = connectToMySQL('books_schema').query_db(query)
        authors = []
        for author in results:
            authors.append(cls(author))
        return authors

    @classmethod
    def insert_author(cls, data):
        query = "INSERT INTO authors (name) VALUES (%(name)s);"
        results = connectToMySQL('books_schema').query_db(query, data)
        return results
