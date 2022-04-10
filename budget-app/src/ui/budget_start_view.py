from tkinter import Tk, ttk, constants, StringVar

class BudgetStartView:
    def __init__(self, root):
        self._root = root
        self._categories = ('Food', 'Bills', 'Transportation',
                        'Clothes/accessories', 'Eating out', 'Entertainment', 'Sports', 
                        'Communication','House', 'Toiletry', 'Cosmetics', 'Other')


    def view(self):
        self._frame = ttk.Frame(master=self._root)
        self._option_var = StringVar(self._root)
        optionmenu_label=ttk.Label(master=self._root, text="Select category: ")
        option_menu = ttk.OptionMenu(self._root, self._option_var,self._categories[0],*self._categories)

        option_menu.grid(column=1, row=0, sticky=constants.W, padx=5, pady=5)
        optionmenu_label.grid(row=0, column=0, sticky=constants.W, padx=5, pady=5)



window = Tk()
window.title("TkInter example")

ui =BudgetStartView(window)
ui.view()

window.mainloop()