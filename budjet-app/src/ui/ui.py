from ui.creating_user_view import CreateNewUserView
from ui.logging_in_view import LoginView
from ui.budjet_start_view import BudjetStartView

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
        self._current_view = LoginView(self._root,self._handle_creating_user, self._handle_budjet_start)
        self._current_view.pack()

    def _show_creating_user(self):
        self._hide_current_view()
        self._current_view = CreateNewUserView(self._root,self._handle_loggin_in)
        self._current_view.pack()

    def _show_budjet_start(self):
        self._hide_current_view()
        self._current_view= BudjetStartView(self._root)

    def _handle_loggin_in(self):
        self._show_logging_in()

    def _handle_creating_user(self):
        self._show_creating_user()

    def _handle_budjet_start(self):
        self._show_budjet_start()

