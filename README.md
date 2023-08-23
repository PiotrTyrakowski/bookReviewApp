# Book Review App Documentation

## Table of Contents
- [Introduction](#introduction)
- [Setup and Installation](#setup-and-installation)
- [Features](#features)
- [Application Structure](#application-structure)
- [Testing](#testing)
- [Future Enhancements](#future-enhancements)
- [FAQ](#faq)

## 1. Introduction
The Book Review App is a web-based application designed to catalog books and their respective reviews. Built using Flask, SQLAlchemy, and SQLite, it serves as a demonstration of CRUD (Create, Read, Update, Delete) operations in a web application context.

## 2. Setup and Installation
**Requirements:**
- Python (3.x recommended)
- Flask
- Flask-SQLAlchemy
- Flask-Migrate

**Steps:**
1. Clone the repository or download the source code.
2. Install the required packages:
   ```bash
   pip install Flask Flask-SQLAlchemy Flask-Migrate
3. Initialize the database:
   ```bash
   flask db init
   flask db migrate -m "Initial migration."
   flask db upgrade
4. Run the application:
   ```bash
   python app.py

## 3. Features
- Add Books: Users can add new books to the catalog.
- Review Books: For each book, users can add reviews which include a rating and a comment.
- List Books & Reviews: All books and their respective reviews are listed on the homepage.
- Delete Books: Books can be deleted from the catalog. All related reviews get automatically deleted.
- Delete Reviews: Specific reviews can be removed individually.

## 4. Application Structure

- Backend (Python with Flask): Main application logic, database interactions, and routing are managed here.

- Models:
- Book: Represents a book entity with attributes like title.
- Review: Represents a review entity with attributes like comment, rating, and a foreign key relationship to Book.
- Routes:
  - Home (/): Displays all books and reviews.
  - Add Book (/add_book): Endpoint to add a new book.
  - Add Review (/add_review/<int:book_id>): Endpoint to add a review to a specific book.
  - Delete Book (/delete_book/<int:book_id>): Endpoint to delete a specific book and its associated reviews.
  - Delete Review (/delete_review/<int:review_id>): Endpoint to delete a specific review.
  - Frontend (HTML with Bootstrap): The visual interface of the application, using templating to render dynamic content.
  -Database (SQLite with SQLAlchemy): Data persistence layer. Uses SQLAlchemy ORM to map Python classes to database tables and vice versa.

## 5. Testing
The Book Review App incorporates a series of tests to ensure its core functionalities work as expected. The tests are written using Python's built-in unittest library.

To execute the tests, run the script containing the test cases. The tests cover the following functionalities:
- Adding a book.
- Adding a review.
- Deleting a book.
- Deleting a review.
  
Refer to the testing script provided for detailed test case implementations.

## 6. Future Enhancements
- User Authentication: Add the ability for users to register, login, and manage their reviews.
- Search Feature: Implement a search feature for users to easily find books or specific reviews.
- Book Details API Integration: Retrieve detailed information about books from external sources.
## 7. FAQ

Q: How can I contribute to the project?

A: Contributions are always welcome! Please fork the repository, make your changes, and submit a pull request.
