 def create_book_gallery(self):
        # Create a frame for the book gallery
        book_gallery_frame = tk.Frame(self.root, bg='white')
        book_gallery_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Create a canvas for displaying book images
        self.canvas = tk.Canvas(book_gallery_frame, bg='white', height=300)
        self.canvas.pack(side=tk.TOP, pady=10, fill=tk.X)

        # Load book images
        self.book_images = [Image.open(f"./images/logo{i}.png") for i in range(1, 6)]

        # Display initial slogan
        self.display_slogan()

        # Create a button for navigating to the next set of books
        self.see_books_btn = ttk.Button(book_gallery_frame, text="See Books", style="Nav.TButton", command=self.show_next_books)
        self.see_books_btn.pack(side=tk.RIGHT, padx=(20, 10))

    def display_slogan(self):
        # Display a slogan or any content you want initially
        slogan_label = ttk.Label(self.canvas, text="Welcome to Athena's Library", font=("Palatino Linotype", 16, "bold"), background='white')
        self.canvas.create_window(400, 150, window=slogan_label)

    def show_next_books(self):
        # Display the next set of books
        # Clear previous content
        self.canvas.delete("all")

        # Calculate the width of each image based on the number of images to display
        canvas_width = self.canvas.winfo_reqwidth()
        num_images = 6
        image_width = canvas_width / num_images

        # Load and display the next set of book images
        for i in range(num_images):
            # Adjust the index based on the current set of images
            index = len(self.book_images) - num_images + i
            if index < 0:
                # If all images are displayed, break the loop
                break

            book_image = self.book_images[index]
            photo = ImageTk.PhotoImage(book_image)
            x_position = i * image_width + image_width / 2
            self.canvas.create_image(x_position, 150, anchor=tk.CENTER, image=photo)
            self.canvas.image = photo  # Keep a reference to the image to prevent it from being garbage collected

        if index + 1 == len(self.book_images):
            # Replace "See Books" button with "All Books" and "All Authors" buttons after the last set of images
            self.see_books_btn.destroy()

            all_books_btn = ttk.Button(self.canvas, text="All Books", style="Nav.TButton", command=self.show_all_books)
            all_books_btn.place(relx=0.25, rely=0.9)

            all_authors_btn = ttk.Button(self.canvas, text="All Authors", style="Nav.TButton", command=self.show_all_authors)
            all_authors_btn.place(relx=0.75, rely=0.9)
        else:
            # Continue displaying "See Books" button for the next sets
            self.see_books_btn.place(relx=0.95, rely=0.5, anchor=tk.E)























 # Display initial slogan
        #self.display_slogan()

        # Configure Button Style
        #style = ttk.Style()
        #style.configure('Gal.TButton',
                        #font=('Palatino Linotype', 14),
                        #background='white',
                        #foreground='white',
                        #borderwidth=0,
                        #relief='flat',
                        #padding=(0, 0))

        # Hover configuration
        #style.map('Gal.TButton',
                #background=[('active', 'white')],
                #foreground=[('active', '#FFB6C1')])

        # Create a button for navigating to the next set of books
        #self.see_books_btn = ttk.Button(self.canvas, text=">>", style="Gal.TButton", command=self.show_images)
        #self.see_books_btn.place(relx=0.98, rely=0.5, anchor=tk.E)





        #def display_slogan(self):
        # Display a slogan or any content you want initially
     #   slogan_label = Label(self.canvas, text="Welcome to Athena's Library", font=("Palatino Linotype", 16, "bold"), background='white')
      #  slogan_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)





# Create a frame for the book gallery
        #book_gallery_frame = tk.Frame(self.root, bg='white', height=350)
        #book_gallery_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        


# White background for the main frame
        self.bg_frame = Frame(self.login_window, bg='white', width=1166, height=718)
        self.bg_frame.pack(fill='both', expand='yes')

        # Pink login frame
        self.lgn_frame = Frame(self.bg_frame, bg='#FFC0CB', width=950, height=600)
        self.lgn_frame.place(x=200, y=70)



        # Add widgets for reader login
        username_label = ttk.Label(self.login_frame, text="Username:")
        username_label.grid(row=0, column=0, sticky=tk.W, pady=(0, 5))

        self.username_entry = ttk.Entry(login_frame, width=20)
        self.username_entry.grid(row=0, column=1, pady=(0, 5))

        password_label = ttk.Label(login_frame, text="Password:")
        password_label.grid(row=1, column=0, sticky=tk.W, pady=(0, 5))

        self.password_entry = ttk.Entry(login_frame, show="*")
        self.password_entry.grid(row=1, column=1, pady=(0, 5))

        self.login_button = ttk.Button(login_frame, text="Login", command=self.reader_login_action)
        self.login_button.grid(row=2, column=0, columnspan=2, pady=(10, 0))

        signup_button = ttk.Button(login_frame, text="Sign Up", command=self.show_signup_window)
        signup_button.grid(row=3, column=0, columnspan=2, pady=(10, 0))

        forgot_password_link = ttk.Label(login_frame, text="Forgot Password?", cursor="hand2")
        forgot_password_link.grid(row=4, column=0, columnspan=2, pady=(10, 0))
        forgot_password_link.bind("<Button-1>", self.show_forgot_password_window)

          # Bind an event to enable/disable the login button based on the entry content
        self.username_entry.bind("<KeyRelease>", self.toggle_login_button_state)

        self.toggle_login_button_state(None)




        def create_scrapbook_area(self):
        # Create a canvas for the scrapbook area at the bottom.
        scrapbook_canvas = Canvas(self.root, bg='white', height=400, highlightthickness=0)
        scrapbook_canvas.pack(side=BOTTOM, pady=10, fill=X)

        # Directory containing scrapbook images
        scrapbook_images_dir = "./images/Scrapbook/"
        
        # Get a list of all scrapbook image filenames
        scrapbook_image_files = [f for f in os.listdir(scrapbook_images_dir) if f.startswith("q") and f.endswith(".png")]

        # Display the resized scrapbook images randomly.
        scrapbook_width = self.root.winfo_reqwidth()
        scrapbook_height = 400
        scrapbook_images = []

        for image_file in scrapbook_image_files:
            image_path = os.path.join(scrapbook_images_dir, image_file)
            scrapbook_image = Image.open(image_path)
            resized_scrapbook_image = scrapbook_image.resize((scrapbook_width // 5, scrapbook_height), Image.LANCZOS)
            scrapbook_photo = ImageTk.PhotoImage(resized_scrapbook_image)

            # Randomly position each image within the scrapbook canvas
            x_position = random.randint(0, scrapbook_width - scrapbook_width // 5)
            y_position = random.randint(0, scrapbook_height - scrapbook_height)

            scrapbook_canvas.create_image(x_position, y_position, anchor=NW, image=scrapbook_photo)
            scrapbook_canvas.image = scrapbook_photo
            scrapbook_images.append(scrapbook_photo)






#From show ooks window

nav_frame = Frame(books_window, bg="white")
        nav_frame.pack(side=tk.TOP, fill=tk.X)

        # Add logo
        logo_path = "./images/logo.png"
        logo_image = Image.open(logo_path)
        logo_image = logo_image.resize((70, 40), Image.LANCZOS)
        logo_photo = ImageTk.PhotoImage(logo_image)

        logo_label = tk.Label(nav_frame, image=logo_photo, bg="white")
        logo_label.image = logo_photo
        logo_label.pack(side=tk.LEFT, padx=(10, 20))

        # Add navigation buttons to the right of the screen
        author_btn = ttk.Button(nav_frame, text="Home", style="Nav.TButton", command=books_window.destroy)
        author_btn.pack(side=tk.RIGHT, padx=(20, 10))

        reader_btn = ttk.Button(nav_frame, text="Logout", style="Nav.TButton", command=books_window.destroy)
        reader_btn.pack(side=tk.RIGHT, padx=(20, 10))

        # Create a frame for the books content
        books_frame = ttk.Frame(books_window, padding=(20, 20))
        books_frame.pack(padx=20, pady=20)

        # Add a label to display the list of books
        books_label = ttk.Label(books_frame, text="Books Read by User:")
        books_label.grid(row=0, column=0, sticky=tk.W, pady=(0, 5))

        # Display the list of books
        for i, book in enumerate(books, start=1):
            book_label = ttk.Label(books_frame, text=f"{i}. {book}")
            book_label.grid(row=i, column=0, sticky=tk.W, pady=(0, 5))