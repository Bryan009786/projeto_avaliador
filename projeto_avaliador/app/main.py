import tkinter as tk
from app.views.cliente_view import ClienteView

def main():
    root = tk.Tk()
    app = ClienteView(root)
    root.mainloop()

if __name__ == "__main__":
    main()
