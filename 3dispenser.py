import tkinter
import customtkinter as ctk

# Theme & color
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("dark-blue")

class MyApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title('PillPal GUI')
        self.geometry("800x480")

        self.container = ctk.CTkFrame(self)
        self.container.pack(fill="both", expand=True)

        self.frames = {}
        self.show_frame(Streak1)

    def show_frame(self, page_class):
        frame = self.frames.get(page_class)
        if frame is None:
                        frame = page_class(parent=self.container, controller=self)
                        self.frames[page_class] = frame
                        frame.grid(row=0, column=0, sticky="nsew")

        frame.tkraise()
#----------------------------------------------------------STREAKFRAME
class Streak1(ctk.CTkFrame):
        def __init__(self, parent, controller):
                super().__init__(parent)
                self.controller = controller

                streak = ctk.CTkLabel(self,
                                      width=800,
                                      height=480,
                                      text = "You're on a \n [] day streak!",
                                      font = ('Sans-Serif', 40, 'bold'),
                                      fg_color = '#ffb9d5')
                streak.pack()

                button2 = ctk.CTkButton(self,
                                        text="Next",
                                        text_color='black',
                                        font = ('Sans-Serif', 20, 'bold'),
                                        width=300,
                                        height=75,
                                        fg_color='#ff78ae',
                                        border_width=5,
                                        border_color='red',
                                        hover_color='red',
                                        command=lambda: self.controller.show_frame(Ready2))
                button2.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)
                
                hi = ctk.CTkLabel(self,
                                  width = 800,
                                  height = 80,
                                  text="Hi, PillPal User",
                                  fg_color='#ffff9c',
                                  text_color='black',
                                  font=('Sans-Serif', 30, 'bold'))
                hi.place(relx=0.5, rely=0.075, anchor=tkinter.CENTER)

#------------------------------------------------------------READY FRAME
class Ready2(ctk.CTkFrame):
        def __init__(self, parent, controller):
                super().__init__(parent)
                self.controller = controller

                label1 = ctk.CTkLabel(self,
                                      width = 800,
                                      height = 480,
                                      text = "It's time to take your medication",
                                      text_color = 'black',
                                      font = ('Sans-Serif', 35, 'bold'),
                                      fg_color = '#ffb9d5')
                label1.pack()

                button1 = ctk.CTkButton(self,
                                        text="Dispense Now",
                                        text_color='black',
                                        font = ('Sans-Serif', 20, 'bold'),
                                        width=300,
                                        height=75,
                                        fg_color='#ff78ae',
                                        border_width=5,
                                        border_color='red',
                                        hover_color='red',
                                        command=lambda: controller.show_frame(Dispense3))
                button1.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)
#-------------------------------------------------------------DISPENSE FRAME
class Dispense3(ctk.CTkFrame):
        def __init__(self,  parent, controller):
                super().init__(parent)
                self.controller = controller

                label2 = ctk.CTkLabel(self,
                                      width = 800,
                                      height = 500,
                                      text = "Dispensing...",
                                      text_color = 'black',
                                      font = ('Sans-Serif', 40, 'bold'),
                                      fg_color = '#ffb9d5')
                label2.pack()
            
                testbutton = ctk.CTkButton(self, text="test", command=lambda: controller.show_frame(Daysleft4))
                testbutton.place(relx=0.5, rely=0.65, anchor=tkinter.CENTER)
#-----------------------------------------------------------DAYS LEFT FRAME
class Daysleft4(ctk.CTkFrame):
        def __init__(self, parent, controller):
                super().__init__(parent)
                self.controller = controller

                label3 = ctk.CTkLabel(self,
                      width = 800,
                      height = 500,
                      text = "You have {days} day(s) of {evening_pills[index].Ename} left", #days = variable
                      text_color = 'black',
                      font = ('Sans-Serif', 35, 'bold'),
                      fg_color = '#ffb9d5')
                label3.pack()

                hello = ctk.CTkLabel(self,
                                width = 800,
                                height = 80,
                                text = "Hi, PillPal User",
                                fg_color = '#ffff9c',
                                text_color = 'black',
                                font = ('Sans-Serif', 30, 'bold'))
                hello.place(relx=0.5, rely=0.075, anchor=tkinter.CENTER)

                testbutton1 = ctk.CTkLabel(self, text="", command=lambda: controller.show_frame(Streak1))
                testbutton1.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)
            
app = MyApp()
app.mainloop()

