import tkinter
from tkinter import *
import customtkinter as ctk
from PIL import Image

#theme & color
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

#window size & title
window = ctk.CTk()
window.title('PillPal GUI')
window.iconbitmap('images/codemy.ico')
window.geometry("800x480")

bg = ctk.CTkLabel(window,
                  width = 800,
                  height = 500,
                  text = "",
                  fg_color = '#ffb9d5')
bg.pack(padx=5, pady=5)
bg.pack_propagate(False)

hi = ctk.CTkLabel(bg,
                  width = 800,
                  height = 80,
                  text = "Hi, PillPal User",
                  fg_color = '#ffff9c',
                  text_color = 'black',
                  font = ('Sans-Serif', 30, 'bold'))
hi.pack(padx=10, pady=10)

streak = ctk.CTkLabel(bg,
                      text = "You're on a \n [] day streak!",
                      font = ('Sans-Serif', 40, 'bold'))
streak.place(relx=0.35, rely=0.5, anchor=tkinter.CENTER)

fireimage = ctk.CTkImage(Image.open('fire_image.png').convert('RGBA'), size=(200,200))
firephoto = ctk.CTkLabel(window,
                         text = "",
                         image = fireimage,
                         fg_color = '#ffb9d5')
firephoto.place(relx = 0.65, rely = 0.5, anchor=tkinter.CENTER)

window.mainloop()
