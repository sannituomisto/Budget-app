from tkinter import Tk, ttk, constants, StringVar, PhotoImage

class BudgetNewExpenseView:
    def __init__(self, root):
        self._root = root
        self._frame=None
        self._dwnd = PhotoImage(file='plus2.png')
        self._dwnd2 = PhotoImage(file='minus2.png')
        self._dwnd3 = PhotoImage(file='home.png')
        self._categories = ('Food', 'Bills', 'Transportation',
                        'Clothes/accessories', 'Eating out', 'Entertainment', 'Sports', 
                        'Communication','House', 'Toiletry/cosmetics', 'Other')
        self._amount_entry=None
        self._expense_amount_entry=None
        self._income_amount_entry=None

        self._view()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()


    def _view(self):
        self._frame = ttk.Frame(master=self._root)
        s = ttk.Style()
        s.configure("plus/minus_button.TButton", backround="systemTransparent", activebackground="-transparent")
        plus_button = ttk.Button(master=self._frame, image=self._dwnd, style="plus/minus_button.TButton")
        minus_button = ttk.Button(master=self._frame, image=self._dwnd2, style="plus/minus_button.TButton")
        home_button = ttk.Button(master=self._frame, image=self._dwnd3, style="plus/minus_button.TButton")
        label = ttk.Label(master=self._root, text="Budget-app")
        expense_label = ttk.Label(master=self._frame, text="New expense")
        euro_label = ttk.Label(master=self._frame, text="€")
        euro_label2 = ttk.Label(master=self._frame, text="€")
        income_label = ttk.Label(master=self._frame, text="New income")
        self._option_var = StringVar(self._frame)
        expense_amount_label = ttk.Label(master=self._frame, text="Amount: ")
        income_amount_label = ttk.Label(master=self._frame, text="Amount: ")
        self._expense_amount_entry = ttk.Entry(master=self._frame)
        self._income_amount_entry = ttk.Entry(master=self._frame)
        optionmenu_label=ttk.Label(master=self._frame, text="Select category: ")
        option_menu = ttk.OptionMenu(self._frame, self._option_var, self._categories[0],*self._categories)



        label.grid(row=0, column=0, columnspan=2)
        euro_label.grid(row=3, column=0, sticky=(constants.E), padx=60, pady=5)
        euro_label2.grid(row=6, column=0, sticky=(constants.E), padx=60, pady=5)
        plus_button.grid(row=7, column=0,columnspan=2, padx=50, pady=5)
        minus_button.grid(row=4, column=0,columnspan=2, padx=50, pady=5)
        home_button.grid(row=0, column=0,columnspan=1,sticky=(constants.W), padx=5, pady=5)
        expense_label.grid(row=1, column=0, columnspan=2)
        income_label.grid(row=5, column=0, columnspan=2)
        option_menu.grid(column=0, row=2, sticky=constants.W, padx=130, pady=5)
        optionmenu_label.grid(row=2, column=0, sticky=constants.W, padx=5, pady=5)
        expense_amount_label.grid(row=3, column=0, sticky=constants.W, padx=5, pady=5)
        income_amount_label.grid(row=6, column=0, sticky=constants.W, padx=5, pady=5)
        self._expense_amount_entry.grid(row=3, column=0, sticky=(constants.E, constants.W), padx=80, pady=5)
        self._income_amount_entry.grid(row=6, column=0, sticky=(constants.E, constants.W), padx=80, pady=5)
        self._root.grid_columnconfigure(0, weight=1, minsize=400)
