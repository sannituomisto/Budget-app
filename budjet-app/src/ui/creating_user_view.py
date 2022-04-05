from tkinter import Tk, ttk, constants, StringVar
from services.budget_services import budget_services, UsernameExistsError

class CreastingUser:
    def __init__ (self, root, handle_create_user, handle_show_login_view):
        self._root = root
        self._handle_create_user = handle_create_user
        self._handle_show_login_view = handle_show_login_view
        self._frame = None
        self._username_entry = None
        self._password_entry = None
        self._error_variable = None
        self._error_label = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)


    def destroy(self):
        self._frame.destroy()

    def _create_user_handler(self):
        username = self._username_entry.get()
        password = self._password_entry.get()

        if len(username) == 0 or len(password) == 0:
            self._show_error('Username and password is required')
            return

        if len(username) < 2:
            self._show_error('Username must be at least 2 characters')
            return

        if len(password) < 4 and any(char.isdigit() for char in password) == False:
            self._show_error('Password must be at least 4 characters and contain numbers')
            return
        
        if len(password) < 4:
            self._show_error('Password must be at least 4 characters')
            return

        if any(char.isdigit() for char in password) == False:
            self._show_error('Password must contain numbers')
            return

        try:
            budget_services.create_user(username, password)
            self._handle_create_user()

        except UsernameExistsError:
            self._show_error(f'Username {username} already exists')

    def _show_error(self, message):
        self._error_variable.set(message)
        self._error_label.grid()

    def _hide_error(self):
        self._error_label.grid_remove()

    def _initialize_username_field(self):
        username_label = ttk.Label(master=self._frame, text='Username')
        self._username_entry = ttk.Entry(master=self._frame)

        username_label.grid(padx=4, pady=4)
        self._username_entry.grid(row=1, column=1, sticky=constants.EW, padx=4, pady=4)

    def _initialize_password_field(self):
        password_label = ttk.Label(master=self._frame, text='Password')
        self._password_entry = ttk.Entry(master=self._frame)

        password_label.grid(padx=4, pady=4)
        self._password_entry.grid(row=2, column=1, sticky=constants.EW, padx=4, pady=4)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        self._error_variable = StringVar(self._frame)

        self._error_label = ttk.Label(master=self._frame,textvariable=self._error_variable)

        self._error_label.grid(padx=4, pady=4)

        self._initialize_username_field()
        self._initialize_password_field()

        create_user_button = ttk.Button(master=self._frame,text='Create account',command=self._create_user_handler)
        login_button = ttk.Button(master=self._frame,text='Login',command=self._handle_show_login_view)

        self._frame.grid_columnconfigure(1, weight=1, minsize=300)

        create_user_button.grid(columnspan=2, sticky=constants.EW, padx=4, pady=4)
        login_button.grid(columnspan=3, sticky=constants.EW, padx=4, pady=4)
        
        self._hide_error()