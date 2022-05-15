from tkinter import Tk, ttk, constants, StringVar
from services.budget_services import budget_services, UsernameError


class CreateNewUserView:
    """Vastaa uuden käyttäjän luomisnäkymästä"""

    def __init__(self, root, handle_loggin_in):
        """Tämä konstruktori luo uuden uuden käyttäjän luominäkymän
        Args:
            root: TKinter-elementti, johon uuden käyttäjän luomisnäkymä alustetaan
            handle_loggin_in: UI-luokan metodi, jota kutsutaan, kun vaihdetaan sisäänkirjautumisnäkymään
        """
        self._root = root
        self._frame = None
        self._handle_loggin_in = handle_loggin_in
        self.username_entry = None
        self.password_entry = None
        self._error_var = None
        self._error_label = None

        self._initialize()

    def pack(self):
        """Pakkaa näkymän"""
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Tuhoaa näkymän"""
        self._frame.destroy()

    def _show_error(self, errormessage):
        """Vastaa virheilmoituksen näyttämisestä"""
        self._error_var.set(errormessage)
        self._error_label.grid()

    def _hide_error(self):
        """Vastaa virheilmoituksen piilottamisesta"""
        self._error_label.grid_remove()

    def _creating_user_handler(self):
        """Hoitaa uuden käyttäjän luomisen"""
        username = self._username_entry.get()
        password = self._password_entry.get()
        if len(username) == 0 or len(password) == 0:
            self._show_error('Enter password and username')
            return

        if len(username) < 2:
            self._show_error('Username must be at least 2 characters')
            return

        if len(password) < 4 and any(char.isdigit() for char in password) == False:
            self._show_error(
                'Password must be at least 4 characters and contain numbers')
            return

        if len(password) < 4:
            self._show_error('Password must be at least 4 characters')
            return

        if any(char.isdigit() for char in password) == False:
            self._show_error('Password must contain numbers')
            return

        try:
            budget_services.create_user(username, password)
            self._handle_loggin_in()

        except UsernameError:
            self._show_error(
                f'Choose another username, {username} already exists')

    def _initialize_labels(self):
        """Alustaa näkymän otsikot"""
        label = ttk.Label(master=self._frame, text="Create a new user")
        label.grid(row=0, column=0, columnspan=2)

        username_label = ttk.Label(master=self._frame, text="Username")
        username_label.grid(row=1, column=0, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        password_label = ttk.Label(master=self._frame, text="Password")
        password_label.grid(row=3, column=0, sticky=(
            constants.E, constants.W), padx=5, pady=5)

    def _initialize_entrys(self):
        """Alustaa näkymän syötekentät"""
        self._username_entry = ttk.Entry(master=self._frame)
        self._username_entry.grid(row=2, column=0, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        self._password_entry = ttk.Entry(master=self._frame)
        self._password_entry.grid(row=4, column=0, sticky=(
            constants.E, constants.W), padx=5, pady=5)

    def _initialize_buttons(self):
        """Alustaa näkymän painikkeet"""
        create_button = ttk.Button(
            master=self._frame, text="CREATE USER", command=self._creating_user_handler)
        create_button.grid(row=5, columnspan=2, sticky=(
            constants.E, constants.W), padx=70, pady=5)

        login_button = ttk.Button(
            master=self._frame, text='Back to login', command=self._handle_loggin_in)
        login_button.grid(row=6, column=0, sticky=(
            constants.E, constants.W), padx=140, pady=5)

    def _initialize(self):
        """Alustaa uuden käyttäjän luomisnäkymän pohjan ja kutsuu muita alustusmetodeja"""
        self._frame = ttk.Frame(master=self._root)

        self._error_var = StringVar(self._frame)
        self._error_label = ttk.Label(
            master=self._frame, textvariable=self._error_var, foreground='red')
        self._error_label.grid(row=7, padx=5, pady=5)

        self._initialize_labels()
        self._initialize_entrys()
        self._initialize_buttons()

        self._frame.grid_columnconfigure(0, weight=1, minsize=400)
        self._hide_error()
