from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from app import app, db
from app.models import User, Book
from werkzeug.security import check_password_hash
import spacy


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        user = User(username=username, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        flash('Account created successfully! You can now log in.', 'success')
        return redirect(url_for('login'))
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            login_user(user)
            flash('Logged in successfully!', 'success')
            return redirect(url_for('profile'))
        else:
            flash('Login failed. Check your email and/or password.', 'danger')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully.', 'info')
    return redirect(url_for('login'))

@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html')



# Load SpaCy model
nlp = spacy.load("en_core_web_sm")

@app.route('/add_book', methods=['GET', 'POST'])
@login_required
def add_book():
    if request.method == 'POST':
        title = request.form.get('title')
        author = request.form.get('author')
        genre = request.form.get('genre')
        status = request.form.get('status')
        book = Book(title=title, author=author, genre=genre, status=status, owner=current_user)
        db.session.add(book)
        db.session.commit()
        flash('Book added successfully!', 'success')
        return redirect(url_for('profile'))
    return render_template('add_book.html')

@app.route('/recommendations', methods=['GET', 'POST'])
@login_required
def recommendations():
    recommendations = []
    if request.method == 'POST':
        keywords = request.form.get('keywords')
        doc = nlp(keywords)
        # Example: In a real app, you would use the keywords to query a book database or API
        # Here, we'll just provide dummy recommendations based on keywords
        if "mystery" in keywords.lower():
            recommendations = ["The Da Vinci Code", "Gone Girl"]
        elif "sci-fi" in keywords.lower():
            recommendations = ["Dune", "Neuromancer"]
        # Add more recommendations based on keywords
    return render_template('recommendations.html', recommendations=recommendations)

@app.route('/my_books')
@login_required
def my_books():
    books = Book.query.filter_by(user_id=current_user.id).all()
    return render_template('my_books.html', books=books)