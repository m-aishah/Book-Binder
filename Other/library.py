import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk  # pip install pillow

class LibraryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")

        # Create a navigation bar
        self.create_navigation_bar()

        # Create a book gallery
        self.create_book_gallery()

        # Create reviews section
        self.create_reviews_section()

    def create_navigation_bar(self):
        '''Creates a nav bar.'''
        # Create a frame for the navigation bar
        nav_frame = ttk.Frame(self.root)
        nav_frame.pack(side=tk.TOP, fill=tk.X)

        # Add buttons to the navigation bar with even distribution
        reader_btn = ttk.Button(nav_frame, text="Reader", command=self.show_reader_books)
        reader_btn.pack(side=tk.LEFT, padx=(10, 20))

        author_btn = ttk.Button(nav_frame, text="Author", command=self.show_author_books)
        author_btn.pack(side=tk.LEFT, padx=(20, 20))

        all_books_btn = ttk.Button(nav_frame, text="See all books", command=self.show_all_books)
        all_books_btn.pack(side=tk.LEFT, padx=(20, 20))

        all_authors_btn = ttk.Button(nav_frame, text="See all authors", command=self.show_all_authors)
        all_authors_btn.pack(side=tk.LEFT, padx=(20, 10))

    def create_book_gallery(self):
        # Create a frame for the book gallery
        book_gallery_frame = ttk.Frame(self.root)
        book_gallery_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Add a label for book gallery
        gallery_label = ttk.Label(book_gallery_frame, text="Book Gallery")
        gallery_label.pack(side=tk.TOP, pady=10)

        # Create a canvas for book images
        canvas = tk.Canvas(book_gallery_frame, height=300)
        canvas.pack(side=tk.TOP, pady=10)

        book_image_paths = [
            "./images/library_background.jpg",
            "./images/library_background.jpg",
            "./images/library_background.jpg",
            "./images/library_background.jpg",
            "./images/library_background.jpg",
        ]

        # Load and display book images on the canvas
        for i, image_path in enumerate(book_image_paths):
            # Load image using Pillow
            image = Image.open(image_path)
            image = image.resize((100, 150), Image.LANCZOS)  # Resize the image as needed

            # Convert the image to Tkinter format
            tk_image = ImageTk.PhotoImage(image)

            # Create a label to display the image
            book_label = tk.Label(canvas, image=tk_image, padx=10, pady=10, relief=tk.RIDGE, borderwidth=2)
            book_label.grid(row=0, column=i, padx=10)

            # Keep a reference to the image to prevent it from being garbage collected
            book_label.image = tk_image


    def create_reviews_section(self):
        # Create a frame for the reviews section
        reviews_frame = ttk.Frame(self.root)
        reviews_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Add a label for reviews
        reviews_label = ttk.Label(reviews_frame, text="Reviews")
        reviews_label.pack(side=tk.TOP, pady=10)

        # Add reviews by authors and readers
        # You can dynamically load reviews here

    def show_reader_books(self):
        # Implement functionality to show books for readers
        pass

    def show_author_books(self):
        # Implement functionality to show books for authors
        pass

    def show_all_books(self):
        # Implement functionality to show all books
        pass

    def show_all_authors(self):
        # Implement functionality to show all authors
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryApp(root)
    root.mainloop()
