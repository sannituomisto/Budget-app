from tkinter import Tk, ttk, constants, StringVar
from services.budget_services import budget_services, InvalidCredentialsError


class LoginView:
    """Vastaa sisäänkirjautuimisnäkymästä"""

    def __init__(self, root, handle_creating_user, handle_budget_start):
        """Tämä konstruktori luo uuden sisäänkirjautumisnäkymän
        Args:
            root: TKinter-elementti, johon sisäänkirjautumisnäkymä alustetaan
            handle_creating_user: UI-luokan metodi, jota kutsutaan, kun vaihdetaan uuden käyttäjän luomisnäkymään
            handle_budget_start: UI-luokan metodi, jota kutsutaan, kun vaihdetaan budjettisovelluksen aloitus- eli kotinäkymään
        """
        self._root = root
        self._frame = None
        self._handle_budget_start = handle_budget_start
        self._handle_creating_user = handle_creating_user
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
        """Vastaa virheilmoituksen esittämisestä"""
        self._error_var.set(errormessage)
        self._error_label.grid()

    def _hide_error(self):
        """Vastaa virheilmoituksen piilottamisesta"""
        self._error_label.grid_remove()

    def _loggin_in_handler(self):
        """Hoitaa sisäänkirjautumisen"""
        username = self._username_entry.get()
        password = self._password_entry.get()

        try:
            budget_services.login(username, password)
            self._handle_budget_start()

        except InvalidCredentialsError:
            self._show_error('Invalid username or password')

    def _initialize_labels(self):
        """Alustaa näkymän otsikot"""
        label = ttk.Label(master=self._frame, text="Log in")
        label.grid(row=0, column=0, columnspan=2)

        username_label = ttk.Label(master=self._frame, text="Username")
        username_label.grid(row=1, column=0, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        password_label = ttk.Label(master=self._frame, text="Password")
        password_label.grid(row=3, column=0, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        not_user_label = ttk.Label(
            master=self._frame, text="Don't have a user?")
        not_user_label.grid(row=7, column=0, sticky=(
            constants.E, constants.W), padx=5, pady=5)

    def _initialize_buttons(self):
        """Alustaa näkymän painikkeet"""
        login_button = ttk.Button(
            master=self._frame, text="LOG IN", command=self._loggin_in_handler)
        login_button.grid(row=6, columnspan=2, sticky=(
            constants.E, constants.W), padx=80, pady=5)

        create_create_button = ttk.Button(
            master=self._frame, text="Create a new user", command=self._handle_creating_user)
        create_create_button.grid(
            row=7, column=0, sticky=(constants.W), padx=140, pady=5)

    def _initialize_entrys(self):
        """Alustaa näkymän syötekentät"""
        self._username_entry = ttk.Entry(master=self._frame)
        self._username_entry.grid(row=2, column=0, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        self._password_entry = ttk.Entry(master=self._frame)
        self._password_entry.grid(row=4, column=0, sticky=(
            constants.E, constants.W), padx=5, pady=5)

    def _initialize(self):
        """Alustaa sisäänkirjautumisnäkymän pohjan ja kutsuu muita alustus metodeja"""
        self._frame = ttk.Frame(master=self._root)

        self._error_var = StringVar(self._frame)
        self._error_label = ttk.Label(
            master=self._frame, textvariable=self._error_var, foreground='red')
        self._error_label.grid(row=8, padx=5, pady=5)

        self._initialize_labels()
        self._initialize_entrys()
        self._initialize_buttons()

        self._frame.grid_columnconfigure(0, weight=1, minsize=400)
        self._hide_error()
