'''
The Landing Page of the Library Management System.
'''
from tkinter import *
from PIL import Image, ImageTk, ImageFilter  # pip install pillow

from page_setup import *


class LandingPage:
    '''Contains structure, design of the landing page.'''
    def __init__(self, root):
        '''
        Creates an instance of the Landing Page.

        Args:
        root (Tk): An instance of the Tk() from the tkinter module.
        '''
        self.root = root
        self.root.geometry("1910x1080")
        self.root.title("Book Binder")
        self.root.configure(
                            bg='white', 
                            highlightthickness=4, 
                            highlightbackground='#FFB6C1', 
                            highlightcolor='#FFB6C1'
                        )

        create_navigation_bar(self.root, "LandingPage")
        self.create_book_gallery()

                                        #self.create_scrapbook_area()
                                        # Create reviews section.
                                        # self.create_reviews_section()

    def create_book_gallery(self):
        '''
        Structures the book gallery section of the landing page.
        '''
        # Create a canvas for displaying book images.
        self.canvas = tk.Canvas(self.root, bg='white', height=200, highlightthickness=0)
        self.canvas.pack(side=tk.TOP, pady=10, fill=tk.X)

        # Load book images
        self.book_images = []
        self.show_images()

        # Create another canvas for second row of book images.
        self.canvas = tk.Canvas(self.root, bg='white', height=200, highlightthickness=0)
        self.canvas.pack(side=tk.TOP, pady=10, fill=tk.X)

        # Load book images
        self.book_images = []
        self.show_images(1)

        # Create another canvas for second row of book images.
        self.canvas = tk.Canvas(self.root, bg='white', height=200, highlightthickness=0)
        self.canvas.pack(side=tk.TOP, pady=10, fill=tk.X)

        # Load book images
        self.book_images = []
        self.show_images(2)


    def show_images(self, row=0):
        '''
        Displays a number of images side by side on a row 
        (in already created canvas).

        Also displays 2 buttons on the first row.

        Args:
        row (int): The row number.
        '''
        # Calculate the width and height of the images.
        # Get canvas size (height and width).
        canvas_width = self.canvas.winfo_reqwidth()
        canvas_height = self.canvas.winfo_reqheight()
        # Calculate the number of images to be placed in the row.
        if row < 1:
            num_images = 9
        else:
            num_images = 10
        # Calculate image width and height.
        image_width = canvas_width / num_images + 125
        image_height = canvas_height - 50

        # Introduce a gap and start_offset between the images.
        image_gap = 20 
        start_offset = 40

        self.canvas.image = [] # List of images.
        
        # Display the images.
        for i in range(num_images):
            # Load image dynamically.
            index = len(self.book_images) + 1
            image_path = "./images/Gallery/{}_{}.png".format(row, index)
            try:
                book_image = Image.open(image_path)

                # Resize the image to fit the grid
                resized_image = book_image.resize((int(image_width), int(image_height)), Image.LANCZOS)
                photo = ImageTk.PhotoImage(resized_image)
                x_position =start_offset + i * (image_width + image_gap)
                y_position = (canvas_height - image_height) / 2 
                self.canvas.create_image(x_position, y_position, anchor=tk.NW, image=photo)
                self.canvas.image.append(photo) 
                self.book_images.append(book_image)
            except FileNotFoundError:
                # No more images to load
                break      

        # Configure Button Style.
        style = ttk.Style()
        style.configure('Gal.TButton',
                        font=('Palatino Linotype', 14),
                        background='white',
                        foreground='black',
                        borderwidth=0,
                        relief='flat',
                        padding=(10, 10))

        # Hover configuration.
        style.map('Gal.TButton',
                  background=[('active', '#FFB6C1')],  # Faint pink color on hover.
                  foreground=[('active', 'black')])
        # Only display buttons on the first row.
        if row == 0:
            # Create "All Books!" button.
            collection_button = ttk.Button(self.canvas, text="All Books!", style='Gal.TButton', command=self.show_all_books)
            collection_button.place(relx=0.98, rely=0.3, anchor=tk.E)

            # Create "All Authors!" button.
            authors_button = ttk.Button(self.canvas, text="All Authors!", style='Gal.TButton', command=self.show_all_authors)
            authors_button.place(relx=.98, rely=0.6, anchor=tk.E)   


    def create_reviews_section(self):
        '''
        Structure, design of the reviews section. Still needs some attention!!!
        '''
        # Create a frame for the reviews section
        reviews_frame = ttk.Frame(self.root)  # White background!!!
        reviews_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Add a label for reviews
        reviews_label = ttk.Label(reviews_frame, text="Reviews", font=("Helvetica", 14, "bold"))
        reviews_label.pack(side=tk.TOP, pady=10)

        # Add reviews by authors and readers
        for i in range(3):  # Displaying 3 reviews in 3 rows and 1 column
            reader_name = ttk.Label(reviews_frame, text="Reader Name", font=("Palatino Linotype", 12, "bold"))
            reader_name.pack(side=tk.TOP, pady=5)

            review_text = ttk.Label(reviews_frame, text="Random review text goes here.", font=("Palatino Linotype", 10))
            review_text.pack(side=tk.TOP, pady=5)

    
    def show_all_books(self):
        '''
        Functionality to show all books.
        '''
        pass

    def show_all_authors(self):
        '''
        Functionality to show all authors.
        '''
        pass

if __name__ == "__main__":
    root = Tk()
    app = LandingPage(root)
    root.mainloop()