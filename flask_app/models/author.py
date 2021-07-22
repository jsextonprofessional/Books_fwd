from flask_app.config.mysqlconnection import connectToMySQL

class Author():
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

# selects all authors from DB
    @classmethod
    def select_all_authors(cls):
        query = "SELECT * FROM authors;"
        results = connectToMySQL('books_schema').query_db(query)
        authors = []
        for author in results:
            authors.append(cls(author))
        return authors

# inserts new author to DB
    @classmethod
    def insert_author(cls, data):
        query = "INSERT INTO authors (name) VALUES (%(name)s);"
        results = connectToMySQL('books_schema').query_db(query, data)
        return results

    @classmethod
    def get_book_by_id(cls, data):
        query = "SELECT * FROM authors JOIN books WHERE id = %(author_id)s;"
        result = connectToMySQL('books_schema').query_db(query,data)
        book = Book(result[0])
        return book
