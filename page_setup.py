'''
Methods that structure/design common parts of different windows like the nav bar.
''' 
import tkinter as tk
from tkinter import ttk, Frame
from PIL import Image, ImageTk, ImageFilter 

def initial_page_setup(self, parent, window_name, window_title):
        '''
        Common set up designs for windows.
        
        Args:
        self (class): The class in which the window's structure is defined.
        parent (class): Parent of the self class.
        window_name (str): The name of the window.
        window_title (str): The title to be placed at the to of the window.
        '''
        window = tk.Toplevel(self.parent)
        window.geometry('1910x1080')
        window.resizable(0, 0)
        window.state('normal')
        window.title(window_title)
        window.configure(bg = 'white', highlightthickness=4, highlightbackground='#FFB6C1', highlightcolor='#FFB6C1')
        
        # Create Navigation bar.
        create_navigation_bar(window, window_name)
        return window

        

def create_navigation_bar(root, window_name=""):
        '''
        Structure, Design of the nav bar of specified window.
        
        Args:
        root (any): The window whose nav bar is to be designed.
        '''
        # Configure Button Style.
        style = ttk.Style()
        style.configure('Nav.TButton',
                        font=('Palatino Linotype', 14, 'bold'),
                        background='white',
                        foreground='black',  # Text color
                        borderwidth=0,
                        relief='flat',
                        padding=(10, 10))

        # Hover configuration.
        style.map('Nav.TButton',
                  background=[('active', '#FFB6C1')],  # Faint pink color on hover.
                  foreground=[('active', 'black')])

        # Create a frame for the navigation bar.
        nav_frame = Frame(root, bg='white')
        nav_frame.pack(side=tk.TOP, fill=tk.X)

        # Add the title/logo of your library management system
        logo_path = "./images/logo.png"
        logo_image = Image.open(logo_path)
        logo_image = logo_image.resize((70, 40), Image.LANCZOS)
        logo_photo = ImageTk.PhotoImage(logo_image)

        logo_label = tk.Label(nav_frame, image=logo_photo, bg='white')
        logo_label.image = logo_photo
        logo_label.pack(side=tk.LEFT, padx=(10, 20))

        # Add navigation buttons to the right of the screen.
        if window_name == "ReaderBookshelf" or window_name == "AuthorDashboard":
            reader_btn = ttk.Button(nav_frame, text="Logout", style="Nav.TButton", command=root.destroy)
            reader_btn.pack(side=tk.RIGHT, padx=(20, 10))
            
        if window_name != "SignUp" and window_name != "ReaderBookshelf" and window_name != "AuthorDashboard":
            home_btn = ttk.Button(nav_frame, text="Sign Up", style="Nav.TButton", command=lambda: show_signup_window(root, window_name))
            home_btn.pack(side=tk.RIGHT, padx=(20, 10))

        if window_name != "Reader" and window_name != "SignUp" and window_name != "ReaderBookshelf":
            author_btn = ttk.Button(nav_frame, text="Author", style="Nav.TButton", command=lambda: show_author_login(root, window_name))
            author_btn.pack(side=tk.RIGHT, padx=(20, 10))

        if window_name != "Author" and window_name != "SignUp" and window_name != "AuthorDashboard":
            reader_btn = ttk.Button(nav_frame, text="Reader", style="Nav.TButton", command=lambda: show_reader_login(root, window_name))
            reader_btn.pack(side=tk.RIGHT, padx=(20, 10))

        home_btn = ttk.Button(nav_frame, text="Home", style="Nav.TButton", command=lambda: show_home(root, window_name))
        home_btn.pack(side=tk.RIGHT, padx=(20, 10))

# Define the methods for each button action.
def show_signup_window(root, window_name):
    '''
    Functionality of the "Sign up" button.
    
    Args:
    root (Tk): An instance of a tkinter window.
    window_name (str): The name of the window in which the "Sign up" button is clicked.
    '''
    if window_name == "SignUp":
        return
    from signup import SignUp
    sign_up = SignUp(root)

def show_author_login(root, window_name):
    '''
    Functionality of the "Author" button.
    Goes to Author's login Page.

    Args:
    root (Tk): An instance of a tkinter window.
    window_name (str): The neame of the window the button was clicked in.
    '''
    if window_name == "Author": # Do nothing if the button is clicked in the login window.
        return
    from author import AuthorAuth
    author_auth = AuthorAuth(root)

def show_reader_login(root, window_name):
    '''
    Functionality of the "Reader" button.
    Goes to Reader's login Page.

    Args:
    root (Tk): An instance of a tkinter window.
    window_name (str): The neame of the window the button was clicked in.
    '''
    if window_name == "Reader": # Do nothing if the button is clicked in the login window.
        return
    from reader import ReaderAuth
    reader_auth = ReaderAuth(root)

def show_home(root, window_name):
    '''
    Functionality of the "Home" button.
    Displays the home window.

    Args:
    root (Tk): An instance of a tkinter window.
    window_name (str): The neame of the window the button was clicked in.
    '''
    if window_name == "LandingPage": # Do nothing if the button is clicked in the home window.
        return
    root.destroy()