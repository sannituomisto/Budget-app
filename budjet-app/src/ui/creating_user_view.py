from tkinter import Tk, ttk, constants, StringVar
from services.budjet_services import budjet_services, UsernameError

class CreateNewUserView:
    def __init__(self, root, handle_loggin_in):
        self._root = root
        self._frame = None
        self._handle_loggin_in=handle_loggin_in
        self.username_entry=None
        self.password_entry=None
        self._error_var=None
        self._error_label=None

        self._view()


    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _show_error(self, errormessage):
        self._error_var.set(errormessage)
        self._error_label.grid()

    def _hide_error(self):
        self._error_label.grid_remove()

    def _creating_user_handler(self):
        username = self._username_entry.get()
        password = self._password_entry.get()
        if len(username) == 0 or len(password) == 0:
            self._show_error('Enter password and username')
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
            budjet_services.create_user(username, password)
            self._handle_loggin_in

        except UsernameError:
            self._show_error(f'Choose another password, {username} already exists')


    def _view(self):
        self._frame = ttk.Frame(master=self._root)
        self._error_variable = StringVar(self._frame)
        self._error_label = ttk.Label(master=self._frame,textvariable=self._error_var)
        label = ttk.Label(master=self._root, text="Create a new user")
        username_label = ttk.Label(master=self._root, text="Username")
        self._username_entry = ttk.Entry(master=self._root)
        password_label = ttk.Label(master=self._root, text="Password")
        self._password_entry = ttk.Entry(master=self._root)
        create_button = ttk.Button(master=self._root, text="CREATE USER",command=self._creating_user_handler)
        login_button = ttk.Button(master=self._frame,text='Back to login',command=self._handle_loggin_in)

        self._error_label.grid(padx=5, pady=5)
        label.grid(row=0, column=0, columnspan=2)
        username_label.grid(row=1, column=0,sticky=(constants.E, constants.W),padx=5, pady=5)
        self._username_entry.grid(row=2, column=0, sticky=(constants.E, constants.W), padx=5, pady=5)
        password_label.grid(row=3, column=0,sticky=(constants.E, constants.W), padx=5, pady=5)
        self._password_entry.grid(row=4, column=0, sticky=(constants.E, constants.W), padx=5, pady=5)
        create_button.grid(row=5,columnspan=2, sticky=(constants.E, constants.W), padx=70, pady=5)
        login_button.grid(row=6, column=0,sticky=(constants.E, constants.W), padx=5, pady=5)


        self._root.grid_columnconfigure(0, weight=1, minsize=400)
        self._hide_error()
