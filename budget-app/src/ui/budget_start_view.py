from tkinter import END, Listbox, Tk, ttk, constants, StringVar, Scrollbar
from repositories import budget_repository
from services.budget_services import budget_services
from repositories.budget_repository import budget_repository


class BudgetStartView:
    def __init__(self, root, handle_new_expense, handle_log_out):
        self._root = root
        self._frame = None
        self._handle_new_expense = handle_new_expense
        self._handle_log_out = handle_log_out
        self._user = budget_services.get_current_user()
        self._income_sum = budget_services.get_income_sum(self._user[0])
        self._expense_sum = budget_services.get_expense_sum(self._user[0])
        self._incomes = budget_services.get_all_incomes(self._user[0])
        self._expenses = budget_services.get_all_expenses(self._user[0])
        self._clear=budget_services.delete_all_from_user(self._user[0])
        self._view()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _log_out_handler(self):
        budget_services.log_out()
        self._handle_log_out()

    def _view(self):
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, text="Budget-app", font='bold')
        new_expense_button = ttk.Button(
            master=self._frame, text="Enter new expense or income", command=self._handle_new_expense)
        log_out_button = ttk.Button(
            master=self._frame, text="LOG OUT", command=self._log_out_handler)
        clear_button = ttk.Button(
            master=self._frame, text="Clear your budget", command=self._clear)
        balance_label = ttk.Label(
            master=self._frame, text=f"Balance: {self._income_sum-self._expense_sum} €")
        expenses_label = ttk.Label(master=self._frame, text=f"Expenses")
        incomes_label = ttk.Label(master=self._frame, text=f"Incomes")
        expenses_sum_label = ttk.Label(
            master=self._frame, text=f"{self._expense_sum} €")
        incomes_sum_label = ttk.Label(
            master=self._frame, text=f"{self._income_sum} €")
        expenses_box = Listbox(master=self._frame)
        incomes_box = Listbox(master=self._frame)
        for expense in self._expenses:
            expenses_box.insert(END, expense)
        for income in self._incomes:
            incomes_box.insert(END, income)
        scroll = Scrollbar(master=self._frame)
        scroll2 = Scrollbar(master=self._frame)
        expenses_box.config(yscrollcommand=scroll.set)
        incomes_box.config(yscrollcommand=scroll2.set)
        scroll.config(command=expenses_box.yview)
        scroll2.config(command=expenses_box.yview)
        label.grid(row=0, column=0, columnspan=2)
        new_expense_button.grid(row=5, columnspan=2, sticky=(
            constants.E, constants.W), padx=70, pady=5)
        clear_button.grid(row=6, columnspan=2, sticky=(
            constants.E, constants.W), padx=70, pady=5)
        log_out_button.grid(row=0, columnspan=2, sticky=(
            constants.E), padx=10, pady=5)
        expenses_box.grid(row=4, sticky=(
            constants.W), columnspan=2, padx=15, pady=5)
        incomes_box.grid(row=4, sticky=(constants.E),
                         columnspan=2, padx=30, pady=5)
        scroll.grid(row=4, columnspan=2, sticky=(
            constants.NS, constants.W), padx=180, pady=5)
        scroll2.grid(row=4, columnspan=2, sticky=(
            constants.NS, constants.E), padx=15, pady=5)
        expenses_label.grid(row=2, column=0, columnspan=2, sticky=(
            constants.W), padx=70)
        incomes_label.grid(row=2, column=0, columnspan=2, sticky=(
            constants.E), padx=82)
        balance_label.grid(row=1, column=0, columnspan=2, sticky=(
            constants.E), padx=155, pady=5)
        expenses_sum_label.grid(row=3, column=0, columnspan=2, sticky=(
            constants.W), padx=80)
        incomes_sum_label.grid(row=3, column=0, columnspan=2, sticky=(
            constants.E), padx=85)

        self._frame.grid_columnconfigure(0, weight=1, minsize=400)
