'''
Structure/Design/Funtionality of the Sign Up window.
'''
from tkinter import *
from tkinter import ttk, messagebox, simpledialog
from PIL import Image, ImageTk, ImageFilter  # pip install pillow

from page_setup import *
from database import insert_reader_in_database, insert_author_in_database

# Buttons Style Configurations.
style = ttk.Style()
style.configure('Buttons.TButton',
                font=('Palatino Linotype', 13, 'bold'),
                background='#FFB6C1',
                foreground='black',
                borderwidth=0,
                relief='flat',
                padding=(5, 5))

class SignUp:
    '''Contains structure, design of the SignUp page.'''
    def __init__(self, parent):
        '''
        Creates an instance of the SignUp Page.

        Args:
        parent (class): The class instance from which the SignUp button was clicked.
        '''
        self.parent = parent
        # Ask the user to sign up as a reader or author
        self.show_user_options()       

    def show_user_options(self):
        '''
        Ask the user to specify signup option (Reader or Author).
        '''
        # Ask the user to sign up as a reader or author.
        self.popup = tk.Toplevel(self.parent)
        self.popup.geometry('290x150')
        self.popup.title("Who are you?")
        self.popup.configure(bg='white')
        # Calculate x and y coordinates for center placement of window.
        screen_width = self.parent.winfo_screenwidth()
        screen_height = self.parent.winfo_screenheight()
        x_coordinate = int((screen_width - self.popup.winfo_reqwidth()) / 2)
        y_coordinate = int((screen_height - self.popup.winfo_reqheight()) / 2)
        # Set the geometry of the window.
        self.popup.geometry("+{}+{}".format(x_coordinate, y_coordinate))

        label = Label(self.popup, text="Who are you?", 
                      font=('Palatino Linotype', 14, 'bold'), bg='white')
        label.pack(pady=10)
        # Create buttons for Reader and Author options.
        reader_button = ttk.Button(self.popup, text="Reader",
                                   command=lambda: self.open_signup_window("Reader"), 
                                   style='Buttons.TButton'
                                  )
        reader_button.pack(side=tk.LEFT, padx=13, pady=10)       
        author_button = ttk.Button(self.popup, text="Author", 
                                   command=lambda: self.open_signup_window("Author"), 
                                   style='Buttons.TButton'
                                  )
        author_button.pack(side=tk.RIGHT, padx=13, pady=10)

    def open_signup_window(self, user_type):
        '''
        Open the corresponding sign-up window.
        (Depending on the user's choice).

        Args:
        user_type (str): The user's choice (Author/Reader).
        '''
        self.user_type = user_type
        self.popup.destroy()
        
        if user_type == "Reader":
            # Print for testing
            print("Open Reader Sign-Up Window")
            self.create_signup_window()

        elif user_type == "Author":
            # Print for testing
            print("Open Author Sign-Up Window")
            self.create_signup_window()
    
    def create_signup_window(self):
        '''
        Design/Functionality/Structure of the actual signup page.
        '''
        self.signup_window = initial_page_setup (self, self.parent, "SignUp", "Sign Up")
        
        # Main frame.
        self.bg_frame = Frame(self.signup_window, bg='white', width=1166, height=718)
        self.bg_frame.pack(fill='both', expand='yes')
        
        # Signup frame.
        self.signup_frame = Frame(self.bg_frame, bg='white', width=1000, height=700)
        self.signup_frame.place(x=450, y=100)

        # Slogan in Login frame.
        self.slogan = "Let's Get Started!"
        self.heading = Label(self.signup_frame, text=self.slogan, 
                             font=('Palatino Linotype', 20, 'italic bold'),
                             bg='white', fg='#de984e', bd=5, relief=FLAT)
        self.heading.place(x=35, y=20, width=400, height=30)

        # Sign In icon.
        self.signup_image = Image.open('./images/SignUp/signup_icon.png')
        photo = ImageTk.PhotoImage(self.signup_image)
        self.signup_image_label = Label(self.signup_frame, image=photo, bg='white')
        self.signup_image_label.image = photo
        self.signup_image_label.place(x=450, y=90)
        
        # Widgets for Reader sign up.
        # Labels
        # First Name.
        self.firstname_label = Label(self.signup_frame, text="First Name *",
                                     font=('yu gothic ui', 13, 'bold'),
                                     bg='white', fg='#ccbfb1')
        self.firstname_label.place(x=40, y=255)
        # Last Name
        self.lastname_label = Label(self.signup_frame, text="Last Name *",
                                     font=('yu gothic ui', 13, 'bold'),
                                     bg='white', fg='#ccbfb1')
        self.lastname_label.place(x=555, y=255)
        # Password
        self.password_label = Label(self.signup_frame, text="Password *",
                                     font=('yu gothic ui', 13, 'bold'),
                                     bg='white', fg='#ccbfb1')
        self.password_label.place(x=40, y=335)
        # Reenter Password
        self.reenter_password_label = Label(self.signup_frame, text="Re-Password",
                                     font=('yu gothic ui', 13, 'bold'),
                                     bg='white', fg='#ccbfb1')
        self.reenter_password_label.place(x=555, y=335)
        # Email
        self.email_label = Label(self.signup_frame, text="Email *",
                                     font=('yu gothic ui', 13, 'bold'),
                                     bg='white', fg='#ccbfb1')
        self.email_label.place(x=40, y=415)
        # Bio
        self.bio_label = Label(self.signup_frame, text="Bio (0-70)",
                                     font=('yu gothic ui', 13, 'bold'),
                                     bg='white', fg='#ccbfb1')
        self.bio_label.place(x=555, y=415)
        # Username
        self.username_label = Label(self.signup_frame, text="Username *",
                                     font=('yu gothic ui', 13, 'bold'),
                                     bg='white', fg='#ccbfb1')
        self.username_label.place(x=40, y=495)
        # Entry
        # First Name.
        self.firstname_entry = Entry(self.signup_frame, highlightthickness=0,
                                    font=('yu gothic ui', 12, 'bold'), 
                                    insertbackground = '#6b6a69', relief=FLAT, 
                                    bg='white', fg='#696868')
        self.firstname_entry.place(x=170, y=255, width=270, height=30)
        # Last Name.
        self.lastname_entry = Entry(self.signup_frame, highlightthickness=0,
                                    font=('yu gothic ui', 12, 'bold'), 
                                    insertbackground = '#6b6a69', relief=FLAT, 
                                    bg='white', fg='#696868')
        self.lastname_entry.place(x=685, y=255, width=270, height=30)
        # Password.
        self.password_entry = Entry(self.signup_frame, highlightthickness=0,
                                    font=('yu gothic ui', 12, 'bold'),
                                    show="*", insertbackground = '#6b6a69',
                                    relief=FLAT, bg='white', fg='#696868',)
        self.password_entry.place(x=170, y=335, width=270, height=30)
        # Show/Hide Password
        self.show_image = ImageTk.PhotoImage(file='./images/ReaderLogin/pswd_hide.png')
        self.hide_image = ImageTk.PhotoImage(file='./images/ReaderLogin/pswd_show.png')
        self.show_button = Button(self.signup_frame, image=self.show_image, command=self.show, 
                                  relief=FLAT, activebackground='#f7ebed' ,borderwidth=0, 
                                  background='white', cursor='hand2')
        self.show_button.place(x=950, y=335)
        # Reenter Password
        self.reenter_password_entry = Entry(self.signup_frame, highlightthickness=0,
                                    font=('yu gothic ui', 12, 'bold'),
                                    show="*", insertbackground = '#6b6a69',
                                    relief=FLAT, bg='white', fg='#696868',)
        self.reenter_password_entry.place(x=685, y=335, width=270, height=30)
        # Email
        self.email_entry = Entry(self.signup_frame, highlightthickness=0,
                                    font=('yu gothic ui', 12, 'bold'), 
                                    insertbackground = '#6b6a69', relief=FLAT, 
                                    bg='white', fg='#696868')
        self.email_entry.place(x=170, y=415, width=270, height=30)
        # Multi line Bio
        self.bio_entry = Text(self.signup_frame, wrap="word", font=('yu gothic ui', 12, 'bold'), 
                              insertbackground='#6b6a69', relief=FLAT, bg='white', fg='#696868')
        self.bio_entry.place(x=685, y=415, width=270, height=80) 
        # Username
        self.username_entry = Entry(self.signup_frame, highlightthickness=0,
                                    font=('yu gothic ui', 12, 'bold'), 
                                    insertbackground = '#6b6a69', relief=FLAT, 
                                    bg='white', fg='#696868')
        self.username_entry.place(x=170, y=495, width=270, height=30)
        # Line
        # First Name.
        self.firstname_line = Canvas(self.signup_frame, width=270, height=2.0,
                                    bg='#bdb9b1', highlightthickness=0)
        self.firstname_line.place(x=170, y=281)
        # Last Name
        self.lastname_line = Canvas(self.signup_frame, width=270, height=2.0,
                                    bg='#bdb9b1', highlightthickness=0)
        self.lastname_line.place(x=685, y=281)
        # Password
        self.password_line = Canvas(self.signup_frame, width=270, height=2.0,
                                    bg='#bdb9b1', highlightthickness=0)
        self.password_line.place(x=170, y=361)
        # Reenter Password.
        self.reenter_password_line = Canvas(self.signup_frame, width=270, height=2.0,
                                    bg='#bdb9b1', highlightthickness=0)
        self.reenter_password_line.place(x=685, y=361)
        # Email
        self.email_line = Canvas(self.signup_frame, width=270, height=2.0,
                                    bg='#bdb9b1', highlightthickness=0)
        self.email_line.place(x=170, y=441)  
        # Username
        self.username_line = Canvas(self.signup_frame, width=270, height=2.0,
                                    bg='#bdb9b1', highlightthickness=0)
        self.username_line.place(x=170, y=521)    

        # Reader Signup Button.
        self.signup_button = Image.open('./images/SignUp/signup_button.png')
        photo = ImageTk.PhotoImage(self.signup_button)
        self.signup_button_label = Label(self.signup_frame, image=photo, bg='white', cursor='hand2')
        self.signup_button_label.image = photo
        self.signup_button_label.place(x=330, y=585)
        self.signup_button_label.bind("<Button-1>", self.validate_signup)  

        # Signup frame Hover events.
        self.signup_frame.bind("<Enter>", self.on_enter)
        self.signup_frame.bind("<Leave>", self.on_leave)


    def validate_signup(self, event):
        '''
        Validate SignUp enteries and insert new user into the database.

        Args:
            event (): The event that activates the function (Clicking the signup button).
        '''
        # Validate First Name and Last Name.
        first_name = self.firstname_entry.get()
        last_name = self.lastname_entry.get()
        if not first_name.isalpha() or not last_name.isalpha():
            messagebox.showerror("Error", "First Name and Last Name should contain only alphabets.")
            return

        # Validate Password.
        password = self.password_entry.get()
        reenter_password = self.reenter_password_entry.get()
        if len(password) < 8:
            messagebox.showerror("Error", "Password must be at least 8 characters long.")
            return
        if password != reenter_password:
            messagebox.showerror("Error", "Passwords do not match.")
            return

        # Validate Email
        email = self.email_entry.get()
        if "@" not in email:
            messagebox.showerror("Error", "Invalid email address.")
            return
        
        # Validate Username
        username = self.username_entry.get()
        if ' ' in username:
            messagebox.showerror("Error", "Username should not contain spaces.")
            return
        
        # Validate Bio
        bio = self.bio_entry.get("1.0", END).strip() 
        if len(bio) > 70:
            messagebox.showerror("Error", "Bio cannot be more than 70 characters.")
            return

        if self.user_type == "Reader":
            # Insert new reader in the database
            ReaderID = insert_reader_in_database(username, first_name, last_name, password, email, bio)
            if not ReaderID:
                messagebox.showerror("Invalid Username", "Username already exists. Choose a different username.")
            elif ReaderID > 0:
                messagebox.showinfo("Success", "Signup successful! Welcome {}".format(first_name))
                self.signup_window.destroy()
                from reader import ReaderBookshelf
                reader_bookshelf = ReaderBookshelf(self.parent, ReaderID)
        else:
            AuthorID = insert_author_in_database(username, first_name, last_name, password, email, bio)
            if not AuthorID:
                messagebox.showerror("Invalid Username", "Username already exists. Choose a different username.")
            elif AuthorID > 0:
                messagebox.showinfo("Success", "Signup successful! Welcome {}".format(first_name))
                self.signup_window.destroy()
                #from author import authorInfo
                #reader_bookshelf = authorInfo(self.parent, ReaderID)

    def on_enter(self, event):
        '''
        Changes the background color of a frame/label/button to pink when the cursor is over it (Hover feature).
        '''
        self.signup_frame.configure(bg='#f7ebed')
        self.heading.configure(bg='#f7ebed')
        #self.side_image_label.configure(bg='#f7ebed')

        self.signup_image_label.configure(bg='#f7ebed')
        #self.signup_label.configure(bg='#f7ebed')

        self.firstname_label.configure(bg='#f7ebed')
        self.firstname_entry.configure(bg='#f7ebed')
        self.lastname_label.configure(bg='#f7ebed')
        self.lastname_entry.configure(bg='#f7ebed')
        #self.firstname_icon_label.configure(bg='#f7ebed')

        self.password_label.configure(bg='#f7ebed')
        self.password_entry.configure(bg='#f7ebed')
        self.reenter_password_label.configure(bg='#f7ebed')
        self.reenter_password_entry.configure(bg='#f7ebed')
        #self.password_icon_label.configure(bg='#f7ebed')
        self.show_button.configure(bg='#f7ebed')
                #self.hide_button.configure(bg='#f7ebed')
        self.email_label.configure(bg='#f7ebed')
        self.email_entry.configure(bg='#f7ebed')
        self.bio_label.configure(bg='#f7ebed')
        self.username_label.configure(bg='#f7ebed')
        self.username_entry.configure(bg='#f7ebed')

        #self.password_icon_label.configure(bg='#f7ebed')


        self.signup_button_label.configure(bg='#f7ebed')

        #self.forgot_button.configure(bg='#f7ebed')

        

    def on_leave(self, event):
        '''
        Changes the background color of a frame/label/button to white when the cursor is not on it (Hover feature).
        '''
        self.signup_frame.configure(bg='white')
        self.heading.configure(bg='white')
        #self.side_image_label.configure(bg='white')

        self.signup_image_label.configure(bg='white')
        #self.signup_label.configure(bg='white')

        self.firstname_label.configure(bg='white')
        self.firstname_entry.configure(bg='white')
        self.lastname_label.configure(bg='white')
        self.lastname_entry.configure(bg='white')
        #self.firstname_icon_label.configure(bg='white')

        self.password_label.configure(bg='white')
        self.password_entry.configure(bg='white')
        self.reenter_password_label.configure(bg='white')
        self.reenter_password_entry.configure(bg='white')
        #self.password_icon_label.configure(bg='white')
        self.show_button.configure(bg='white')
                #self.hide_button.configure(bg='white')

        self.email_label.configure(bg='white')
        self.email_entry.configure(bg='white')
        self.bio_label.configure(bg='white')
        self.username_label.configure(bg='white')
        self.username_entry.configure(bg='white')

        self.signup_button_label.configure(bg='white')

        #self.forgot_button.configure(bg='white')

    def show(self):
        '''
        Configure the show password feature for the password entry.
        '''
        self.hide_button = Button(self.signup_frame, image=self.hide_image, command=self.hide, relief=FLAT,
                                  activebackground='#f7ebed'
                                  , borderwidth=0, background='white', cursor='hand2')
        self.hide_button.place(x=950, y=335)
        self.password_entry.config(show='')
        self.reenter_password_entry.config(show='')

    def hide(self):
        '''
        Configure the hide password feature for the password entry.
        '''
        self.show_button = Button(self.signup_frame, image=self.show_image, command=self.show, relief=FLAT,
                                  activebackground='#f7ebed'
                                  , borderwidth=0, background='white', cursor='hand2')
        self.show_button.place(x=950, y=335)
        self.password_entry.config(show='*')
        self.reenter_password_entry.config(show='*')