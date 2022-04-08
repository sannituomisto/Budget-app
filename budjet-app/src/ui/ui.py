from tkinter import Tk
from ui.creating_user_view import CreateNewUserView
from ui.logging_in_view import LoginView

class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self._show_logging_in()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()
        self._current_view = None

    def _show_logging_in(self):
        self._hide_current_view()
        self._current_view = LoginView(self._root,self._handle_creating_user)
        self._current_view.pack()

    def _show_creating_user(self):
        self._hide_current_view()
        self._current_view = CreateNewUserView(self._root,self._handle_loggin_in)
        self._current_view.pack()

    def _handle_loggin_in(self):
        self._show_logging_in()

    def _handle_creating_user(self):
        self._show_creating_user()
