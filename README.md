Library Management System
Author: Hasnain Dehwar
Email: hansaindehwar78@gmail.com
GitHub Username: Hasnai_dehwar

Features
1. Admin Functionalities
Manage Books

Add new books to the library.
Update book information.
Delete books.
View available books and their counts.
Manage Members

Add new members.
Remove members.
View all registered members.
2. Member Functionalities
Borrow a book (with checks on availability).
Return a book (with fine calculation for overdue returns).
View borrowed books and borrowing history.
Database Design
Tables:
Books

book_id: Unique identifier for each book.
title: Title of the book.
author: Author of the book.
Copies_available: Number of available copies.
Members

Member_id: Unique identifier for each member.
Name: Full name of the member.
email: Email address of the member.
phone: Contact number of the member.
Transactions

transaction_id: Unique identifier for each transaction.
Member_id: Foreign key linking to Members.
book_id: Foreign key linking to Books.
borrow_date: Date when the book was borrowed.
return_date: Date when the book was returned.
fine: Fine imposed for overdue returns.
How to Run the Project
Clone the Repository

git clone https://github.com/Hasnai_dehwar/Library-Management-System.git
cd Library-Management-System
Install Dependencies
Ensure Python and MySQL are installed on your system. Install required libraries:

pip install mysql-connector-python
Set Up the Database

Import the SQL file (library.sql) provided in the repository to create the database and tables.
Update the Database.connect_db() method in the Database module with your database credentials.

Admin:

Use the admin panel to add or manage books and members.
Members:

Borrow and return books.
Ensure books are returned on time to avoid fines.
Folder Structure
Library-Management-System
│
├── books.py              # Manages book-related functionalities.
├── members.py            # Manages member-related functionalities.
├── borrow_return.py      # Handles borrowing and returning of books.
├── database.py           # Database connection and queries.
├── main.py               # Entry point for the application.
├── README.md             # Project documentation.
└── library.sql           # SQL script to create database and tables.
License
This project is licensed under the MIT License. See LICENSE for more details.
