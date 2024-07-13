# 📚 Book Binder – A Book Tracking System

![Book Binder Logo](./images/READMEImages/logo.png)

Welcome to **Book Binder**! This is my awesome project where I bring order to the chaotic world of book tracking. Whether you're an avid reader or an author, this app is here to make your life easier.

## Table of Contents

1. [Project Overview](#project-overview)
2. [Why Python?](#why-python)
3. [Database Stuff](#database-stuff)
4. [What It Can Do](#what-it-can-do)
5. [Getting Started](#getting-started)
6. [Screenshots](#screenshots)
7. [My Thoughts](#my-thoughts)
8. [Wrapping Up](#wrapping-up)
9. [Cool Resources](#cool-resources)
10. [Future Plans](#future-plans)

## Project Overview

### 📖 The Backstory

This whole thing started as a project for my COMP 337 DBMS course during the 2nd year Fall Semester at the European University of Lefke. The assignment was to create a simple CRUD app, but why stop there? I decided to go all out and make something extra cool.

### ❓ The Problem

As a book lover, I kept forgetting which books I had read. So, I built **Book Binder**, a slick app that helps readers keep track of their books and lets authors see how popular they are (or aren't).

### 🎯 Goals

- **Readers**: Keep a digital bookshelf.
- **Authors**: See your reader count and average ratings.
- **Me**: Implement CRUD operations and have fun coding!

## Why Python? 🐍

I chose Python because it's easy to work with, has tons of community support, and plays nicely with MySQL. Plus, Python is just plain awesome.

## Database Stuff 💾

### The Database

I went with MySQL for this project because it's robust and I had some prior experience with it. It turned out to be a great choice.

### Relationships

Here's how the database is structured:

- **Reader**: (ReaderID, Username, FirstName, LastName, PasswordHash, Email, Bio)
- **Author**: (AuthorID, Username, FirstName, LastName, PasswordHash, Email, About)
- **Book**: (BookID, Title, AuthorID, YearReleased, Genre, CreatedAt, UpdatedAt)
- **ReaderBookshelf**: (BookID, ReaderID, Rating, DateInserted)

You can check out the SQL queries I used in the [database_queries.sql](path_to_queries_file).

![ER Diagram](path_to_er_diagram_image)

## What It Can Do 🛠️

Here's a list of all the cool stuff this app can do:

- **Add Data**: Sign up as a reader or author, and add books to your shelf.
- **Delete Data**: Remove books from your shelf.
- **Update Data**: Change your ratings for books.
- **View Data**: See your bookshelf or author dashboard.

## Getting Started 🚀

### Prerequisites

Make sure you have the following installed:

- Python 3.x
- MySQL

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/m-aishah/Book-Binder.git
    cd Book-Binder
    ```

2. Install the required Python modules:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up the MySQL database:
    - Create a new database in MySQL.
    - Run the queries in the `database_queries.sql` file to create the necessary tables.

4. Update the database configuration in the code if necessary (e.g., username, password).

5. Run the application:
    ```bash
    python landing_page.py
    ```

## Screenshots 📸

To get started, just run the `landing_page.py` module. Check out some screenshots:

1. **Landing Page**:
   ![Landing Page](path_to_landing_page_image)

2. **Sign Up Prompt**:
   ![Sign Up Prompt](path_to_sign_up_prompt_image)

3. **Reader Bookshelf**:
   ![Reader Bookshelf](path_to_reader_bookshelf_image)

4. **Insert New Book**:
   ![Insert New Book](path_to_insert_new_book_image)

5. **Author's Dashboard**:
   ![Author's Dashboard](path_to_authors_dashboard_image)

## My Thoughts 💭

Working on this project was a blast. It was challenging but incredibly rewarding. I learned a ton about GUI development and database interactions.

## Wrapping Up 🎉

**Book Binder** hit all the goals I set out for it. It provides a slick interface for readers and authors alike. Sure, there were some bumps along the way (like dependency hell), but I’m super proud of how it turned out.

## Cool Resources 📚

- [Python GUI Programming with tkinter](https://realpython.com/python-gui-tkinter/)
- [Tkinter Complete Tutorial](https://realpython.com/python-gui-tkinter/)
- [Project Repository](https://github.com/m-aishah/Book-Binder)

## Future Plans 🔮

Stay tuned for more updates! You can follow the project on my [GitHub repository](https://github.com/m-aishah/Book-Binder).

