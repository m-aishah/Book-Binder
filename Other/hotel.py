'''Defines the Hotel Management System interface.'''
from tkinter import *
from PIL import Image, ImageTk  # pip install pillow


class LibraryManagementSystem:
    '''Defines the interface for the Hotel Management System GUI.'''

    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.configure(bg='white')
        
        # Get screen width and height
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Load and resize the image
        img_path = r"/mnt/c/Documents and Settings/WINDOWS11/Desktop/HotelManagaementSystem/images/library_background2.jpg"
        img = Image.open(img_path)
        img = img.resize((screen_width, screen_height), Image.LANCZOS)  # Resize the image to fit the screen
        self.photoimg = ImageTk.PhotoImage(img)

        # Create a label with the background image
        lblimg = Label(self.root, image=self.photoimg, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=0, relwidth=1, relheight=1)  # Use relative width and height to cover the entire screen


        # Main Frame
        main_frame = Frame(self.root, bd=4, relief=RIDGE)
        main_frame.place(x = 0, y = 190, width = 1550, height = 620)
        # Menu Button
        lbl_menu = Label(main_frame, text = 'MENU', font = ('Palintino Linotype', 20, 'bold'), bg = 'white', fg = 'teal', bd = 4, relief = RIDGE)
        lbl_menu.place(x = 0, y = 0, width = 230)


if __name__ == "__main__":
    root = Tk()
    obj = LibraryManagementSystem(root)
    root.mainloop()
