from tkinter import END, Listbox, Tk, ttk, constants, StringVar, Scrollbar
from services.budget_services import budget_services


class BudgetStartView:
    """Vastaa budjettisovelluksen aloitus- eli kotinäkymästä"""

    def __init__(self, root, handle_new_expense, handle_log_out, handle_budget_start):
        """Tämä konstruktori luo uuden kotinäkymän
        Args:
            root: TKinter-elementti, johon kotinäkymä alustetaan
            handle_new_expense: UI-luokan metodi, jota kutsutaan, kun vaihdetaan tulojen ja kulujen lisäämisnäkymään
            handle_log_out: UI-luokan metodi, jota kutsutaan, kun vaihdetaan sisäänkirjautuimsnäkymään
            handle_budget_start: UI-luokan metodi, jota kutsutaan, kun vaihdetaan budjettisovelluksen aloitus- eli kotinäkymään
                eli tässä tapauksessa, kun kutsutaan samaa näkymää, missä jo ollaan
        """
        self._root = root
        self._frame = None
        self._handle_new_expense = handle_new_expense
        self._handle_log_out = handle_log_out
        self._handle_budget_start = handle_budget_start
        self._user = budget_services.get_current_user()
        self._variable = None
        self._sum_var = None
        self._sum_label = None
        self._categories = ('Groceries', 'Bills', 'Transportation',
                            'Clothes/accessories', 'Restaurants', 'Entertainment', 'Sports',
                            'Communication', 'House', 'Toiletry/cosmetics', 'Other')
        self._initialize()

    def pack(self):
        """Pakkaa näkymän"""
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Tuhoaa näkymän"""
        self._frame.destroy()

    def _show_sum(self, errormessage):
        """Vastaa virheilmoituksen näyttämisestä"""
        self._sum_var.set(errormessage)
        self._sum_label.grid()

    def _hide_sum(self):
        """Vastaa virheilmoituksen piilottamisesta"""
        self._sum_label.grid_remove()

    def _log_out_handler(self):
        """Hoitaa uloskirjautumisen"""
        budget_services.log_out()
        self._handle_log_out()

    def _delete_budget_handler(self):
        """Hoitaa käyttäjän tulojen ja menojen nollaamisen"""
        budget_services.delete_all_from_user(self._user[0])
        self._handle_budget_start()

    def _expense_sum_handler(self):
        """Hakee ja palauttaa käyttäjän kulujen summan"""
        expense_sum = budget_services.get_expense_sum(self._user[0])
        return expense_sum

    def _income_sum_handler(self):
        """Hakee ja palauttaa käyttäjän tulojen summan"""
        income_sum = budget_services.get_income_sum(self._user[0])
        return income_sum

    def _all_income_handler(self):
        """Hakee ja palauttaa käyttäjän kaikki tulot listana"""
        all_income = budget_services.get_all_incomes(self._user[0])
        return all_income

    def _all_expense_handler(self):
        """Hakee ja palauttaa käyttäjän kaikki kulut listana"""
        all_expense = budget_services.get_all_expenses(self._user[0])
        return all_expense

    def _get_selected(self, choice):
        """Lukee pudotusvalikosta valitun arvon"""
        choice = self._variable.get()
        amount = budget_services.get_expense_sum_by_category(
            self._user[0], choice)
        self._show_sum(f'{amount} €')
        return

    def _initialize_sum_by_category(self):
        """Alustaa toiminnot, joilla saadaan näytettyä käyttäjän kulujen summan kategorioittain """
        self._variable = StringVar(self._frame)
        self._variable.set(self._categories[3])

        option_menu = ttk.OptionMenu(
            self._frame, self._variable, "Select a category", *self._categories, command=self._get_selected)
        option_menu.grid(column=0, columnspan=2, row=5,
                         sticky=(constants.W), padx=(170, 0), pady=5)

        self._sum_var = StringVar(self._frame)
        self._sum_label = ttk.Label(
            master=self._frame, textvariable=self._sum_var)
        self._sum_label.grid(row=6, padx=5, pady=5)

        category_sum_label = ttk.Label(
            master=self._frame, text=f"Total sum by category:")
        category_sum_label.grid(row=5, column=0, columnspan=2, sticky=(
            constants.W), padx=(15, 0))

    def _initialize_boxes(self):
        """Alustaa näkymän kulu- ja tulolaatikot"""
        expenses_box = Listbox(master=self._frame)
        for expense in self._all_expense_handler():
            expenses_box.insert(END, expense)
        scroll = Scrollbar(master=self._frame)
        expenses_box.config(yscrollcommand=scroll.set)
        scroll.config(command=expenses_box.yview)
        expenses_box.grid(row=4, sticky=(
            constants.W), columnspan=2, padx=(15, 0), pady=5)
        scroll.grid(row=4, columnspan=2, sticky=(
            constants.NS, constants.W), padx=180, pady=5)

        incomes_box = Listbox(master=self._frame)
        for income in self._all_income_handler():
            incomes_box.insert(END, income)
        scroll2 = Scrollbar(master=self._frame)
        incomes_box.config(yscrollcommand=scroll2.set)
        scroll2.config(command=expenses_box.yview)
        incomes_box.grid(row=4, sticky=(constants.W),
                         columnspan=2, padx=(220, 0), pady=5)
        scroll2.grid(row=4, columnspan=2, sticky=(
            constants.NS, constants.W), padx=(385, 15), pady=5)

    def _initialize_labels(self):
        """Alustaa näkymän otsikot"""
        s = ttk.Style()
        s.configure('balance.TLabel', foreground='red')

        label = ttk.Label(master=self._frame, text="Budget-app", font='bold')
        label.grid(row=0, column=0, columnspan=2,
                   sticky=constants.W, padx=(155, 0))

        if (self._income_sum_handler()-self._expense_sum_handler()) < 0:
            balance_label = ttk.Label(
                master=self._frame, text=f"Balance: {self._income_sum_handler()-self._expense_sum_handler()} €", style="balance.TLabel")
        else:
            balance_label = ttk.Label(
                master=self._frame, text=f"Balance: {self._income_sum_handler()-self._expense_sum_handler()} €")
        balance_label.grid(row=1, column=0, columnspan=2, sticky=(
            constants.W), padx=(15, 0), pady=5)

        expenses_label = ttk.Label(master=self._frame, text=f"Expenses:")
        expenses_label.grid(row=2, column=0, columnspan=2, sticky=(
            constants.W), padx=(15, 0))

        incomes_label = ttk.Label(master=self._frame, text=f"Incomes:")
        incomes_label.grid(row=2, column=0, columnspan=2, sticky=(
            constants.W), padx=(220, 0))

    def _initialize_sums(self):
        """Alustaa näkymän tulojen ja kulujen summat ja niiden otsikot"""
        expenses_sum_label = ttk.Label(
            master=self._frame, text=f"{self._expense_sum_handler()} €")
        expenses_sum_label.grid(row=3, column=0, columnspan=2, sticky=(
            constants.W), padx=(15, 0))

        incomes_sum_label = ttk.Label(
            master=self._frame, text=f"{self._income_sum_handler()} €")
        incomes_sum_label.grid(row=3, column=0, columnspan=2, sticky=(
            constants.W), padx=(220, 0))

    def _initialize_buttons(self):
        """Alustaa näkymän painikkeet"""
        new_expense_button = ttk.Button(
            master=self._frame, text="Add new expense or income", command=self._handle_new_expense)
        new_expense_button.grid(row=7, columnspan=2, sticky=(
            constants.W), padx=(110, 0), pady=5)

        log_out_button = ttk.Button(
            master=self._frame, text="LOG OUT", command=self._log_out_handler)
        log_out_button.grid(row=0, columnspan=2, sticky=(
            constants.W), padx=(315, 0), pady=5)

        clear_button = ttk.Button(
            master=self._frame, text="Clear your budget", command=self._delete_budget_handler)
        clear_button.grid(row=8, columnspan=2, sticky=(
            constants.W), padx=(140, 0), pady=5)

    def _initialize(self):
        """Alustaa kotinäkymän pohjan ja kutsuu muita alustusmetodeja"""
        self._frame = ttk.Frame(master=self._root)

        self._initialize_labels()
        self._initialize_sums()
        self._initialize_boxes()
        self._initialize_sum_by_category()
        self._initialize_buttons()

        self._frame.grid_columnconfigure(0, weight=1, minsize=400)
        self._hide_sum()
