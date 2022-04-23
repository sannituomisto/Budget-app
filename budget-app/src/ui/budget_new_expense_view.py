
from tkinter import Tk, ttk, constants, StringVar, PhotoImage
from services.budget_services import budget_services


class BudgetNewExpenseView:
    def __init__(self, root, handle_budget_start, handle_new_expense):
        self._root = root
        self._frame = None
        self._handle_budget_start = handle_budget_start
        self._handle_new_expense = handle_new_expense
        self._dwnd3 = PhotoImage(file='home.png')
        self._categories = ('Food', 'Bills', 'Transportation',
                            'Clothes/accessories', 'Eating out', 'Entertainment', 'Sports',
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

    def _creating_new_expense_handler(self):
        amount = self._expense_amount_entry.get()
        category = self._get_selected(choice=None)
        if len(amount) == 0:
            self._show_error('Please enter amount')
            return
        budget_services.create_expense(amount, category, self._user[0])
        self._handle_new_expense()

    def _creating_new_income_handler(self):
        amount = self._income_amount_entry.get()
        if len(amount) == 0:
            self._show_error('Please enter amount')
            return
        budget_services.create_income(amount, self._user[0])
        self._handle_new_expense()

    def _get_selected(self, choice):
        choice = self._variable.get()
        return choice

    def _view(self):
        self._frame = ttk.Frame(master=self._root)
        s = ttk.Style()
        s.configure('income.TButton', foreground='green')
        s.configure('expense.TButton', foreground='red')
        income_button = ttk.Button(
            master=self._frame, text="Enter", style="income.TButton", command=self._creating_new_income_handler)
        expense_button = ttk.Button(
            master=self._frame, text="Enter", style="expense.TButton", command=self._creating_new_expense_handler)
        home_button = ttk.Button(
            master=self._frame, image=self._dwnd3, command=self._handle_budget_start)
        label = ttk.Label(master=self._frame, text="Budget-app", font='bold')
        expense_label = ttk.Label(master=self._frame, text="New expense")
        euro_label = ttk.Label(master=self._frame, text="€")
        euro_label2 = ttk.Label(master=self._frame, text="€")
        income_label = ttk.Label(master=self._frame, text="New income")
        expense_amount_label = ttk.Label(master=self._frame, text="Amount: ")
        income_amount_label = ttk.Label(master=self._frame, text="Amount: ")
        self._expense_amount_entry = ttk.Entry(master=self._frame)
        self._income_amount_entry = ttk.Entry(master=self._frame)
        self._error_var = StringVar(self._frame)
        self._error_label = ttk.Label(
            master=self._frame, textvariable=self._error_var, foreground='red')
        spacer1 = ttk.Label(master=self._frame, text="")
        spacer2 = ttk.Label(master=self._frame, text="")
        spacer3 = ttk.Label(master=self._frame, text="")

        self._variable = StringVar(self._frame)
        self._variable.set(self._categories[3])
        optionmenu_label = ttk.Label(
            master=self._frame, text="Select category: ")
        option_menu = ttk.OptionMenu(
            self._frame, self._variable,  self._categories[0], *self._categories, command=self._get_selected)

        label.grid(row=0, column=0, columnspan=2)
        euro_label.grid(row=4, column=0, sticky=(constants.E), padx=60, pady=5)
        euro_label2.grid(row=9, column=0, sticky=(
            constants.E), padx=60, pady=5)
        income_button.grid(row=10, columnspan=2, sticky=(
            constants.E, constants.W), padx=200, pady=5)
        expense_button.grid(row=5, columnspan=2, sticky=(
            constants.E, constants.W), padx=200, pady=5)
        home_button.grid(row=0, column=0, columnspan=1,
                         sticky=(constants.W), padx=5, pady=5)
        expense_label.grid(row=2, column=0, columnspan=2)
        income_label.grid(row=8, column=0, columnspan=2)
        self._error_label.grid(row=11, padx=5, pady=5)
        option_menu.grid(column=0, row=3, sticky=constants.W, padx=130, pady=5)
        optionmenu_label.grid(
            row=3, column=0, sticky=constants.W, padx=5, pady=5)
        expense_amount_label.grid(
            row=4, column=0, sticky=constants.W, padx=5, pady=5)
        income_amount_label.grid(
            row=9, column=0, sticky=constants.W, padx=5, pady=5)
        self._expense_amount_entry.grid(row=4, column=0, sticky=(
            constants.E, constants.W), padx=80, pady=5)
        self._income_amount_entry.grid(row=9, column=0, sticky=(
            constants.E, constants.W), padx=80, pady=5)
        spacer1.grid(row=6, column=0)
        spacer2.grid(row=7, column=0)
        spacer3.grid(row=1, column=0)

        self._frame.grid_columnconfigure(0, weight=1, minsize=500)
        self._hide_error()
