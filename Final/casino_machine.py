from dealerhand import DealerHand
import tkinter as tk #imports everything from tkinter
from tkinter import font as font
from credits import Credits
from PIL import ImageTk, Image
from deck import DeckOfCards
from pathlib import Path

from deck import DeckOfCards
from dealerhand import DealerHand
from playerhand import PlayerHand



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

button_font = ("Verdana", 30)


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
        """Function that calls the frame of the game."""
        # frame = self.game_frames[name]
        # frame.tkraise()
        #self.game_frames.configure(state='disabled')
        frame = self.game_frames[name]
        frame.update_credits_gui()
        frame.tkraise()

    def back_to_menu(self):
        """Function to send game back to menu."""
        frame = self.game_frames[GameOptionWidgets]
        frame.update_credits_gui()
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
        self.credits = controller.machine_credits

        credits_frame = tk.LabelFrame(
            self, frame_styles)
        credits_frame.place(relx=0, rely=1, anchor='sw')

        credits_frame.grid_rowconfigure(0, weight=1)
        credits_frame.grid_columnconfigure(0, weight=1)

        self.credits_text = tk.Label(credits_frame, text=f'Credits: {self.credits.balance}',
                                font=(button_font[1], 35), fg='yellow', bg=self.main_frame['bg'],
                                padx=20, pady=10, anchor='sw')

        cashout_button = tk.Button(credits_frame, text='Cash\nOut', font=(button_font[0], 15),
                                   command=lambda: controller.machine_credits.deposit(
                                       100),
                                   padx=10, pady=5)

        add_credits_button = tk.Button(credits_frame, text='Add\nCredits', font=(button_font[0], 15),
                                       command=lambda: self.add_credits_gui(100),
                                       padx=10, pady=5)

        cashout_button.grid(row=5, column=2, sticky='w', ipadx=10)
        add_credits_button.grid(row=5, column=1, sticky='w', ipadx=10)
        self.credits_text.grid(row=5, column=0, sticky='w')

        # def get_credits_label(self):
        #     """Function to get the credits label."""
        #     return tk.Label(self.main_frame, text=f'Credits: {controller.machine_credits.balance}',
        #                             font=button_font, fg='yellow', bg=self.main_frame['bg'],
        #                             padx=20, pady=20, anchor='sw')


    def add_credits_gui(self, num):
        """Function to add credits to the machine"""
        self.credits.deposit(num)
        self.update_credits_gui()

    def update_credits_gui(self):
        """Function to ensure credits gui matches machine credits."""
        self.credits_text.config(text=f'Credits: {self.credits.balance}')


class GameOptionWidgets(GUI):
    """Class that controls GameOptionWidgets GUI"""
    def __init__(self, parent, controller):
        #GUI.__init__(self, parent)
        super().__init__(parent, controller)

        #controller.on_main_menu = True

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
        video_poker_button.grid(row=0, column=1, padx=20, pady=20)
        craps_button.grid(row=0, column=2, padx=20, pady=20)

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

    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        self.player_hand = PlayerHand()
        self.dealer_hand = DealerHand()
        self.deck_of_carks = DeckOfCards()

        self.players = [self.player_hand, self.dealer_hand]

        #GUI Elements
        canvas_width = 1000
        canvas_height = 700

        self.blackjack_frame = tk.Frame(self.main_frame, width=1000, height=600)
        self.blackjack_frame.place(anchor='center', relx=0.5, rely=0.5)

        self.hand_canvas = self.create_hand_canvas()

        side_btn_font = (button_font[0], 15)

        game_label = tk.Label(self.main_frame, text="Blackjack", font=button_font, anchor='n')
        game_label.place(anchor='n', relx=0.5, rely=0)

        self.hit_button = tk.Button(self.blackjack_frame, text='Hit', font=side_btn_font,
                               bg='green',
                               command=lambda: self.hit(self.player_hand),
                               state='disabled')
        self.hit_button.place(anchor='ne', relx=1, rely=.73)

        self.stand_button = tk.Button(self.blackjack_frame, text='Stand', font=side_btn_font,
                               bg='red',
                               command=lambda: self.stand(),
                               state='disabled')
        self.stand_button.place(anchor='ne', relx=1, rely=.8)

        self.deal_button = tk.Button(self.blackjack_frame, text='Deal Hand', font=side_btn_font,
                               command=lambda: self.start_new_hand(),
                                state='normal')
        self.deal_button.place(anchor='ne', relx=1, rely=.87)

        back_button = tk.Button(self.main_frame, text='More Games', font=button_font,
                                command=lambda: controller.back_to_menu())
        back_button.place(anchor='se',relx=1, rely=1)
        
        # Start Of Gameplay
        #self.start_new_hand()
        #self.deal_cards()

        # first_player_card = self.deck_of_carks.deal_card()
        # #first_card = Image.open(
        # #    f"D:/Pima/CIS 131/Final/card_images/2_of_clubs.png")
        # first_card = Image.open(
        #     f"D:/Pima/CIS 131/Final/card_images/{first_player_card.image_name}.png")
        # first_card = first_card.resize((int(first_card.width/4),int(first_card.height/4)))
        # first_player_card_img = ImageTk.PhotoImage(first_card)
        # first_player_card_img = ImageTk.PhotoImage(Image.open(
        #     f"D:/Pima/CIS 131/Final/card_images/{first_player_card.image_name}.png"))
        #print(first_card)

        #canvas.create_image(100, 100, image=first_player_card_img)

        #player_card_lbls

        # first_player_card_lbl = tk.Label(player_cards_canvas, image=first_player_card_img, padx=20)
        # first_player_card_lbl.image=first_player_card_img
        # first_player_card_lbl.grid(row=0, column=0,sticky='w')
        # #first_card_lbl.place(anchor='w', relx=0, rely=.5)

        # second_player_card_lbl = tk.Label(player_cards_canvas, image=first_player_card_img, padx=20)
        # second_player_card_lbl.image=first_player_card_img
        # second_player_card_lbl.grid(row=0, column=1, sticky='w')
        # #second_card_lbl.place(anchor='w', relx=0, rely=.5)
        # thrid_player_card_lbl = tk.Label(
        #     player_cards_canvas, image=first_player_card_img, padx=20)
        # thrid_player_card_lbl.image = first_player_card_img
        # thrid_player_card_lbl.grid(row=0, column=2, sticky='w')

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

        # def 


    def start_new_hand(self):
        """Function to start a new hand of blackjack."""
        self.clear_hand_gui()
        self.hand_canvas = self.create_hand_canvas()

        self.hit_button['state'] = 'normal'
        self.stand_button['state'] = 'normal'

        self.player_hand.set_hand([])
        self.dealer_hand.set_hand([])

        self.deck_of_carks.shuffle()

        self.deal_cards()


    def deal_cards(self):
        """Function deals cards in sequence to player than dealer."""
        num_cards_to_deal = len(self.players)

        # loops to deal the correct amount of cards to players
        for count in range(num_cards_to_deal):
            for player in self.players:  # loop to deal a card to each player
                self.hit(player)


    def hit(self, hand):
        """Function to add card to hand."""
        card_to_add = self.deck_of_carks.deal_card()
        hand.add_card(card_to_add)

        self.update_hand_gui(hand, card_to_add)

        if(hand.determine_hand_value() >= 21):
            self.hit_button['state'] = 'disabled'
            self.stand_button['state'] = 'disabled'
    

    def stand(self):
        """Function to control the stand decision of the player."""
        pass

    
    def update_hand_gui(self, hand, card):
        """Function to update the hand GUI"""

        player_card = Image.open(
            f"D:/Pima/CIS 131/Final/card_images/{card.image_name}.png")
        player_card = player_card.resize(
            (int(player_card.width/4), int(player_card.height/4)))
        card_img = ImageTk.PhotoImage(player_card)

        card_lbl = tk.Label(self.hand_canvas[self.players.index(hand)], image=card_img, padx=20)
        card_lbl.image = card_img
        card_lbl.grid(row=0, column=len(hand.hand)-1, sticky='w')


    def clear_hand_gui(self):
        """Function to clear the hand gui"""
        for hand in self.hand_canvas:
            hand.destroy()


    def create_hand_canvas(self):
        """Function to create new hand canvas gui"""
        player_cards_canvas = tk.Canvas(self.blackjack_frame)
        player_cards_canvas.place(anchor='s', relx=.5, rely=.85)

        dealer_cards_canvas = tk.Canvas(self.blackjack_frame)
        dealer_cards_canvas.place(anchor='n', relx=.5, rely=0)

        return (player_cards_canvas, dealer_cards_canvas)


class Video_Poker(GUI):
    """Class that controls Video Poker GUI"""
    def __init__(self, parent, controller):
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
        super().__init__(parent, controller)

        game_label = tk.Label(self.main_frame, font=("Verdana", 20), text="Craps",
                            anchor='center')
        game_label.grid(row=0, column=0,sticky='n')

        back_button = tk.Button(self.main_frame, text='Main Menu', font=button_font,
                                command=lambda: controller.back_to_menu())
        back_button.grid(row=5, column=5)

        # Credits Widget
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
