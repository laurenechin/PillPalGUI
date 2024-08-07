import tkinter
import customtkinter as ctk     #pysimplegui extension

#theme & color
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

#window size & title
window = ctk.CTk()
window.title('PillPal GUI')
window.geometry("800x480")


schedule = ctk.CTkLabel(window,
                        width = 800,
                        height = 80,
                        text = "SCHEDULE",
                        fg_color = '#cde6e2',
                        text_color = 'black',
                        font = ('Sans-Serif', 30, 'bold'))
schedule.pack(padx=10, pady=5)

p1frame = ctk.CTkFrame (window,
                          width = 180,
                          height = 390,
                          border_width = 7,
                          fg_color = '#d4ffc3',
                          border_color = '#FF8E8E')     #red
p1frame.pack(side="left", padx=10, pady=5)
p1frame.pack_propagate(False)

label1 = ctk.CTkLabel(p1frame,
                      text = "Pill Name",
                      text_color = 'black',
                      font = ('Sans-Serif', 24, 'bold'))
label1.place(x=12, y=12)
label2 = ctk.CTkLabel(p1frame,
                      text = "DESCRIPTION",
                      text_color = 'black',
                      font = ('Sans-Serif', 18))
label2.place(x=12, y=50)
label3 = ctk.CTkLabel(p1frame,
                      text = "Quantity Left: ",
                      text_color = 'black',
                      font = ('Sans-Serif', 18))
label3.place(x=12, y=150)
label4 = ctk.CTkLabel(p1frame,
                      text = "[Time]",
                      text_color = 'black',
                      font = ('Sans-Serif', 18, 'bold'))
label4.place(relx=0.5, rely=0.75, anchor= tkinter.CENTER)

pill2frame = ctk.CTkFrame (window,
                          width = 180,
                          height = 390,
                          border_width = 7,
                          fg_color = '#fffde4',
                          border_color = '#97B0FF')     #blue
pill2frame.pack(side="left", padx=10, pady=5)
pill2frame.pack_propagate(False)

pill4frame = ctk.CTkFrame (window,
                          width = 180,
                          height = 390,
                          border_width = 7,
                          fg_color = '#fffde4',
                          border_color = '#8ddb6b')     #green
pill4frame.pack(side="right", padx=10, pady=5)
pill4frame.pack_propagate(False)

pill3frame = ctk.CTkFrame (window,
                          width = 180,
                          height = 390,
                          border_width = 7,
                          fg_color = '#fffde4',
                          border_color = '#BD97FF')     #purple
pill3frame.pack(side="right", padx=10, pady=5)
pill3frame.pack_propagate(False)

button = ctk.CTkButton(master=window, text="button", width=40, height=40)
button.place(x=732, y=5)


window.mainloop()


