import unittest
from app import app, db, Book, Review
from flask_migrate import Migrate, upgrade
import time

class BookReviewTests(unittest.TestCase):

    # Setup and teardown for each test
    def setUp(self):
        self.app = app
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test_books.db'
        self.client = self.app.test_client()


        with self.app.app_context():
            db.create_all()




    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    # Test adding a book
    def test_add_book(self):
        with self.app.app_context():
            response = self.client.post('/add_book', data=dict(title="Test Book"), follow_redirects=True)
            book = Book.query.first()


            self.assertIsNotNone(book)
            self.assertEqual(book.title, "Test Book")
            self.assertIn(b"Test Book", response.data)

    # Test adding a review
    def test_add_review(self):
        with self.app.app_context():
            book = Book(title="Test Book")
            db.session.add(book)
            db.session.commit()
            response = self.client.post(f'/add_review/{book.id}', data=dict(comment="Great Book!", rating=5),
                                        follow_redirects=True)
            review = db.session.get(Review, 1)


            self.assertIsNotNone(review)
            self.assertEqual(review.comment, "Great Book!")
            self.assertIn(b"Great Book!", response.data)

    # Test deleting a book
    def test_delete_book(self):
        with self.app.app_context():
            book = Book(title="Test Book")
            db.session.add(book)
            db.session.commit()

            self.client.get(f'/delete_book/{book.id}', follow_redirects=True)
            book = db.session.get(Book, book.id)


            self.assertIsNone(book)

    # Test deleting a review
    def test_delete_review(self):

        with self.app.app_context():
            book = Book(title="Test Book")
            db.session.add(book)
            db.session.commit()

            review = Review(comment="Great Book!", rating=5, book_id=book.id)
            db.session.add(review)
            db.session.commit()

            self.client.get(f'/delete_review/{review.id}', follow_redirects=True)
            review = db.session.get(Review, review.id)


            self.assertIsNone(review)


if __name__ == "__main__":
    unittest.main()
