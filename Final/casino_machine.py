from dealerhand import DealerHand
import tkinter as tk #imports everything from tkinter
from tkinter import font as font
from credits import Credits
from PIL import ImageTk, Image
from deck import DeckOfCards
from pathlib import Path



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

button_font = ("Verdana", 40)


class CasinoApp(tk.Tk):
    """CasinoApp Class that provides GUI for the program."""

    def __init__(self, *args, **kwargs):

        self.machine_credits = Credits(100)

        tk.Tk.__init__(self, *args, **kwargs)
        main_frame = tk.Frame(self, bg="#280FE0", height=600, width=1024)
        main_frame.pack_propagate(0)
        main_frame.pack(fill="both", expand="true")
        main_frame.grid_rowconfigure(0, weight=1)
        main_frame.grid_columnconfigure(0, weight=1)
        self.resizable(0, 0) #prevents the app from being resized
        self.geometry("1366x768") #fixes the applications size
        #self.on_main_menu = False
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
        #self.main_frame.grid()
        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(0, weight=1)

        # #if(not controller.game_frames[GameOptionWidgets]):
        # if(controller.on_main_menu):

        #Credits Widget
        credits_frame = tk.LabelFrame(
            self, frame_styles, height=600, width=1024)
        credits_frame.place(relx=0, rely=1, anchor='sw')

        credits_frame.grid_rowconfigure(0, weight=1)
        credits_frame.grid_columnconfigure(0, weight=1)

        credits_text = tk.Label(credits_frame, text=f'Credits: {controller.machine_credits.balance}',
                                font=(button_font[1], 35), fg='yellow', bg=self.main_frame['bg'],
                                padx=20, pady=20, anchor='sw')

        cashout_button = tk.Button(credits_frame, text='Cashout', font=(button_font[1], 15),
                                   command=lambda: controller.machine_credits.deposit(
                                       100),
                                   padx=10, pady=5)

        add_credits_button = tk.Button(credits_frame, text='Add Credits', font=(button_font[1], 15),
                                       command=lambda: controller.machine_credits.deposit(
                                           100),
                                       padx=10, pady=5)

        cashout_button.grid(row=4, column=0, sticky='nw', ipadx=10)
        add_credits_button.grid(row=4, column=0, sticky='ne', ipadx=10)
        credits_text.grid(row=5, column=0, sticky='sw')

        # def get_credits_label(self):
        #     """Function to get the credits label."""
        #     return tk.Label(self.main_frame, text=f'Credits: {controller.machine_credits.balance}',
        #                             font=button_font, fg='yellow', bg=self.main_frame['bg'],
        #                             padx=20, pady=20, anchor='sw')
        


class GameOptionWidgets(GUI):
    """Class that controls GameOptionWidgets GUI"""
    def __init__(self, parent, controller):
        #GUI.__init__(self, parent)
        super().__init__(parent, controller)

        controller.on_main_menu = True

        # Game Option Menu
        option_frame = tk.LabelFrame(self, frame_styles, height=600, width=1024)
        option_frame.place(relx=.5, rely=.5, anchor='center')
        
        option_frame.grid_rowconfigure(0, weight=1)
        option_frame.grid_columnconfigure(0, weight=1)

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

        # #Credits Widget
        # credits_frame = tk.LabelFrame(self, frame_styles, height=600, width=1024)
        # credits_frame.place(relx=0, rely=1, anchor='sw')
        
        # credits_frame.grid_rowconfigure(0, weight=1)
        # credits_frame.grid_columnconfigure(0, weight=1)

        # credits_text = tk.Label(credits_frame, text=f'Credits: {controller.machine_credits.balance}', 
        #                             font=(button_font[1], 35), fg='yellow', bg=self.main_frame['bg'],
        #                             padx=20, pady=20, anchor='sw')

        # cashout_button = tk.Button(credits_frame, text='Cashout', font=(button_font[1], 15),
        #                                 command=lambda: controller.machine_credits.deposit(100),
        #                                 padx=10, pady=5)

        # add_credits_button = tk.Button(credits_frame, text='Add Credits', font=(button_font[1], 15),
        #                                 command=lambda: controller.machine_credits.deposit(100),
        #                                padx=10, pady=5)

        # cashout_button.grid(row=4, column=0, sticky='nw', ipadx=10)
        # add_credits_button.grid(row=4, column=0, sticky='ne', ipadx=10)
        # credits_text.grid(row=5, column=0, sticky='sw')


class CreditsWidget():
    def __init__(self, controller):


        credits_frame = tk.LabelFrame(self, frame_styles, height=600, width=1024)
        credits_frame.place(relx=0, rely=1, anchor='sw')

        credits_text = tk.Label(credits_frame, text=f'Credits: {controller.machine_credits.balance}',
                                    font=(button_font[1], 35), fg='yellow', bg=self.main_frame['bg'],
                                    padx=20, pady=20, anchor='sw')

        cashout_button = tk.Button(credits_frame, text='Cashout', font=(button_font[1], 15),
                                       command=lambda: controller.machine_credits.deposit(
                                           100),
                                       padx=10, pady=5)

        add_credits_button = tk.Button(credits_frame, text='Add Credits', font=(button_font[1], 15),
                                        command=lambda: controller.machine_credits.deposit(100),
                                       padx=10, pady=5)

        cashout_button.grid(row=4, column=0, sticky='nw', ipadx=10)
        add_credits_button.grid(row=4, column=0, sticky='ne', ipadx=10)
        credits_text.grid(row=5, column=0, sticky='sw')


class Blackjack(GUI):
    """Class that controls Blackjack GUI"""
    from deck import DeckOfCards
    from dealerhand import DealerHand
    from playerhand import PlayerHand

    player_hand = PlayerHand()
    dealer_hand = DealerHand()

    #deck = DeckOfCards()

    def __init__(self, parent, controller):
        #GUI().__init__(self, parent)
        super().__init__(parent, controller)
        global deck

        blackjack_frame = tk.Frame(self.main_frame, width=1000, height=600)
        #blackjack_frame.grid(row=0, column=0)
        blackjack_frame.place(anchor='center', relx=0.5, rely=0.5)

        canvas_width = 1000
        canvas_height = 700

        # canvas = tk.Canvas(self.main_frame,
        #         width=canvas_width,
        #         height=canvas_height,
        #         borderwidth=5)
        # canvas.grid(column=0, row=0)

        game_label = tk.Label(self.main_frame, text="Blackjack", font=button_font, anchor='n')
        #game_label.grid(row=0, column=0,sticky='n')
        game_label.place(anchor='n', relx=0.5, rely=0)

        back_button = tk.Button(self.main_frame, text='More Games', font=button_font,
                                command=lambda: controller.back_to_menu())
        back_button.grid(row=5, column=5, sticky='se')
        
        # Player Cards
        deck = DeckOfCards()

        deck.shuffle()
        first_player_card = deck.deal_card()
        #first_card = Image.open(
        #    f"D:/Pima/CIS 131/Final/card_images/2_of_clubs.png")
        first_card = Image.open(
            f"D:/Pima/CIS 131/Final/card_images/{first_player_card.image_name}.png")
        first_card = first_card.resize((int(first_card.width/4),int(first_card.height/4)))
        first_player_card_img = ImageTk.PhotoImage(first_card)
        # first_player_card_img = ImageTk.PhotoImage(Image.open(
        #     f"D:/Pima/CIS 131/Final/card_images/{first_player_card.image_name}.png"))
        print(first_card)

        #canvas.create_image(100, 100, image=first_player_card_img)

        player_cards_canvas = tk.Canvas(blackjack_frame)
        player_cards_canvas.place(anchor='n', relx=.5, rely=1)

        dealer_cards_canvas = tk.Canvas(blackjack_frame)
        dealer_cards_canvas.place(anchor='s', relx=.5, rely=0)



        first_player_card_lbl = tk.Label(player_cards_canvas, image=first_player_card_img, padx=20)
        first_player_card_lbl.image=first_player_card_img
        first_player_card_lbl.grid(row=0, column=0,sticky='w')
        #first_card_lbl.place(anchor='w', relx=0, rely=.5)

        second_player_card_lbl = tk.Label(player_cards_canvas, image=first_player_card_img, padx=20)
        second_player_card_lbl.image=first_player_card_img
        second_player_card_lbl.grid(row=0, column=1, sticky='w')
        #second_card_lbl.place(anchor='w', relx=0, rely=.5)
        thrid_player_card_lbl = tk.Label(
            player_cards_canvas, image=first_player_card_img, padx=20)
        thrid_player_card_lbl.image = first_player_card_img
        thrid_player_card_lbl.grid(row=0, column=2, sticky='w')

        # #Credits Widget
        # credits_frame = tk.LabelFrame(
        #     self, frame_styles, height=600, width=1024)
        # credits_frame.place(relx=0, rely=1, anchor='sw')

        # credits_frame.grid_rowconfigure(0, weight=1)
        # credits_frame.grid_columnconfigure(0, weight=1)

        # credits_text = tk.Label(credits_frame, text=f'Credits: {controller.machine_credits.balance}',
        #                         font=(button_font[1], 35), fg='yellow', bg=self.main_frame['bg'],
        #                         padx=20, pady=20, anchor='sw')

        # cashout_button = tk.Button(credits_frame, text='Cashout', font=(button_font[1], 15),
        #                            command=lambda: controller.machine_credits.deposit(
        #                                100),
        #                            padx=10, pady=5)

        # add_credits_button = tk.Button(credits_frame, text='Add Credits', font=(button_font[1], 15),
        #                                command=lambda: controller.machine_credits.deposit(
        #                                    100),
        #                                padx=10, pady=5)

        # cashout_button.grid(row=4, column=0, sticky='nw', ipadx=10)
        # add_credits_button.grid(row=4, column=0, sticky='ne', ipadx=10)
        # credits_text.grid(row=5, column=0, sticky='sw')

        #def 


    def deal_cards(players):
        """Function deals cards in sequence to player than dealer."""
        #players = [player_hand, dealer_hand]
        global deck

        num_cards_to_deal = len(players)

        #  loops to deal the correct amount of cards to players
        for count in range(num_cards_to_deal):
            for player in players:  # loop to deal a card to each player
                card = deck.deal_card()
                player.add_card(card)


class Video_Poker(GUI):
    """Class that controls Video Poker GUI"""
    def __init__(self, parent, controller):
        #GUI().__init__(self, parent)
        super().__init__(parent, controller)

        game_label = tk.Label(self.main_frame, text="Video Poker", font=("Verdana", 20), anchor='center')
        game_label.grid(row=0, column=0,sticky='n')

        back_button = tk.Button(self.main_frame, text='Main Menu', font=button_font,
                                command=lambda: controller.back_to_menu())
        back_button.grid(row=5, column=5)

        # #Credits Widget
        # credits_frame = tk.LabelFrame(
        #     self, frame_styles, height=600, width=1024)
        # credits_frame.place(relx=0, rely=1, anchor='sw')

        # credits_frame.grid_rowconfigure(0, weight=1)
        # credits_frame.grid_columnconfigure(0, weight=1)

        # credits_text = tk.Label(credits_frame, text=f'Credits: {controller.machine_credits.balance}',
        #                         font=(button_font[1], 35), fg='yellow', bg=self.main_frame['bg'],
        #                         padx=20, pady=20, anchor='sw')

        # cashout_button = tk.Button(credits_frame, text='Cashout', font=(button_font[1], 15),
        #                            command=lambda: controller.machine_credits.deposit(
        #                                100),
        #                            padx=10, pady=5)

        # add_credits_button = tk.Button(credits_frame, text='Add Credits', font=(button_font[1], 15),
        #                                command=lambda: controller.machine_credits.deposit(
        #                                    100),
        #                                padx=10, pady=5)

        # cashout_button.grid(row=4, column=0, sticky='nw', ipadx=10)
        # add_credits_button.grid(row=4, column=0, sticky='ne', ipadx=10)
        # credits_text.grid(row=5, column=0, sticky='sw')



class Craps(GUI):
    """Class that controls Craps GUI"""
    def __init__(self, parent, controller):
        #GUI().__init__(self, parent)
        super().__init__(parent, controller)

        game_label = tk.Label(self.main_frame, font=("Verdana", 20), text="Craps",
                            anchor='center')
        game_label.grid(row=0, column=0,sticky='n')

        back_button = tk.Button(self.main_frame, text='Main Menu', font=button_font,
                                command=lambda: controller.back_to_menu())
        back_button.grid(row=5, column=5)

        # #Credits Widget
        # credits_frame = tk.LabelFrame(
        #     self, frame_styles, height=600, width=1024)
        # credits_frame.place(relx=0, rely=1, anchor='sw')

        # credits_frame.grid_rowconfigure(0, weight=1)
        # credits_frame.grid_columnconfigure(0, weight=1)

        # credits_text = tk.Label(credits_frame, text=f'Credits: {controller.machine_credits.balance}',
        #                         font=(button_font[1], 35), fg='yellow', bg=self.main_frame['bg'],
        #                         padx=20, pady=20, anchor='sw')

        # cashout_button = tk.Button(credits_frame, text='Cashout', font=(button_font[1], 15),
        #                            command=lambda: controller.machine_credits.deposit(
        #                                100),
        #                            padx=10, pady=5)

        # add_credits_button = tk.Button(credits_frame, text='Add Credits', font=(button_font[1], 15),
        #                                command=lambda: controller.machine_credits.deposit(
        #                                    100),
        #                                padx=10, pady=5)

        # cashout_button.grid(row=4, column=0, sticky='nw', ipadx=10)
        # add_credits_button.grid(row=4, column=0, sticky='ne', ipadx=10)
        # credits_text.grid(row=5, column=0, sticky='sw')



root = CasinoApp() #builds a root widget
root.title('Virtual Casino Machine')

root.mainloop()
