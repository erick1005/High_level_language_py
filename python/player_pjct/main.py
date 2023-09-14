from tkinter import *

main_window = Tk() #instantiate window
main_window.geometry("780x480")   #size
main_window.title("Leaf player")

#change icon
icon = PhotoImage(file="D:\project\coding\source codes\High_level_languages\python\player_pjct\icon.png")
main_window.iconphoto(True,icon)
main_window.config(background="black")   #you can use any hex-decimal values of colors

main_window.mainloop()