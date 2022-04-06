from tkinter import Tk, ttk, constants

class LoginView:
    def __init__(self, root):
        self._root = root

    def view(self):
        label = ttk.Label(master=self._root, text="Log in")
        username_label = ttk.Label(master=self._root, text="Username")
        username_entry = ttk.Entry(master=self._root)
        password_label = ttk.Label(master=self._root, text="Password")
        password_entry = ttk.Entry(master=self._root)
        create_button = ttk.Button(master=self._root, text="Log in") 
        not_user_label = ttk.Label(master=self._root, text="Don't have a user?")
        create_create_button = ttk.Button(master=self._root, text="Create a new user") 

        label.grid(row=0, column=0, columnspan=2)
        username_label.grid(row=1, column=0,sticky=(constants.E, constants.W),padx=5, pady=5)
        username_entry.grid(row=2, column=0, sticky=(constants.E, constants.W), padx=5, pady=5)
        password_label.grid(row=3, column=0,sticky=(constants.E, constants.W), padx=5, pady=5)
        password_entry.grid(row=4, column=0, sticky=(constants.E, constants.W), padx=5, pady=5)
        create_button.grid(columnspan=2, sticky=(constants.E, constants.W), padx=70, pady=5)
        not_user_label.grid(row=6, column=0,sticky=(constants.E, constants.W), padx=5, pady=5)
        create_create_button.grid(row=6,column=0, sticky=(constants.W), padx=140, pady=30)
        self._root.grid_columnconfigure(0, weight=1, minsize=400)


window = Tk()
window.title("Budjet-app")

ui = LoginView(window)
ui.view()

window.mainloop()
