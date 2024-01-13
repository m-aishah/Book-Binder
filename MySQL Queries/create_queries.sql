-- Create the database
CREATE DATABASE BookBinderDB;
-- Use the database
USE BookBinderDB;
-- Create the Reader Table
CREATE TABLE Reader (
    ReaderID INT PRIMARY KEY AUTO_INCREMENT,
    Username VARCHAR(20) UNIQUE NOT NULL,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    PasswordHash VARCHAR(300) NOT NULL,
    -- Using bycrypt hashing algorithm
    Email VARCHAR(100) UNIQUE NOT NULL,
    Bio TEXT
);
-- Create the Author Table
CREATE TABLE Author (
    AuthorID INT PRIMARY KEY AUTO_INCREMENT,
    Username VARCHAR(20) UNIQUE NOT NULL,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    PasswordHash VARCHAR(300) NOT NULL,
    -- Using bycrypt hashing algorithm
    Email VARCHAR(100) UNIQUE NOT NULL,
    About TEXT
);
-- Create the Book Table
CREATE TABLE Book (
    BookID INT PRIMARY KEY AUTO_INCREMENT,
    Title VARCHAR(100) NOT NULL,
    AuthorID INT,
    YearReleased INT,
    Genre VARCHAR(50),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT fk_author FOREIGN KEY (AuthorID) REFERENCES Author(AuthorID),
    CONSTRAINT unique_title UNIQUE (Title, AuthorID)
);
-- Create Reader Bookshelf Table
CREATE TABLE ReaderBookshelf (
    BookID INT,
    ReaderID INT,
    Rating SMALLINT,
    DateInserted TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_book FOREIGN KEY (BookID) REFERENCES Book(BookID) ON DELETE CASCADE,
    CONSTRAINT fk_reader FOREIGN KEY (ReaderID) REFERENCES Reader(ReaderID) ON DELETE CASCADE
);
CREATE INDEX idx_title ON Book (Title);
CREATE INDEX idx_author_id ON Book (AuthorID);