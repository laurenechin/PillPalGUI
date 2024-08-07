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
                      text = "It's time to take [Pill Name], [Name]",
                      text_color = 'black',
                      font = ('Sans-Serif', 40, 'bold'),
                      fg_color = '#ffb9d5')
label1.place(relx=0.5, rely=0.45, anchor=tkinter.CENTER)

dispenseframe = ctk.CTkFrame (window,
                              width = 800,
                              height = 480)
dispenseframe.pack(padx=5, pady=5)
dispenseframe.pack_propagate(False)
label2 = ctk.CTkLabel(dispenseframe,
                      width = 800,
                      height = 500,
                      text = "Dispensing...",
                      text_color = 'black',
                      font = ('Sans-Serif', 40, 'bold'),
                      fg_color = '#ffb9d5')
label2.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

pages = [readyframe, dispenseframe]
count = 0

def next_page():
        global count

        if not count > len(pages) -2:
                for p in pages:
                        p.pack_forget()

                count += 1
                page = pages[count]
                page.pack(padx=5, pady=5)

button1 = ctk.CTkButton(readyframe,
                        text="Dispense Now",
                        text_color='black',
                        font = ('Sans-Serif', 20, 'bold'),
                        width=300,
                        height=75,
                        fg_color='#ff78ae',
                        border_width=5,
                        border_color='red',
                        hover_color='red',
                        command=next_page)
button1.place(relx=0.5, rely=0.65, anchor=tkinter.CENTER)
window.mainloop()
