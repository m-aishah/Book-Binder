'''
Defines Structure of Reader part of the app.

ReaderAuth (class): Structure/design of the reader Login Window.
ReaderBookshelf (class): Structure/Design of the Reader's Book shelf.
''' 
from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from PIL import Image, ImageTk, ImageFilter 

from page_setup import initial_page_setup
from database import *

# Create a search button with a ttk style
style = ttk.Style()
style.configure('Buttons.TButton',
                font=('Palatino Linotype', 14, 'bold'),
                background='#FFB6C1',
                foreground='black',
                borderwidth=0,
                relief='flat',
                padding=(10, 10))
# Hover configuration.
style.map('Buttons.TButton',
            background=[('active', 'silver')],
            foreground=[('active', 'white')])

class ReaderAuth:
    def __init__(self, parent):
        '''
        Creates an instance of the ReaderAuth class for the Login Page.
        '''
        self.parent = parent
        self.create_login_window()

    def create_login_window(self):
        '''
        Defines structure/design of the Login Page.
        '''
        self.login_window = initial_page_setup (self, self.parent, "Reader", "Reader Login")
        
        # Main frame.
        self.bg_frame = Frame(self.login_window, bg='white', width=1166, height=718)
        self.bg_frame.pack(fill='both', expand='yes')

        # Login frame.
        self.login_frame = Frame(self.bg_frame, bg='white', width=950, height=700)
        self.login_frame.place(x=450, y=100)

        # Slogan in Login frame.
        self.slogan = "\"Reading from the heart\""
        self.heading = Label(self.login_frame, text=self.slogan, 
                             font=('Palatino Linotype', 20, 'italic bold'),
                             bg='white', fg='#de984e', bd=5, relief=FLAT)
        self.heading.place(x=35, y=20, width=400, height=30)

        # Side image in Login frame.
        self.side_image = Image.open('./images/ReaderLogin/side_image.png')
        photo = ImageTk.PhotoImage(self.side_image)
        self.side_image_label = Label(self.login_frame, image=photo, bg='white')
        self.side_image_label.image = photo
        self.side_image_label.place(x=5, y=100)

        # Sign In icon.
        self.sign_in_image = Image.open('./images/ReaderLogin/sign_in.png')
        photo = ImageTk.PhotoImage(self.sign_in_image)
        self.sign_in_image_label = Label(self.login_frame, image=photo, bg='white')
        self.sign_in_image_label.image = photo
        self.sign_in_image_label.place(x=650, y=135)

        # Sign In label.
        self.sign_in_label = Label(self.login_frame, text="Sign In",
                                   font=('yu gothic ui', 14, 'bold'),
                                   bg='white', fg='#696868')
        self.sign_in_label.place(x=650, y=207)

        # Add widgets for reader login
        # Username
        #Label
        self.username_label = Label(self.login_frame, text="Username",
                                   font=('yu gothic ui', 13, 'bold'),
                                    bg='white', fg='#ccbfb1')
        self.username_label.place(x=550, y=300)
        # Entry
        self.username_entry = Entry(self.login_frame, highlightthickness=0,
                                    font=('yu gothic ui', 12, 'bold'), 
                                    insertbackground = '#6b6a69', relief=FLAT, 
                                    bg='white', fg='#696868')
        self.username_entry.place(x=580, y=335, width=270, height=30)
        # Line
        self.username_line = Canvas(self.login_frame, width=300, height=2.0,
                                    bg='#bdb9b1', highlightthickness=0)
        self.username_line.place(x=550, y=361)
        # Icon
        self.username_icon = Image.open('./images/ReaderLogin/username_icon.png')
        photo = ImageTk.PhotoImage(self.username_icon)
        self.username_icon_label = Label(self.login_frame, image=photo, bg='white')
        self.username_icon_label.image = photo
        self.username_icon_label.place(x=550, y=335)
        
        # Password
        # Label
        self.password_label = Label(self.login_frame, text="Password",
                                    font=('yu gothic ui', 13, 'bold'),
                                    bg='white', fg='#ccbfb1')
        self.password_label.place(x=550, y=380)
        # Entry
        self.password_entry = Entry(self.login_frame, highlightthickness=0,
                                    font=('yu gothic ui', 12, 'bold'),
                                    show="*", insertbackground = '#6b6a69',
                                    relief=FLAT, bg='white', fg='#696868',)
        self.password_entry.place(x=580, y=416, width=244, height=30)
        # Line
        self.password_line = Canvas(self.login_frame, width=300, height=2.0, 
                                    bg='#bdb9b1', highlightthickness=0)
        self.password_line.place(x=550, y=442)
        # Icon
        self.password_icon = Image.open('./images/ReaderLogin/password_icon.png')
        photo = ImageTk.PhotoImage(self.password_icon)
        self.password_icon_label = Label(self.login_frame, image=photo, bg='#040405')
        self.password_icon_label.image = photo
        self.password_icon_label.place(x=550, y=417)
        # Show/Hide Password
        self.show_image = ImageTk.PhotoImage(file='./images/ReaderLogin/pswd_hide.png')
        self.hide_image = ImageTk.PhotoImage(file='./images/ReaderLogin/pswd_show.png')
        self.show_button = Button(self.login_frame, image=self.show_image, command=self.show, 
                                  relief=FLAT, activebackground='#f7ebed' ,borderwidth=0, 
                                  background='white', cursor='hand2')
        self.show_button.place(x=860, y=420)

        # ReaderLogin Button
        self.login_button = Image.open('./images/ReaderLogin/login_button.png')
        photo = ImageTk.PhotoImage(self.login_button)
        self.login_button_label = Label(self.login_frame, image=photo, bg='white', cursor='hand2')
        self.login_button_label.image = photo
        self.login_button_label.place(x=550, y=480)
        self.login_button_label.bind("<Button-1>", self.reader_login_action)

        self.forgot_button = Button(self.login_frame, text="Forgot Password ?",
                                    font=('yu gothic ui', 9, 'italic underline'), fg='#ccbfb1', relief=FLAT,
                                    borderwidth=0, activebackground='#f7ebed', background='white', cursor='hand2',
                                    activeforeground='#ccbfb1', command=self.show_forgot_password_window)
        self.forgot_button.place(x=550, y=580)

                            # Bind an event to enable/disable the login button based on the entry content
                            #self.username_entry.bind("<KeyRelease>", self.toggle_login_button_state)
                            #self.toggle_login_button_state(None)
        # Login frame Hover events.
        self.login_frame.bind("<Enter>", self.on_enter)
        self.login_frame.bind("<Leave>", self.on_leave)


    def on_enter(self, event):
        '''
        Changes the background color of a frame/label/button to pink when the cursor is over it (Hover feature).
        '''
        self.login_frame.configure(bg='#f7ebed')
        self.heading.configure(bg='#f7ebed')
        self.side_image_label.configure(bg='#f7ebed')

        self.sign_in_image_label.configure(bg='#f7ebed')
        self.sign_in_label.configure(bg='#f7ebed')

        self.username_label.configure(bg='#f7ebed')
        self.username_entry.configure(bg='#f7ebed')
        self.username_icon_label.configure(bg='#f7ebed')

        self.password_label.configure(bg='#f7ebed')
        self.password_entry.configure(bg='#f7ebed')
        self.password_icon_label.configure(bg='#f7ebed')

        self.show_button.configure(bg='#f7ebed')
        #self.hide_button.configure(bg='#f7ebed')

        self.login_button_label.configure(bg='#f7ebed')

        self.forgot_button.configure(bg='#f7ebed')

        

    def on_leave(self, event):
        '''
        Changes the background color of a frame/label/button to white when the cursor is not on it (Hover feature).
        '''
        self.login_frame.configure(bg='white')
        self.heading.configure(bg='white')
        self.side_image_label.configure(bg='white')

        self.sign_in_image_label.configure(bg='white')
        self.sign_in_label.configure(bg='white')

        self.username_label.configure(bg='white')
        self.username_entry.configure(bg='white')
        self.username_icon_label.configure(bg='white')

        self.password_label.configure(bg='white')
        self.password_entry.configure(bg='white')
        self.password_icon_label.configure(bg='white')
        self.show_button.configure(bg='white')
        #self.hide_button.configure(bg='white')

        self.login_button_label.configure(bg='white')

        self.forgot_button.configure(bg='white')

    def show(self):
        '''
        Configure the show password feature for the password entry.
        '''
        self.hide_button = Button(self.login_frame, image=self.hide_image, command=self.hide, relief=FLAT,
                                  activebackground='#f7ebed'
                                  , borderwidth=0, background='white', cursor='hand2')
        self.hide_button.place(x=860, y=420)
        self.password_entry.config(show='')

    def hide(self):
        '''
        Configure the hide password feature for the password entry.
        '''
        self.show_button = Button(self.login_frame, image=self.show_image, command=self.show, relief=FLAT,
                                  activebackground='#f7ebed'
                                  , borderwidth=0, background='white', cursor='hand2')
        self.show_button.place(x=860, y=420)
        self.password_entry.config(show='*')

                                        # CHECK THIS!!! AND FIX IT.
    #def toggle_login_button_state(self, event):
     #   '''
      #  Enables the login button only if a username is entered.
       # '''
        #username = self.username_entry.get()
        #password = self.password_entry.get()
        #if username and password:
         #   self.login_button_label["state"] = tk.NORMAL
        #else:
         #   self.login_button_label["state"] = tk.DISABLED

    def reader_login_action(self, event):
        '''
        Perform necessary action after logging in.
        (1) Destroy the login window.
        (2) Validate user.
        (3) Create the Reader Bookshelf window.
        '''
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Check database if username exists with correct password if not print error message.
        if not username:
            messagebox.showerror("Invalid Username", "Please enter a username!")
            return 
        if not password:
            messagebox.showerror("Invalid Password", "Please enter a password!")
            return

        # Check that the user is in the database.
        ReaderID = validate_reader(username, password)
        if not ReaderID:
            messagebox.showerror("Invalid Login Details", "User does not exist")
            return 

        # Close the login window after successful login.
        self.login_window.destroy()

        # Open a new window to display the list of books.
        reader_bookshelf = ReaderBookshelf(self.parent, ReaderID)

    def show_forgot_password_window(self, event):
            # Implement functionality to show the forgot password window
            print("Forgot Password clicked")

class ReaderBookshelf:
    '''List of books in a reader's bookshelf.'''
    def __init__(self, parent, ReaderID):
        '''
        Create an instance of the Reader Book shelf window.
        (Displays all the books the reader has added to his/her bookshelf).

        Args:
        parent (Tk): The window from which the button ws clicked i.e the login window.
        ReaderID (int): The ID of the Reader whose bookshelf is to be displayed.
        '''
        self.parent = parent
        self.ReaderID = ReaderID
        self.create_bookshelf_window()

    def create_bookshelf_window(self):
        ''''
        Create a new window to display the list of books.
        '''
        self.bookshelf_window = initial_page_setup (
                                                    self, 
                                                    self.parent, 
                                                    "ReaderBookshelf", 
                                                    "Reader Bookshelf"
                                                )
        # Create a frame for the info area
        info_frame = Frame(self.bookshelf_window, bg='white', highlightthickness=0)
        info_frame.place(x=50, y=40, width=400, height=100)

        # Add profile picture (replace 'path_to_profile_pic' with the actual path)
        profile_pic_path = './images/ReaderLogin/profile_pic.png'
        profile_pic = PhotoImage(file=profile_pic_path)
        profile_label = Label(info_frame, image=profile_pic, bg='white')
        profile_label.image = profile_pic
        profile_label.pack(side=tk.LEFT, padx=0)

        # Add username and bio
        username = get_username(self.ReaderID, "Reader")
        username_label = Label(info_frame, text="{}'s Bookshelf".format(username), font=('Palatino Linotype', 12, 'bold'), bg='white')
        username_label.pack(side=tk.LEFT, padx=10)
        

        # Create a frame for the search bar
        search_frame = Frame(self.bookshelf_window, bg='white', highlightthickness=0)
        search_frame.place(x=670, y=50, width=700, height=50)

        # Create a search entry widget
        self.search_entry = Entry(search_frame, font=('yu gothic ui', 15), width=30)
        self.search_entry.pack(side=tk.LEFT, padx=10)

        search_button = ttk.Button(search_frame, text="Search", command=self.perform_search, style='Buttons.TButton')
        search_button.pack(side=tk.LEFT, padx=10)


        # Create a frame to hold the book list
        self.book_list_frame = Frame(self.bookshelf_window, bg='white', highlightthickness=1)
        self.book_list_frame.place(x=50, y=140, width=1800, height=800)

        # Create a scrollable canvas
        self.canvas = tk.Canvas(self.book_list_frame, bg='white', highlightthickness=0)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

        treeview_style = ttk.Style()
        treeview_style.configure("Custom.Treeview",
                        background='#faedef',
                        foreground='black',
                        rowheight=30,
                        fieldbackground='#faedef')
        treeview_style.map("Custom.Treeview",
                            background=[('selected', 'silver')])
        # Configure the style for the Treeview header.
        style = ttk.Style()
        style.configure("Treeview.Heading", font = ('Paltino Linotype', 16, 'bold italic'), 
                         background='#FFB6C1', foreground='black'
                        )

        # Create the Treeview.
        self.tree = ttk.Treeview(self.canvas, show='headings', selectmode='browse', style='Custom.Treeview')
        self.tree["columns"] = ("BookName", "AuthorName", "DateInserted", "Rating")

        self.tree.heading('BookName', text="Book Title")
        self.tree.heading('AuthorName', text="Author Name")
        self.tree.heading('DateInserted', text="Date Inserted")
        self.tree.heading('Rating', text="Book Rating")
        # Set the anchor option for each column to 'center'.
        self.tree.column('BookName', anchor='center')
        self.tree.column('AuthorName', anchor='center')
        self.tree.column('DateInserted', anchor='center')
        self.tree.column('Rating', anchor='center')

        # Add a vertical scrollbar to the Treeview.
        vsb = ttk.Scrollbar(self.canvas, orient='vertical', command=self.tree.yview)
        self.tree.configure(yscrollcommand=vsb.set)

        # Pack the Treeview and scrollbar.
        self.tree.pack(side='left', fill='both', expand=True)
        vsb.pack(side='right', fill='y')

        # Fetch boks from the database.
        books_data = fetch_books_for_reader(self.ReaderID)
        for i, book_data in enumerate(books_data):
            self.create_book_entry(book_data)

        # Update the scroll region to encompass the Treeview.
        self.tree.bind("<Configure>", lambda e: self.tree.update_idletasks())
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

        # Create "Update Bookshelf" button.
        update_button = ttk.Button(self.bookshelf_window, text="Update Bookshelf",
                                   command=self.update_bookshelf, style='Buttons.TButton')
        update_button.pack(side=tk.BOTTOM, pady=(0, 75), anchor=tk.SE, padx=(0, 50))

    def create_book_entry(self, book_data):
        '''
        Create a single row for a book in the book list.

        Args:
        books_data (dict): Dictionary containing book data to be inserted in a row.
        '''
        self.tree.insert('', 'end', values=(
                                            book_data["BookName"], 
                                            book_data["AuthorName"], 
                                            book_data["DateInserted"], 
                                            book_data["Rating"]
                                            )
                        )
    
    #def create_star_ratings(self, event):
        # Function to create star ratings in the "Rating" column
        # Load star images
     #   self.star_images = [tk.PhotoImage(file=f"./images/star.png") for i in range(5)]
      #  stars = []
       # item = self.tree.selection()
        #if item:
         #   rating = int(self.tree.item(item, "values")[3])
          #  star_image = self.star_images[rating - 1]
           # self.tree.set(item, "Rating", star_image)

    
    
    def perform_search(self):
        '''
        Search Functionality in the Reader's window.
        '''
        # Get the search query from the entry widget
        search_query = self.search_entry.get().strip().lower()

        # Clear the Treeview
        self.tree.delete(*self.tree.get_children())

        # Fetch books from the database based on the search query
        books_data = fetch_books_for_reader(self.ReaderID, search_query)
        
        # Populate the Treeview with the search results
        for i, book_data in enumerate(books_data):
            self.create_book_entry(book_data)

        # Update the scroll region
        self.tree.update_idletasks()
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
    
    def refresh_bookshelf(self):
        '''
        Refresh the bookshelf (Treeview/ books table).
        '''
        # Clear the Treeview
        self.tree.delete(*self.tree.get_children())

        # Fetch books from the database.
        books_data = fetch_books_for_reader(self.ReaderID)

        # Populate the Treeview with book details.
        for i, book_data in enumerate(books_data):
            self.create_book_entry(book_data)

        # Update the scroll region to encompass the Treeview.
        self.tree.update_idletasks()
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))


    def update_bookshelf(self):
        '''
        Structure/Design/Implementation of the "Update bookshelf" button click.
        '''
        # Print for testing
        print("Updating bookshelf...")

        # Open a new window for inserting new books and updating the bookshelf
        update_window = tk.Toplevel(self.bookshelf_window)
        update_window.geometry('900x300')
        update_window.title("Update Bookshelf")

        # Left Frame for inserting new books
        left_frame = tk.Frame(update_window, bg='white')
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        tk.Label(left_frame, text="Insert New Book", font=("Helvetica", 16), bg='white').pack(pady=10)

        tk.Label(left_frame, text="Book Title:", font=("Arial", 12), bg='white').pack(pady=5)
        title_entry = tk.Entry(left_frame, font=("Arial", 12))
        title_entry.pack(pady=5)

        tk.Label(left_frame, text="Author Name:", font=("Arial", 12), bg='white').pack(pady=5)
        author_entry = tk.Entry(left_frame, font=("Arial", 12))
        author_entry.pack(pady=5)

        tk.Label(left_frame, text="Rating (out of 4):", font=("Arial", 12), bg='white').pack(pady=5)
        rating_entry = tk.Entry(left_frame, font=("Arial", 12))
        rating_entry.pack(pady=5)

        def insert_book():
            '''
            Function to insert the new book into the bookshelf.
            '''
            book_title = title_entry.get()
            author_name = author_entry.get()
            rating = rating_entry.get()

            # Validate inputs.
            if not book_title.replace(' ', '').isalpha() or not author_name.replace(' ', '').isalpha():
                messagebox.showerror("Invalid Entry", "Please enter only alphabets for the title and author name.")
                return

            try:
                rating = int(rating)
                if not (0 <= rating <= 4):
                    raise ValueError()
            except ValueError:
                messagebox.showerror("Invalid Entry", "Please enter a valid rating between 0 and 4.")
                return
            
           
            # Insert book into the ReaderBookshelf database.
            if (insert_book_for_reader(self.ReaderID, book_title, author_name, rating)):
                messagebox.showinfo("Success", "Your book has been inserted!")
                update_window.destroy()
                self.refresh_bookshelf()
            else:
                return

        tk.Button(left_frame, text="Add Book", command=insert_book,
                  bg='#de984e', fg='white', font=("Helvetica", 12)).pack(pady=10)

        # Right Frame for updating bookshelf
        right_frame = tk.Frame(update_window, bg='white')
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        tk.Label(right_frame, text="Update Book Rating", font=("Helvetica", 16), bg='white').pack(pady=10)

        tk.Label(right_frame, text="Book Title:", font=("Arial", 12), bg='white').pack(pady=5)
        update_title_entry = tk.Entry(right_frame, font=("Arial", 12))
        update_title_entry.pack(pady=5)

        tk.Label(right_frame, text="Author Name:", font=("Arial", 12), bg='white').pack(pady=5)
        update_author_entry = tk.Entry(right_frame, font=("Arial", 12))
        update_author_entry.pack(pady=5)

        tk.Label(right_frame, text="New Rating (out of 4):", font=("Arial", 12), bg='white').pack(pady=5)
        new_rating_entry = tk.Entry(right_frame, font=("Arial", 12))
        new_rating_entry.pack(pady=5)

        def update_rating():
            '''
            Function to update the bookshelf with the new rating.
            '''
            book_title = update_title_entry.get()
            author_name = update_author_entry.get()
            new_rating = new_rating_entry.get()

            # Validate inputs
            if not book_title.replace(' ', '').isalpha() or not author_name.replace(' ', '').isalpha():
                messagebox.showerror("Invalid Entry", "Please enter only alphabets for the title and author name.")
                return

            try:
                new_rating = int(new_rating)
                if not (0 <= new_rating <= 4):
                    raise ValueError()
            except ValueError:
                messagebox.showerror("Invalid Entry", "Please enter a valid rating between 0 and 4.")
                return
            

            if (update_book_rating_for_reader(self.ReaderID, book_title, author_name, new_rating)):
                messagebox.showinfo("Success", "Your book has been updated!")
                update_window.destroy()
                self.refresh_bookshelf()
            else:
                messagebox.showerror("Invalid Book", "The book you have entered is not in your Bookshelf.")
                return

        tk.Button(right_frame, text="Update Bookshelf", command=update_rating,
                  bg='#de984e', fg='white', font=("Helvetica", 12)).pack(pady=10)
        
        # Bottom Frame for deleting books
        delete_frame = tk.Frame(update_window, bg='white')
        delete_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        tk.Label(delete_frame, text="Delete Book", font=("Helvetica", 16), bg='white').pack(pady=10)

        tk.Label(delete_frame, text="Book Title:", font=("Arial", 12), bg='white').pack(pady=5)
        delete_title_entry = tk.Entry(delete_frame, font=("Arial", 12))
        delete_title_entry.pack(pady=5)

        tk.Label(delete_frame, text="Author Name:", font=("Arial", 12), bg='white').pack(pady=5)
        delete_author_entry = tk.Entry(delete_frame, font=("Arial", 12))
        delete_author_entry.pack(pady=5)

        def delete_book():
            '''
            Function to delete the book from the bookshelf.
            '''
            book_title = delete_title_entry.get()
            author_name = delete_author_entry.get()

            # Validate inputs
            if not book_title.replace(' ', '').isalpha() or not author_name.replace(' ', '').isalpha():
                messagebox.showerror("Invalid Entry", "Please enter only alphabets for the title and author name.")
                return

            if (delete_book_from_reader_bookshelf(self.ReaderID, book_title, author_name)):
                messagebox.showinfo("Success", "Your book has been deleted!")
                update_window.destroy()
                self.refresh_bookshelf()
            else:
                messagebox.showerror("Invalid Book", "The book you have entered is not in your Bookshelf.")
                return

        tk.Button(delete_frame, text="Delete Book", command=delete_book,
                bg='#de984e', fg='white', font=("Helvetica", 12)).pack(pady=10)