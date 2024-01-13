'''Connect to mysql server.'''
import hashlib
import mysql.connector


# Connect to the database.
db = mysql.connector.connect(
    host='localhost',
    passwd='Password(2540)',
    user='root',
    port=33061,
    database='BookBinderDB'
)

my_cursor = db.cursor()



def hash_password(password):
        '''
        Hash the password using a secure hashing algorithm.
        
        Args:
        password (str): The password to be hashed.

        Returns: The hashed password.
        '''
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        return hashed_password

def get_username(ID, table):
        '''
        Returns the username of a Reader/Author.

        Args:
        ID (str): The ID of the Reader/Author.
        table (str): The table to get the username from (Reader/ Author).

        Returns: Username of a Reader/Author on success, else None.
        '''
        try:
                ID_clause = table + "ID"
                query = "SELECT Username \
                         FROM {} \
                         WHERE {} = %s".format(table, ID_clause)
                values = (ID,)

                my_cursor.execute(query, values)
                username = my_cursor.fetchone()[0]
                return username
        except Exception as e:
                print("Error:{}".format(e))
                return None
                

def insert_reader_in_database(username, first_name, last_name, password, email, bio):
        '''
        Insert info about new reader into the Reader table of the database.

        Args:
        username (str): The username of the reader.
        first_name (str): The first name of the reader.
        last_name (str): The last name of the reader.
        password (str): The password of the reader.
        email (str): Email of the reader.
        bio (str): A little bio about the reader.


        Returns: The new reader's ID on success, else 0.
        '''
        try:
                # Check if the username already exists.
                check_query = "SELECT ReaderID \
                        FROM Reader \
                        WHERE Username = %s"
                check_values = (username,)
                my_cursor.execute(check_query, check_values)
                existing_reader = my_cursor.fetchone()

                if existing_reader:
                        print("Username already exists. Choose a different username.")
                        return 0

                # Hash the password using bcrypt.
                hashed_password = hash_password(password)

                # Insert into the Reader table.
                insert_query = "INSERT INTO Reader (Username, FirstName, LastName, PasswordHash, Email, Bio) \
                                VALUES (%s, %s, %s, %s, %s, %s)"
                insert_values = (username, first_name, last_name, hashed_password, email, bio)
                my_cursor.execute(insert_query, insert_values)
                db.commit()

                print("Reader successfully inserted into the database.")

                # Get the inserted ReaderID for reference.
                my_cursor.execute(check_query, check_values)
                new_reader_id = my_cursor.fetchone()[0]

                return new_reader_id
        # Handle any errors.
        except Exception as e:
                print("Error inserting reader into the database: {}".format(e))
                return -1

        

def validate_reader(username, password):
        '''
        Check that the user exists in the database.
        
        Args:
        username (str): The username of the reader to be validated.
        password (str): The password of the reader to be validated.

        Returns: The ReaderID on success, else 0.
        '''
        hashed_password = hash_password(password)

        query = "SELECT ReaderID \
                FROM Reader \
                WHERE Username = %s AND PasswordHash = %s"
        values = (username, hashed_password)
        
        my_cursor.execute(query, values)
        result = my_cursor.fetchone()
        
        if not result:
                return 0
        reader_id = result[0]
        return reader_id


def fetch_books_for_reader(ReaderID, search_query=None):
        '''
        Fetches data on books in a Reader' bookshelf 
        (sometimes only books matching a search query)
        
        Args:
        ReaderID (str): The ID of the reader in question.
        search_query (str): The search query (optional).
        
        Returns: A list - each index of the list is a dictionary of data about a book.
        '''
        try:
                if search_query:
                        fetch_query = "SELECT Book.Title AS BookName, \
                                        CONCAT(Author.FirstName, ' ', Author.LastName) AS AuthorName, \
                                        ReaderBookshelf.DateInserted, \
                                        ReaderBookshelf.Rating \
                                FROM ReaderBookshelf \
                                JOIN Book ON ReaderBookshelf.BookID = Book.BookID \
                                JOIN Author ON Book.AuthorID = Author.AuthorID \
                                WHERE ReaderBookshelf.ReaderID = %s \
                                AND (LOWER(Book.Title) LIKE %s OR LOWER(Author.FirstName) LIKE %s OR LOWER(Author.LastName) LIKE %s);"

                        fetch_values = (
                                                ReaderID,
                                                "%{}%".format(search_query.lower()),
                                                "%{}%".format(search_query.lower()),
                                                "%{}%".format(search_query.lower())
                                        )
                else:
                        fetch_query = "SELECT Book.Title AS BookName, \
                                        CONCAT(Author.FirstName, ' ', Author.LastName) AS AuthorName, \
                                        ReaderBookshelf.DateInserted, \
                                        ReaderBookshelf.Rating \
                                FROM ReaderBookshelf \
                                JOIN Book ON ReaderBookshelf.BookID = Book.BookID \
                                JOIN Author ON Book.AuthorID = Author.AuthorID \
                                WHERE ReaderBookshelf.ReaderID = %s;"

                        fetch_values = (ReaderID,)

                my_cursor.execute(fetch_query, fetch_values)
                books = my_cursor.fetchall()

                books_for_user = []
                for book in books:
                        book_dict = {
                                "BookName": book[0],
                                "AuthorName": book[1],
                                "DateInserted": book[2],
                                "Rating": book[3]
                        }
                        books_for_user.append(book_dict)
                
                return books_for_user
        
        except Exception as e:
                print("Error fetching books for reader: {}".format(e))
                return []

def insert_book_for_reader(ReaderID, book_title, author_name, rating):
        '''
        Insert a new book into the ReaderBookshelf relation.

        Args:
        ReaderID (str): The ID of the Reader.
        book_title (str): The title of the book.
        author_name (str): The name of the author of the book.
        rating (str): The reader's rating of the book.

        Returns: 1 on success, 0 on failure.
        '''
        try:
                # Check if the book already exists in the Book table.
                query_book = "SELECT BookID, AuthorID FROM Book WHERE Title = %s AND AuthorID IN (SELECT AuthorID FROM Author WHERE CONCAT(FirstName, ' ', LastName) = %s)"
                values_book = (book_title, author_name)

                my_cursor.execute(query_book, values_book)
                book_info = my_cursor.fetchone()

                if book_info:
                        BookID, AuthorID = book_info
                else:
                        # If the book doesn't exist, insert it into the Book table.
                        insert_book_query = "INSERT INTO Book (Title, AuthorID) VALUES (%s, (SELECT AuthorID FROM Author WHERE CONCAT(FirstName, ' ', LastName) = %s))"
                        insert_book_values = (book_title, author_name)

                        my_cursor.execute(insert_book_query, insert_book_values)
                        db.commit()

                        # Retrieve the newly inserted BookID.
                        my_cursor.execute("SELECT LAST_INSERT_ID()")
                        BookID = my_cursor.fetchone()[0]

                # Insert the Book into the ReaderBookshelf.
                insert_query = "INSERT INTO ReaderBookshelf (BookID, ReaderID, Rating) VALUES (%s, %s, %s)"
                insert_values = (BookID, ReaderID, rating)

                my_cursor.execute(insert_query, insert_values)
                db.commit()
                
                print("Book successfully inserted into the ReaderBookshelf Table.")
                return 1

        except Exception as e:
                print("Error inserting book for user: {}".format(e))
                return 0


def update_book_rating_for_reader(ReaderID, book_title, author_name, new_rating):
        '''
        Updates the rating of a book in the ReaderBookshelf relation.

        Args:
        ReaderID (str): The ID of the Reader.
        book_title (str): The title of the book.
        author_name (str): The name of the author of the book.
        new_rating (str): The reader's new rating of the book.

        Returns: 1 on success, 0 on failure.
        '''
        try:
                # Get BookID from the Book table.
                query = "SELECT BookID \
                        FROM Book \
                        JOIN Author ON Book.AuthorID = Author.AuthorID \
                        WHERE Title = %s"
                values = (book_title,)

                my_cursor.execute(query, values)
                BookID = my_cursor.fetchone()

                if not BookID:
                        print("Book not found.")
                        return 0

                # Update the rating in the ReaderBookshelf.
                update_query = "UPDATE ReaderBookshelf \
                                SET Rating = %s \
                                WHERE BookID = %s AND ReaderID = %s"
                update_values = (new_rating, BookID[0], ReaderID)

                my_cursor.execute(update_query, update_values)
                db.commit()

                print("Rating successfully updated in ReaderBookshelf.")
                return 1
        except Exception as e:
                print("Error updating rating for reader: {}".format(e))


def delete_book_from_reader_bookshelf(ReaderID, book_title, author_name):
        '''
        Removes a book from the ReaderBookshelf relation.

        Args:
        ReaderID (str): The ID of the Reader.
        book_title (str): The title of the book.
        author_name (str): The name of the author of the book.

        Returns: True on success, False on failure.
        '''
        try:
                # Get BookID from the Book table.
                query = "SELECT BookID \
                        FROM Book \
                        JOIN Author ON Book.AuthorID = Author.AuthorID \
                        WHERE Title = %s AND CONCAT(Author.FirstName, ' ', Author.LastName) = %s"
                values = (book_title, author_name)

                my_cursor.execute(query, values)
                book_id = my_cursor.fetchone()

                if not book_id:
                        # The book is not found in the Book table.
                        return False

                # Delete the book from the ReaderBookshelf.
                delete_query = "DELETE FROM ReaderBookshelf \
                                WHERE BookID = %s AND ReaderID = %s"
                delete_values = (book_id[0], ReaderID)

                my_cursor.execute(delete_query, delete_values)
                db.commit()

                print("Book successfully deleted from the ReaderBookshelf Table.")
                return True

        except Exception as e:
                print("Error deleting book from bookshelf: {}".format(e))
                return False



def insert_author_in_database(username, first_name, last_name, password, email, about):
        '''
        Insert a new author into the Author relation.

        Args:
        username (str): The username of the Author.
        first_name (str): The author's first name.
        last_name (str): The author's last name.
        password (str): The author's password.
        email (str): The author's email address.
        about (str): A little bio of the author.

        Returns: the author;s ID on success, 0 on failure.
        '''
        try:
                # Check if the username already exists.
                check_query = "SELECT AuthorID \
                        FROM Author \
                        WHERE Username = %s"
                check_values = (username,)
                my_cursor.execute(check_query, check_values)
                existing_reader = my_cursor.fetchone()

                if existing_reader:
                        print("Username already exists. Choose a different username.")
                        return 0

                # Hash the password using bcrypt.
                hashed_password = hash_password(password)

                # Insert into the Reader table.
                insert_query = "INSERT INTO Author (Username, FirstName, LastName, PasswordHash, Email, About) \
                                VALUES (%s, %s, %s, %s, %s, %s)"
                insert_values = (username, first_name, last_name, hashed_password, email, about)
                my_cursor.execute(insert_query, insert_values)
                db.commit()

                print("Author successfully inserted into the database.")

                # Get the inserted ReaderID for reference.
                my_cursor.execute(check_query, check_values)
                new_author_id = my_cursor.fetchone()[0]

                return new_author_id
        except Exception as e:
                print("Error inserting reader into the database: {}".format(e))
                return -1

def validate_author(username, password):
        '''
        Check that the user exists in the database.
        
        Args:
        username (str): The username of the author to be validated.
        password (str): The author's password.
        
        Returns: the author's ID if in the database, else 0.
        '''
        hashed_password = hash_password(password)

        query = "SELECT AuthorID \
                FROM Author \
                WHERE Username = %s AND PasswordHash = %s"
        values = (username, hashed_password)
        
        my_cursor.execute(query, values)
        result = my_cursor.fetchone()
        
        if not result:
                return 0
        author_id = result[0]
        return author_id

def fetch_books_for_author(AuthorID, search_query="None"):
        '''
        Fetches info relating to an author
        (and sometimes a search query).

        Args: 
        AuthorID (str): The ID of the author.
        search_query (str): A search query.
        '''
        try:
                if search_query.lower() != "none":
                        fetch_query = "SELECT Book.Title AS BookName, \
                                        COUNT(ReaderBookshelf.ReaderID) AS NumberOfReaders, \
                                        AVG(ReaderBookshelf.Rating) AS AverageRating \
                                FROM ReaderBookshelf \
                                JOIN Book ON ReaderBookshelf.BookID = Book.BookID \
                                WHERE Book.AuthorID = %s \
                                AND (LOWER(Book.Title) LIKE %s OR LOWER(Book.Genre) LIKE %s) \
                                GROUP BY Book.BookID;"

                        fetch_values = (
                                                AuthorID,
                                                "%{}%".format(search_query.lower()),
                                                "%{}%".format(search_query.lower())
                                        )
                else:
                        fetch_query = "SELECT Book.Title AS BookName, \
                                        COUNT(ReaderBookshelf.ReaderID) AS NumberOfReaders, \
                                        AVG(ReaderBookshelf.Rating) AS AverageRating \
                                FROM ReaderBookshelf \
                                JOIN Book ON ReaderBookshelf.BookID = Book.BookID \
                                WHERE Book.AuthorID = %s \
                                GROUP BY Book.BookID;"

                        fetch_values = (AuthorID,)

                my_cursor.execute(fetch_query, fetch_values)
                books = my_cursor.fetchall()

                books_for_author = []
                for book in books:
                        book_dict = {
                                "BookName": book[0],
                                "NumberOfReaders": int(book[1]),
                                "AverageRating": round(float(book[2]), 2)
                        }
                        books_for_author.append(book_dict)

                return books_for_author

        except Exception as e:
                print("Error fetching books for author: {}".format(e))
                return []
