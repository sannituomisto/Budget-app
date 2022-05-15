
from tkinter import Tk, ttk, constants, StringVar, PhotoImage
import string
from services.budget_services import budget_services


class BudgetNewExpenseView:
    """Vastaa uuden tulojen ja kulujen lisäämisnäkymästä """

    def __init__(self, root, handle_budget_start, handle_new_expense):
        """Tämä konstruktori luo uuden tulojen ja kulujen lisäämisnäkymän
        Args:
            root: TKinter-elementti, johon tulojen ja kulujen lisäämisnäkymä alustetaan
            handle_budget_start: UI-luokan metodi, jota kutsutaan, kun vaihdetaan budjettisovelluksen aloitus- eli kotinäkymään
            handle_new_expense: UI-luokan metodi, jota kutsutaan, kun vaihdetaan tulojen ja kulujen lisäämisnäkymään
                eli tässä tapauksessa, kun kutsutaan samaa näkymää, missä jo ollaan
        """
        self._root = root
        self._frame = None
        self._handle_budget_start = handle_budget_start
        self._handle_new_expense = handle_new_expense
        self._dwnd3 = PhotoImage(file='home.png')
        self._categories = ('Groceries', 'Bills', 'Transportation',
                            'Clothes/accessories', 'Restaurants', 'Entertainment', 'Sports',
                            'Communication', 'House', 'Toiletry/cosmetics', 'Other')
        self._amount_entry = None
        self._expense_amount_entry = None
        self._income_amount_entry = None
        self._option_menu = None
        self._variable = None
        self._error_var = None
        self._error_label = None
        self._ok_var = None
        self._ok_label = None
        self._user = budget_services.get_current_user()

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

    def _allowedchar(self):
        """Palauttaa syötekentissä hyväksytyt merkit"""
        allowed = string.digits+"."
        return allowed

    def _check_entry(self, amount):
        """Tarkistaa, että syötekenttiin ei ole annettu vääränlaisia merkkejä"""
        if len(amount) == 0:
            self._show_error('Please enter amount')
            return
        for i in amount:
            if i not in self._allowedchar():
                self._show_error('Please use only numbers and a dot')
                return
        count = 0
        for i in amount:
            if i == ".":
                count += 1
        if count > 1:
            self._show_error(
                'Please use only one dot to separate euros and cents')
            return
        return True

    def _creating_new_expense_handler(self):
        """Hoitaa uuden kulun luomisen"""
        amount = self._expense_amount_entry.get()
        category = self._get_selected(choice=None)
        if self._check_entry(amount) == True:
            budget_services.create_expense(amount, category, self._user[0])
            self._handle_new_expense()

    def _creating_new_income_handler(self):
        """Hoitaa uuden tulon luomisen"""
        amount = self._income_amount_entry.get()
        if self._check_entry(amount) == True:
            budget_services.create_income(amount, self._user[0])
            self._handle_new_expense()

    def _get_selected(self, choice):
        """Lukee pudotusvalikosta valitun arvon"""
        choice = self._variable.get()
        return choice

    def _initialize_labels(self):
        """Alustaa näkymän otsikot"""
        expense_label = ttk.Label(master=self._frame, text="New expense")
        expense_label.grid(row=1, column=0, columnspan=2,
                           sticky=(constants.W), padx=(215, 0), pady=3)

        income_label = ttk.Label(master=self._frame, text="New income")
        income_label.grid(row=8, column=0, columnspan=2, sticky=(
            constants.W), padx=(215, 0), pady=(0, 20))

        euro_label = ttk.Label(master=self._frame, text="€")
        euro_label.grid(row=4,  sticky=(constants.W), padx=(500, 5), pady=5)

        euro_label2 = ttk.Label(master=self._frame, text="€")
        euro_label2.grid(row=9, column=0, sticky=(
            constants.W), padx=(500, 5), pady=5)

        expense_amount_label = ttk.Label(master=self._frame, text="Amount: ")
        expense_amount_label.grid(
            row=4, column=0, sticky=constants.W, padx=(5, 0), pady=5)

        income_amount_label = ttk.Label(master=self._frame, text="Amount: ")
        income_amount_label.grid(
            row=9, column=0, sticky=constants.W, padx=(5, 0), pady=5)

        optionmenu_label = ttk.Label(
            master=self._frame, text="Select a category: ")
        optionmenu_label.grid(
            row=3, column=0, sticky=constants.W, padx=(5, 0), pady=5)

    def _initialize_entrys(self):
        """Alustaa näkymän syötekentät"""
        self._expense_amount_entry = ttk.Entry(master=self._frame)
        self._expense_amount_entry.grid(row=4, column=0, sticky=(
            constants.E, constants.W), padx=(70, 20), pady=5)

        self._income_amount_entry = ttk.Entry(master=self._frame)
        self._income_amount_entry.grid(row=9, column=0, sticky=(
            constants.E, constants.W), padx=(70, 20), pady=5)

    def _initialize_buttons(self):
        """Alustaa näkymän painikkeet"""
        s = ttk.Style()
        s.configure('income.TButton', foreground='green')
        s.configure('expense.TButton', foreground='red')

        expense_button = ttk.Button(
            master=self._frame, text="Add", style="expense.TButton", command=self._creating_new_expense_handler)
        expense_button.grid(row=5, columnspan=2, sticky=(
            constants.E, constants.W), padx=(140, 140), pady=5)

        income_button = ttk.Button(
            master=self._frame, text="Add", style="income.TButton", command=self._creating_new_income_handler)
        income_button.grid(row=10, columnspan=2, sticky=(
            constants.E, constants.W), padx=(140, 140), pady=(5, 40))

        home_button = ttk.Button(
            master=self._frame, image=self._dwnd3, command=self._handle_budget_start)
        home_button.grid(row=0, column=0, columnspan=1,
                         sticky=(constants.W), padx=(5, 0), pady=5)

    def _initialize_optionmenu(self):
        """Alustaa näkymän pudotusvalikon"""
        self._variable = StringVar(self._frame)
        self._variable.set(self._categories[3])
        option_menu = ttk.OptionMenu(
            self._frame, self._variable,  self._categories[0], *self._categories, command=self._get_selected)
        option_menu.grid(column=0, row=3, sticky=constants.W,
                         padx=(130, 0), pady=5)

    def _initialize_spacers(self):
        """Alustaa näkymän tyhjät rivit"""
        spacer1 = ttk.Label(master=self._frame, text="")
        spacer1.grid(row=6, column=0)

        spacer2 = ttk.Label(master=self._frame, text="")
        spacer2.grid(row=7, column=0)

        spacer3 = ttk.Label(master=self._frame, text="")
        spacer3.grid(row=2, column=0)

    def _initialize(self):
        """Alustaa tulojen ja kulujen lisäämisnäkymän pohjan ja kutsuu muita alustusmetodeja"""
        self._frame = ttk.Frame(master=self._root)

        self._error_var = StringVar(self._frame)
        self._error_label = ttk.Label(
            master=self._frame, textvariable=self._error_var, foreground='red')
        self._error_label.grid(row=11, padx=(5, 0), pady=5)

        self._initialize_labels()
        self._initialize_entrys()
        self._initialize_buttons()
        self._initialize_optionmenu()
        self._initialize_spacers()

        self._frame.grid_columnconfigure(0, weight=1, minsize=500)
        self._hide_error()
