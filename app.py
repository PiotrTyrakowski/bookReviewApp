from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    reviews = db.relationship('Review', backref='book', lazy=True, cascade="all, delete")


class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(200), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)

@app.route('/')
def index():
    books = Book.query.all()
    return render_template('index.html', books=books)

@app.route('/add_book', methods=['POST'])
def add_book():
    title = request.form.get('title')
    new_book = Book(title=title)
    db.session.add(new_book)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/add_review/<int:book_id>', methods=['POST'])
def add_review(book_id):
    book = Book.query.get(book_id)
    comment = request.form.get('comment')
    rating = request.form.get('rating')
    review = Review(comment=comment, rating=rating, book=book)
    db.session.add(review)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/delete_book/<int:book_id>')
def delete_book(book_id):
    book = Book.query.get(book_id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete_review/<int:review_id>')
def delete_review(review_id):
    review = Review.query.get(review_id)
    book_id = review.book_id  # to redirect to the same book's page after deletion
    db.session.delete(review)
    db.session.commit()
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)