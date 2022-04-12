from ui.ui import UI
from tkinter import Tk


def main():
    window = Tk()
    window.title('Budget-app')
    ui_view = UI(window)
    ui_view.start()
    window.mainloop()


if __name__ == '__main__':
    main()
