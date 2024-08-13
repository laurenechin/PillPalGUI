import tkinter
import customtkinter as ctk

#theme & color
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("dark-blue")

#window size & title
window = ctk.CTk()
window.title('Ready to Dispense')
window.geometry("800x480")

readyframe = ctk.CTkFrame (window,
                           width = 800,
                           height = 480)
readyframe.pack(padx=5, pady=5)
readyframe.pack_propagate(False)
label1 = ctk.CTkLabel(readyframe,
                      width = 800,
                      height = 500,
                      text = "You have 10 day(s) of Cymbalta left",
                      text_color = 'black',
                      font = ('Sans-Serif', 40, 'bold'),
                      fg_color = '#ffb9d5')
label1.place(relx=0.5, rely=0.55, anchor=tkinter.CENTER)

hi = ctk.CTkLabel(readyframe,
                  width = 800,
                  height = 80,
                  text = "Hi, PillPal User",
                  fg_color = '#ffff9c',
                  text_color = 'black',
                  font = ('Sans-Serif', 30, 'bold'))
hi.pack(padx=10, pady=10)
window.mainloop()
