from flask_app.config.mysqlconnection import connectToMySQL

class Book():
    def __init__(self, data):
        self.author_id = data['author_id']
        self.book_id = data['book_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
