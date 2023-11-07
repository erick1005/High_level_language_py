import tkinter as tk

root_window = tk.Tk()
root_window.geometry("800x600")
root_label = tk.Label(root_window, text='Hello World',
                       relief="ridge",
                       border=10,
                      )
root_label.pack()

root_window.mainloop()