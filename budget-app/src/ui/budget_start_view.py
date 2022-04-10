from tkinter import Tk, ttk, constants, StringVar

class BudgetStartView:
    def __init__(self, root):
        self._root = root
        self._frame = None
        self._categories = ('Food', 'Bills', 'Transportation',
                        'Clothes/accessories', 'Eating out', 'Entertainment', 'Sports', 
                        'Communication','House', 'Toiletry', 'Cosmetics', 'Other')
        self._view()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()


    def _view(self):
        self._frame = ttk.Frame(master=self._root)
        self._option_var = StringVar(self._frame)
        optionmenu_label=ttk.Label(master=self._frame, text="Select category: ")
        option_menu = ttk.OptionMenu(self._frame, self._option_var, self._categories[0],*self._categories)

        option_menu.grid(column=1, row=0, sticky=constants.W, padx=5, pady=5)
        optionmenu_label.grid(row=0, column=0, sticky=constants.W, padx=5, pady=5)

        self._frame.grid_columnconfigure(0, weight=1, minsize=400)
