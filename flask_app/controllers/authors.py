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

@app.route('/authors/<int:author_id>')
def show_authors():
    return render_template('author_show.html')

@app.route('/books/<int:book_id>')
def show_books():
    return render_template('book_show.html')