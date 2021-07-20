from flask_app import app
from flask import render_template, request, redirect, session, flash
from flask_app.models.author import Author
from flask_app.models.book import Book

@app.route('/')
def index():
    return redirect('/authors')

@app.route('/authors')
def authors():
    return render_template('authors.html')

@app.route('/books')
def books():
    return render_template('books.html')

@app.route('/authors/<int:author_id>')
def show_authors():
    return render_template('author_show.html')

@app.route('/books/<int:book_id>')
def show_books():
    return render_template('book_show.html')