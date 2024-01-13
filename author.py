'''
Defines Structure of Author part of the app.

AuthorAuth (class): Structure/design of the author Login Window.
AuthorInfoDisplay (class): Structure/Design of the Author's Information Display
''' 
from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from PIL import Image, ImageTk, ImageFilter 

from page_setup import initial_page_setup
from database import *


class AuthorAuth:
    def __init__(self, parent):
        '''
        Creates an instance of the AuthorAuth class for the Login Page.
        '''
        self.parent = parent
        self.create_login_window()

    def create_login_window(self):
        '''
        Defines structure/design of the Login Page.
        '''
        self.login_window = initial_page_setup(self, self.parent, "Author", "Author Login")

        # Main frame
        self.bg_frame = Frame(self.login_window, bg='white', width=1166, height=718)
        self.bg_frame.pack(fill='both', expand='yes')

        # Login frame.
        self.login_frame = Frame(self.bg_frame, bg='white', width=950, height=700)
        self.login_frame.place(x=450, y=100)

        # Slogan in Login frame.
        self.slogan = "\"Writing from the heart\""
        self.heading = Label(self.login_frame, text=self.slogan, 
                             font=('Palatino Linotype', 20, "italic bold"),
                             bg="white", fg='#de984e', bd=5, relief=FLAT)
        self.heading.place(x=35, y=20, width=400, height=30)

        # Side image in Login frame.
        self.side_image = Image.open('./images/AuthorLogin/side_image1.png')
        photo = ImageTk.PhotoImage(self.side_image)
        self.side_image_label = Label(self.login_frame, image=photo, bg='white')
        self.side_image_label.image = photo
        self.side_image_label.place(x=5, y=100)

        # Sign In icon.
        self.sign_in_image = Image.open('./images/AuthorLogin/sign_in.png')
        photo = ImageTk.PhotoImage(self.sign_in_image)
        self.sign_in_image_label = Label(self.login_frame, image=photo, bg='white')
        self.sign_in_image_label.image = photo
        self.sign_in_image_label.place(x=650, y=135)

        # Sign In label.
        self.sign_in_label = Label(self.login_frame, text="Sign In", bg="white", fg="#696868",
                                    font=("yu gothic ui", 14, "bold"))
        self.sign_in_label.place(x=650, y=207)

        # Add widgets for author login.
        # Username
        #Label
        self.username_label = Label(self.login_frame, text="Username", bg='white', fg="#ccbfb1",
                                   font=("yu gothic ui", 13, "bold"))
        self.username_label.place(x=550, y=300)
        # Entry
        self.username_entry = Entry(self.login_frame,  highlightthickness=0, relief=FLAT, bg="white", fg="#696868",
                                    font=("yu gothic ui ", 12, "bold"), insertbackground = '#6b6a69')
        self.username_entry.place(x=580, y=335, width=270, height=30)
        # Line
        self.username_line = Canvas(self.login_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.username_line.place(x=550, y=361)
        # Icon
        self.username_icon = Image.open('./images/AuthorLogin/username_icon.png')
        photo = ImageTk.PhotoImage(self.username_icon)
        self.username_icon_label = Label(self.login_frame, image=photo, bg='white')
        self.username_icon_label.image = photo
        self.username_icon_label.place(x=550, y=335)

        # Password
        # Label
        self.password_label = Label(self.login_frame, text="Password", bg="white", fg="#ccbfb1",
                                    font=("yu gothic ui", 13, "bold"))
        self.password_label.place(x=550, y=380)
        # Entry
        self.password_entry = Entry(self.login_frame, highlightthickness=0, relief=FLAT, bg="white", fg='#696868',
                                    font=("yu gothic ui", 12, "bold"), show="*", insertbackground = '#6b6a69')
        self.password_entry.place(x=580, y=416, width=244, height=30)
        # Line
        self.password_line = Canvas(self.login_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.password_line.place(x=550, y=442)
        # Icon
        self.password_icon = Image.open('./images/AuthorLogin/password_icon.png')
        photo = ImageTk.PhotoImage(self.password_icon)
        self.password_icon_label = Label(self.login_frame, image=photo, bg='#040405')
        self.password_icon_label.image = photo
        self.password_icon_label.place(x=550, y=417)
        # Show/Hide Password
        self.show_image = ImageTk.PhotoImage(file='./images/AuthorLogin/pswd_hide.png')
        self.hide_image = ImageTk.PhotoImage(file='./images/AuthorLogin/pswd_show.png')
        self.show_button = Button(self.login_frame, image=self.show_image, command=self.show, relief=FLAT,
                                  activebackground='#f7ebed'
                                  , borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=860, y=420)

        # AuthorLogin Button
        self.login_button = Image.open('./images/AuthorLogin/login_button.png')
        photo = ImageTk.PhotoImage(self.login_button)
        self.login_button_label = Label(self.login_frame, image=photo, bg='white', cursor='hand2')
        self.login_button_label.image = photo
        self.login_button_label.place(x=550, y=480)
        self.login_button_label.bind("<Button-1>", self.author_login_action)

        self.forgot_button = Button(self.login_frame, text="Forgot Password ?",
                                    font=("yu gothic ui", 9, "italic underline"), fg="#ccbfb1", relief=FLAT,
                                    borderwidth=0, activebackground="#f7ebed", background="white", cursor="hand2",
                                    activeforeground="#ccbfb1", command=self.show_forgot_password_window)
        self.forgot_button.place(x=550, y=580)

                                            # Bind an event to enable/disable the login button based on the entry content
                                            #self.username_entry.bind("<KeyRelease>", self.toggle_login_button_state)
                                            #self.toggle_login_button_state(None)
        #Login frame Hover events.
        self.login_frame.bind("<Enter>", self.on_enter)
        self.login_frame.bind("<Leave>", self.on_leave)


    def on_enter(self, event):
        '''
        Changes the background color of a frame to pink when the cursor is over it.
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
        Changes the background color of a frame to white when the cursor is not on it.
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
                                  , borderwidth=0, background="white", cursor="hand2")
        self.hide_button.place(x=860, y=420)
        self.password_entry.config(show='')

    def hide(self):
        '''
        Configure the hide password feature for the password entry.
        '''
        self.show_button = Button(self.login_frame, image=self.show_image, command=self.show, relief=FLAT,
                                  activebackground='#f7ebed'
                                  , borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=860, y=420)
        self.password_entry.config(show='*')

    #def toggle_login_button_state(self, event):
     #   '''
      #  Enables the login button only if a username is entered.
       # '''
       # username = self.username_entry.get()
        #password = self.password_entry.get()
        #if username and password:
        #    self.login_button_label["state"] = tk.NORMAL
        #else:
         #   self.login_button_label["state"] = tk.DISABLED

    def author_login_action(self, event):
        '''
        Perform necessary action after logging in.
        (1) Destroy the login window.
        (2) Validate user.
        (3) Create the AuthorInfo Display window.
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
        AuthorID = validate_author(username, password)
        if not AuthorID:
            messagebox.showerror("Invalid Login Details", "User does not exist")
            return 

        # Close the login window after successful login
        self.login_window.destroy()
        print('Login successful')
        author_dashboard = AuthorDashboard(self.parent, AuthorID)

    def show_forgot_password_window(self, event):
        # Implement functionality to show the forgot password window
        print("Forgot Password clicked")


class AuthorDashboard:
    '''Display info about the Author.'''
    def __init__(self, parent, AuthorID):
        '''
        Create an instance of the AuthorInformation Display window.
        (Displays all the information about the author and the books written by him/her).

        Args:
        parent (Tk): The window from which the button ws clicked i.e the login window.
        AuthorID (int): The ID of the Reader whose bookshelf is to be displayed.
        '''
        self.parent = parent
        self.AuthorID = AuthorID
        self.create_author_window()

    def create_author_window(self):
        ''''
        Create a new window to display the list of books.
        '''
        self.dashboard_window = initial_page_setup (
                                                    self, 
                                                    self.parent, 
                                                    "AuthorDashboard", 
                                                    "Author Dashboard"
                                                )
        # Create a frame for the info area
        info_frame = Frame(self.dashboard_window, bg='white', highlightthickness=0)
        info_frame.place(x=50, y=40, width=400, height=100)

        # Add profile picture (replace 'path_to_profile_pic' with the actual path)
        profile_pic_path = './images/AuthorLogin/profile_pic.png'
        profile_pic = PhotoImage(file=profile_pic_path)
        profile_label = Label(info_frame, image=profile_pic, bg='white')
        profile_label.image = profile_pic
        profile_label.pack(side=tk.LEFT, padx=0)

        # Add username and bio
        username = get_username(self.AuthorID, "Author")
        username_label = Label(info_frame, text="{}'s Dashboard".format(username), font=('Palatino Linotype', 12, 'bold'), bg='white')
        username_label.pack(side=tk.LEFT, padx=10)
        

        # Create a frame for the search bar
        search_frame = Frame(self.dashboard_window, bg='white', highlightthickness=0)
        search_frame.place(x=670, y=50, width=700, height=50)

        # Create a search entry widget
        self.search_entry = Entry(search_frame, font=('yu gothic ui', 15), width=30)
        self.search_entry.pack(side=tk.LEFT, padx=10)

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
                background=[('active', '#de984e')],
                foreground=[('active', 'white')])

        search_button = ttk.Button(search_frame, text="Search", command=self.perform_search, style='Buttons.TButton')
        search_button.pack(side=tk.LEFT, padx=10)

         # Create a frame to hold the book list
        self.book_list_frame = Frame(self.dashboard_window, bg='white', highlightthickness=1)
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
        self.tree["columns"] = ("BookName", "NumberOfReaders", "AverageRating")

        self.tree.heading('BookName', text="Book Title")
        self.tree.heading('NumberOfReaders', text="Number of Readers")
        self.tree.heading('AverageRating', text="Average Book Rating")
        # Set the anchor option for each column to 'center'.
        self.tree.column('BookName', anchor='center')
        self.tree.column('NumberOfReaders', anchor='center')
        self.tree.column('AverageRating', anchor='center')

        # Add a vertical scrollbar to the Treeview.
        vsb = ttk.Scrollbar(self.canvas, orient='vertical', command=self.tree.yview)
        self.tree.configure(yscrollcommand=vsb.set)

        # Pack the Treeview and scrollbar.
        self.tree.pack(side='left', fill='both', expand=True)
        vsb.pack(side='right', fill='y')

        # Fetch boks from the database.
        books_data = fetch_books_for_author(self.AuthorID)
        for i, book_data in enumerate(books_data):
            self.create_book_entry(book_data)
        
        # Update the scroll region to encompass the Treeview.
        self.tree.bind("<Configure>", lambda e: self.tree.update_idletasks())
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))


    def create_book_entry(self, book_data):
        '''
        Create a single row for a book in the book list.

        Args:
        books_data (dict): Dictionary containing book data to be inserted in a row.
        '''
        self.tree.insert('', 'end', values=(
                                            book_data["BookName"], 
                                            book_data["NumberOfReaders"], 
                                            book_data["AverageRating"]
                                            )
                        )

    def perform_search(self):
        '''
        Search Functionality in the Author's window.
        '''
        # Get the search query from the entry widget
        search_query = self.search_entry.get().strip().lower()

        # Clear the Treeview
        self.tree.delete(*self.tree.get_children())

        # Fetch books from the database based on the search query
        books_data = fetch_books_for_author(self.AuthorID, search_query)
        
        # Populate the Treeview with the search results
        for i, book_data in enumerate(books_data):
            self.create_book_entry(book_data)

        # Update the scroll region
        self.tree.update_idletasks()
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

