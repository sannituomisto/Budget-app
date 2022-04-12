from tkinter import Tk, ttk, constants, StringVar

class BudgetStartView:
    def __init__(self, root, handle_new_expense):
        self._root = root
        self._frame = None
        self._handle_new_expense= handle_new_expense
        self._view()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _view(self):
        self._frame = ttk.Frame(master=self._root)
        new_expense_button = ttk.Button(
            master=self._frame, text="Enter new expense or income", command=self._handle_new_expense)

        new_expense_button.grid(row=0, columnspan=2, sticky=(
            constants.E, constants.W), padx=70, pady=5)

        
        self._frame.grid_columnconfigure(0, weight=1, minsize=400)
