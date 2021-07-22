from flask_app import app
from flask import render_template, request, redirect, session, flash
from flask_app.models.author import Author
from flask_app.models.book import Book

# redirects to authors homepage
@app.route('/')
def index():
    return redirect('/authors')

# authors homepage
@app.route('/authors')
def authors():
    authors = Author.select_all_authors()
    return render_template('authors.html', authors = authors)

# authors POST route to insert new author
@app.route('/authors/insert_author', methods=['POST'])
def insert_author():
    Author.insert_author(request.form)
    return redirect('/')

# books homepage
@app.route('/books')
def books():
    books = Book.select_all_books()
    return render_template('books.html', books = books)

# books POST route to insert new book
@app.route('/books/insert_book', methods=['POST'])
def insert_book():
    Book.insert_book(request.form)
    return redirect('/books')

# author show route to select all favorites of author
@app.route('/authors/<author_id>')
def author_show(author_id):
    data = {
        'id': author_id
    }
    author_id = Author.get_book_by_id
    books = Book.select_all_books()
    return render_template("author_show.html", author_id = author_id, books = books)


@app.route('/books/<int:book_id>')
def show_books():
    return render_template('book_show.html')