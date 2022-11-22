import tkinter as tk #imports everything from tkinter
from tkinter import font as font



# e = Entry(root, width=35, borderwidth=5)
# e.grid(row=0, column=0, columnspan=4, padx=10,pady=10)

# button_font = font.Font(family='Helvitica', size=20)
# button_quit = Button(root, text="Exit",
#                             bg='red',
#                             fg='white',
#                             bd=0,
#                             font=button_font,
#                             command=root.quit, width=5, height=1, anchor=SE)
# button_quit.grid(row=5, column=5, padx=10,pady=10)


frame_styles = {"relief": "groove",
                "bd": 3, "bg": "#1C3AEC",
                "fg": "#280FE0", "font": ("Arial", 9, "bold")}


class CasinoApp(tk.Tk):
    """CasinoApp Class that provides GUI for the program."""

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        main_frame = tk.Frame(self, bg="#280FE0", height=600, width=1024)
        main_frame.pack_propagate(0)
        main_frame.pack(fill="both", expand="true")
        main_frame.grid_rowconfigure(0, weight=1)
        main_frame.grid_columnconfigure(0, weight=1)
        self.resizable(0, 0) #prevents the app from being resized
        self.geometry("1366x768") #fixes the applications size
        self.on_main_menu = False
        self.game_frames = {}
        games = (GameOptionWidgets, Blackjack, Video_Poker, Craps)

    

        for game in games: #loop to display game buttons on the screen
            game_frame = game(main_frame, self)
            self.game_frames[game] = game_frame
            game_frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame(GameOptionWidgets)

        tk.Tk.config(self)        
        
        # pages = (Some_Widgets, PageOne, PageTwo, PageThree, PageFour)
        # for F in pages:
        #     frame = F(main_frame, self)
        #     self.frames[F] = frame
        #     frame.grid(row=0, column=0, sticky="nsew")
        # #self.show_frame(Some_Widgets)
        # menubar = MenuBar(self)
        #tk.Tk.config(self, menu=menubar)


    def show_frame(self, name):
        # frame = self.game_frames[name]
        # frame.tkraise()
        #self.game_frames.configure(state='disabled')
        frame = self.game_frames[name]
        frame.tkraise()

    def back_to_menu(self):
        """Function to send game back to menu."""
        frame = self.game_frames[GameOptionWidgets]
        frame.tkraise()

    #cashout player - cash player out, quit game.

    def OpenNewWindow(self):
        pass
        #OpenNewWindow()

    def Quit_application(self):
        self.destroy()


class GUI(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.main_frame = tk.Frame(self, bg="#1C3AEC", height=600, width=1024)
        #self.main_frame.pack_propagate(0)
        self.main_frame.pack(fill="both", expand="true")
        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(0, weight=1)

        self.button_font =("Verdana", 20)

        # #if(not controller.game_frames[GameOptionWidgets]):
        # if(controller.on_main_menu):
        


class GameOptionWidgets(GUI):
    """Class that controls GameOptionWidgets GUI"""
    def __init__(self, parent, controller):
        #GUI.__init__(self, parent)
        super().__init__(parent, controller)

        controller.on_main_menu = True

        option_frame = tk.LabelFrame(self, frame_styles, height=600, width=1024)
        option_frame.place(relx=self.main_frame.winfo_width()/2, rely=self.main_frame.winfo_height()/2, anchor='center')
        
        option_frame.grid_rowconfigure(0, weight=1)
        option_frame.grid_columnconfigure(0, weight=1)

        #option_frame.place(relx=self.main_frame.winfo_height() / 4, rely=self.main_frame.winfo_width() / 2)

        #button_quit = Button(root, text="Exit", command=root.quit) 
        blackjack_button = tk.Button(option_frame, text='Blackjack', 
                                    command=lambda: controller.show_frame(Blackjack),
                                    padx=40, pady=20)
        video_poker_button = tk.Button(option_frame, text='Video Poker', 
                                    command=lambda: controller.show_frame(Video_Poker),
                                    padx=40, pady=20)
        craps_button = tk.Button(option_frame, text='Craps', 
                                    command=lambda: controller.show_frame(Craps),
                                    padx=40, pady=20)

        blackjack_button.grid(row=0, column=0, padx=20, pady=20)
        video_poker_button.grid(row=0, column=2, padx=20, pady=20)
        craps_button.grid(row=0, column=4, padx=20, pady=20)


class Blackjack(GUI):
    """Class that controls Blackjack GUI"""
    def __init__(self, parent, controller):
        #GUI().__init__(self, parent)
        super().__init__(parent, controller)

        game_label = tk.Label(self.main_frame, text="Blackjack", font=self.button_font, anchor='center')
        game_label.grid(row=0, column=0,sticky='n')

        back_button = tk.Button(self.main_frame, text='Main Menu', font=self.button_font,
                                command=lambda: controller.back_to_menu())
        back_button.grid(row=5, column=5)



class Video_Poker(GUI):
    """Class that controls Video Poker GUI"""
    def __init__(self, parent, controller):
        #GUI().__init__(self, parent)
        super().__init__(parent, controller)

        game_label = tk.Label(self.main_frame, text="Video Poker", font=("Verdana", 20), anchor='center')
        game_label.grid(row=0, column=0,sticky='n')

        back_button = tk.Button(self.main_frame, text='Main Menu', font=self.button_font,
                                command=lambda: controller.back_to_menu())
        back_button.grid(row=5, column=5)



class Craps(GUI):
    """Class that controls Craps GUI"""
    def __init__(self, parent, controller):
        #GUI().__init__(self, parent)
        super().__init__(parent, controller)

        game_label = tk.Label(self.main_frame, font=("Verdana", 20), text="Craps", anchor='center')
        game_label.grid(row=0, column=0,sticky='n')

        back_button = tk.Button(self.main_frame, text='Main Menu', font=self.button_font,
                                command=lambda: controller.back_to_menu())
        back_button.grid(row=5, column=5)



root = CasinoApp() #builds a root widget
root.title('Virtual Casino Machine')


root.mainloop()
