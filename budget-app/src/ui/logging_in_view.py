from tkinter import Tk, ttk, constants, StringVar
from services.budget_services import budget_services, InvalidCredentialsError


class LoginView:
    def __init__(self, root, handle_creating_user, handle_budget_start):
        self._root = root
        self._frame = None
        self._handle_budget_start = handle_budget_start
        self._handle_creating_user = handle_creating_user
        self.username_entry = None
        self.password_entry = None
        self._error_var = None
        self._error_label = None

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

    def _loggin_in_handler(self):
        username = self._username_entry.get()
        password = self._password_entry.get()

        try:
            budget_services.login(username, password)
            self._handle_budget_start()

        except InvalidCredentialsError:
            self._show_error('Invalid username or password')

    def _view(self):
        self._frame = ttk.Frame(master=self._root)
        self._error_var = StringVar(self._frame)
        self._error_label = ttk.Label(
            master=self._frame, textvariable=self._error_var, foreground='red')
        label = ttk.Label(master=self._frame, text="Log in")
        username_label = ttk.Label(master=self._frame, text="Username")
        self._username_entry = ttk.Entry(master=self._frame)
        password_label = ttk.Label(master=self._frame, text="Password")
        self._password_entry = ttk.Entry(master=self._frame)
        login_button = ttk.Button(
            master=self._frame, text="Log in", command=self._loggin_in_handler)
        not_user_label = ttk.Label(
            master=self._frame, text="Don't have a user?")
        create_create_button = ttk.Button(
            master=self._frame, text="Create a new user", command=self._handle_creating_user)

        self._error_label.grid(row=8, padx=5, pady=5)
        label.grid(row=0, column=0, columnspan=2)
        username_label.grid(row=1, column=0, sticky=(
            constants.E, constants.W), padx=5, pady=5)
        self._username_entry.grid(row=2, column=0, sticky=(
            constants.E, constants.W), padx=5, pady=5)
        password_label.grid(row=3, column=0, sticky=(
            constants.E, constants.W), padx=5, pady=5)
        self._password_entry.grid(row=4, column=0, sticky=(
            constants.E, constants.W), padx=5, pady=5)
        login_button.grid(row=6, columnspan=2, sticky=(
            constants.E, constants.W), padx=80, pady=5)
        not_user_label.grid(row=7, column=0, sticky=(
            constants.E, constants.W), padx=5, pady=5)
        create_create_button.grid(
            row=7, column=0, sticky=(constants.W), padx=140, pady=5)

        self._frame.grid_columnconfigure(0, weight=1, minsize=400)
        self._hide_error()
