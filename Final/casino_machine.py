import os
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

folder = os.path.realpath(os.path.dirname(__file__))
#call to get the path to eliminate need to hardcode path, fixes error when running code to different machines and needind different path.
file_path = os.path.dirname(os.path.abspath(__file__)) 

frame_styles = {"relief": "groove",
                "bd": 3, "bg": "#1C3AEC",
                "fg": "#280FE0", "font": ("Arial", 9, "bold")}

button_font = ("Verdana", 30)


class CasinoApp(tk.Tk):
    """CasinoApp Class that provides GUI for the program."""

    def __init__(self, *args, **kwargs):

        self.machine_credits = Credits(50)

        tk.Tk.__init__(self, *args, **kwargs)
        main_frame = tk.Frame(self, bg="#280FE0")  # creates a frame for the application
        main_frame.pack_propagate(0)
        main_frame.pack(fill="both", expand="true") # expands the frame fill the screen size
        main_frame.grid_rowconfigure(0, weight=1)
        main_frame.grid_columnconfigure(0, weight=1)
        self.resizable(0, 0) # prevents the app from being resized
        self.geometry("1366x768") # fixes the applications size
        self.game_frames = {} # dictionary that holds screens associated with each game 
        screens = (GameOptionWidgets, Blackjack, Video_Poker, Craps) # sets

        for screen in screens: #loop to display game buttons on the screen
            game_frame = screen(main_frame, self)
            self.game_frames[screen] = game_frame
            game_frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame(GameOptionWidgets) # call to open the main screen

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
        frame = self.game_frames[name] # retrives game frame from dictionary
        frame.credits_widget.update_credits_gui() # call to ensure credits gui gets updated from screen to screen
        frame.tkraise()

    # def back_to_menu(self):
    #     """Function to send game back to menu."""
    #     frame = self.game_frames[GameOptionWidgets] 
    #     frame.credits_widget.update_credits_gui() # call to ensure credits gui gets updated from screen to screen
    #     frame.tkraise()

        print(self.game_frames.keys())

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

        #Credits Widget
        self.credits_widget = CreditsWidget(self, controller)

        back_button = tk.Button(self.main_frame, text='More Games', font=button_font,
                                command=lambda: controller.show_frame(GameOptionWidgets))
        back_button.place(anchor='se',relx=1, rely=1)


class GameOptionWidgets(GUI):
    """Class that controls GameOptionWidgets GUI"""
    def __init__(self, parent, controller):
        #GUI.__init__(self, parent)
        super().__init__(parent, controller)

        #controller.on_main_menu = True

        # Game Option Menu
        option_frame = tk.LabelFrame(self, frame_styles, height=600, width=1024)
        option_frame.place(relx=.5, rely=.5, relwidth=.6, relheight=.6, anchor='center')

        option_frame.grid_rowconfigure(0, weight=0)
        option_frame.grid_columnconfigure(0, weight=0)

        blackjack_button = tk.Button(option_frame, text='Blackjack', 
                                    command=lambda: controller.show_frame(Blackjack), anchor='center')
        video_poker_button = tk.Button(option_frame, text='Video Poker', 
                                    command=lambda: controller.show_frame(Video_Poker), anchor='center')
        craps_button = tk.Button(option_frame, text='Craps', 
                                    command=lambda: controller.show_frame(Craps), anchor='center')

        blackjack_button.place(in_=option_frame,relx=.17, rely=.37, relwidth=.2, relheight=.3)
        video_poker_button.place(relx=.4, rely=.37, relwidth=.2, relheight=.3)
        craps_button.place(relx=.63, rely=.37, relwidth=.2, relheight=.3)


class BettingChipsWidget(GUI):
    """Class for player betting chips"""
    def __init__(self, parent, controller, game=None):
        super().__init__(parent, controller)

        self.game = game

        bet_btn_font = button_font

        betting_chips_canvas = tk.Canvas(game.blackjack_frame)
        betting_chips_canvas.place(anchor='s', relx=.5, rely=1)

        self.bet_1_button = tk.Button(betting_chips_canvas, text='1', font=bet_btn_font,
                                    width=4,
                                    command=lambda: self.increase_bet(1),
                                    state='normal')
                                    
        self.bet_5_button = tk.Button(betting_chips_canvas, text='5', font=bet_btn_font,
                                    width=4,
                                    command=lambda: self.increase_bet(5),
                                    state='normal')

        self.bet_10_button = tk.Button(betting_chips_canvas, text='10', font=bet_btn_font,
                                    width=4,
                                    command=lambda: self.increase_bet(10),
                                    state='normal')

        self.bet_25_button = tk.Button(betting_chips_canvas, text='25', font=bet_btn_font,
                                    width=4,
                                    command=lambda: self.increase_bet(25),
                                    state='normal')

        self.bet_100_button = tk.Button(betting_chips_canvas, text='100', font=bet_btn_font,
                                    width=4,
                                    command=lambda: self.increase_bet(100),
                                    state='normal')

        self.bet_buttons = (self.bet_1_button,self.bet_5_button,self.bet_10_button,self.bet_25_button,self.bet_100_button)

        self.bet_1_button.grid(row=0, column=0, sticky='w')
        self.bet_5_button.grid(row=0, column=1, sticky='w')
        self.bet_10_button.grid(row=0, column=2, sticky='w')
        self.bet_25_button.grid(row=0, column=3, sticky='w')
        self.bet_100_button.grid(row=0, column=4, sticky='w')

        
    def disable_bet_buttons(self):
        """Function to disable the bet buttons using a for loop"""
        for button in self.bet_buttons:
            button['state'] = 'disabled'

    
    def enable_bet_buttons(self):
        """Function to enable the bet buttons using for loop"""
        for button in self.bet_buttons:
            #if()
            if(int(button['text']) + self.game.current_bet <= int(self.credits_widget.credits.balance)):
                button['state'] = 'normal'
            else:
                button['state'] = 'disabled'


    def reset_bet(self):
        """Function to reset the betting amount and funtionality"""
        self.game.current_bet = 0
        self.game.update_current_bet_gui()
        self.enable_bet_buttons()


    def increase_bet(self, bet_amount):
        """Function to increase the bet when chips are clicked"""
        self.game.current_bet += bet_amount
        self.game.update_current_bet_gui()
        self.enable_bet_buttons()

        self.game.deal_button["state"] = 'normal'



class CreditsWidget(GUI):
    """Class to control the credits widget."""
    def __init__(self, parent, controller):

        self.credits = controller.machine_credits

        self.credits_frame = tk.LabelFrame(parent, frame_styles, height=600, width=1024)
        self.credits_frame.place(relx=0, rely=1, anchor='sw')

        self.credits_text = tk.Label(self.credits_frame, text=f'Credits: {controller.machine_credits.balance}',
                                    font=(button_font[1], 35), fg='yellow', bg=parent.main_frame['bg'],
                                    padx=20, pady=10, anchor='sw')

        self.add_credits_button = tk.Button(self.credits_frame, text='Add Credits', font=(button_font[1], 15),
                                        command=lambda: self.add_credits_gui(100),
                                       padx=10, pady=5)

        self.cashout_button = tk.Button(self.credits_frame, text='Cashout', font=(button_font[1], 15),
                                       command=lambda: self.cash_out_gui(),
                                       padx=10, pady=5)

        self.credits_text.grid(row=5, column=0, sticky='w')
        self.add_credits_button.grid(row=5, column=1, sticky='w')
        self.cashout_button.grid(row=5, column=2, sticky='w')

    def add_credits_gui(self, num):
        """Function to add credits to the machine"""
        self.credits.deposit(num)
        self.update_credits_gui()

    def remove_credits_gui(self, num):
        """Function to remove credits from current amount"""
        self.credits.withdraw(num)
        self.update_credits_gui()

    def cash_out_gui(self):
        """Function to control the cash out of machine credits"""
        self.credits.withdraw(self.credits.balance)
        self.update_credits_gui()

    def update_credits_gui(self):
        """Function to ensure credits gui matches machine credits."""
        self.credits_text.config(text=f'Credits: {self.credits.balance}')


class Blackjack(GUI):
    """Class that controls Blackjack GUI"""

    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        self.PLAY_GAME_MSG = '\nWould you like to play a hand of Black Jack? (y/n) '
        self.END_GAME_MSG = '\nThank you for playing Black Jack!\n'

        self.ENTER_BET_MSG = '\nHow much would you like to bet? (Enter 0 stop hand) '

        self.DEALER_WINS_STATUS = 'Dealer Wins.'
        self.DEALER_BLACKJACK = 'Dealer has blackjack.'
        self.DEALER_BUST = 'Dealer Bust!'

        self.PLAYER_WINS_STATUS = 'Player Wins!'
        self.PLAYER_BLACKJACK = 'Player has blackjack.'
        self.PLAYER_BUST = 'Player Bust...'
        self.PLAYER_STAND = 'Player stands.'

        self.BUST_STATUS = 'Bust...'
        self.PUSH_STATUS = 'Push...'
        self.CONTINUE_STATUS = 'Continue'

        self.BLACKJACK_MULTIPLIER = 1.5


        self.player_hand = PlayerHand()
        self.dealer_hand = DealerHand()
        self.deck_of_carks = DeckOfCards()

        self.players = [self.player_hand, self.dealer_hand]

        self.current_bet = 0

        self.player_status = self.CONTINUE_STATUS
        self.dealer_status = self.CONTINUE_STATUS

        #GUI Elements
        canvas_width = 1000
        canvas_height = 700

        self.blackjack_frame = tk.Frame(self.main_frame, width=1000, height=600)
        self.blackjack_frame.place(anchor='center', relx=0.5, rely=0.5)

        self.hand_canvas = self.create_hand_canvas()

        side_btn_font = (button_font[0], 15)
        bet_btn_font = (button_font[0], 20)

        game_lbl = tk.Label(self.main_frame, text="Blackjack", font=button_font)
        game_lbl.place(anchor='n', relx=0.5, rely=0)

        self.winner_frame = tk.Frame(self.blackjack_frame)
        self.winner_frame.place(anchor='center', relx=.5, rely=.3)
        self.winner_lbl = tk.Label(self.blackjack_frame, text='Winner', font=button_font)
        self.winner_lbl.place(anchor='n', relx=.5, rely=.25)

        #Game Decision Buttons

        self.hit_button = tk.Button(self.blackjack_frame, text='Hit', font=side_btn_font,
                                    bg='green',
                                    command=lambda: self.hit(self.player_hand),
                                    state='disabled')
        self.hit_button.place(anchor='ne', relx=1, rely=.73, relwidth=.13)

        self.stand_button = tk.Button(self.blackjack_frame, text='Stand', font=side_btn_font,
                                    bg='red',
                                    command=lambda: self.stand(),
                                    state='disabled')
        self.stand_button.place(anchor='ne', relx=1, rely=.8, relwidth=.13)

        self.deal_button = tk.Button(self.blackjack_frame, text='Deal Hand', font=side_btn_font,
                                    command=lambda: self.play_blackljack_hand(),
                                    state='disabled')
        self.deal_button.place(anchor='ne', relx=1, rely=.87, relwidth=.13)

        #Betting Chips GUI 
        self.betting_chips_gui = BettingChipsWidget(parent, controller, self)

        #Current Bet GUI
        current_bet_canvas = tk.Canvas(self.blackjack_frame,height=100, width=200)
        current_bet_canvas.place(anchor='center', relx=.5, rely=.5)

        current_bet_lbl = tk.Label(current_bet_canvas, text='Current Bet', font=bet_btn_font)
        current_bet_lbl.place(anchor='s', relx=.5, rely=.63)

        self.current_bet_amount_lbl = tk.Label(current_bet_canvas, text=str(self.current_bet), font=bet_btn_font)
        self.current_bet_amount_lbl.place(anchor='n', relx=.5, rely=.68)
        
        # Start Of Gameplay

    
    def reset_game(self):
        """Function to reset the game to default status"""
        self.clear_hand_gui()
        self.hand_canvas = self.create_hand_canvas()

        self.hit_button['state'] = 'disabled'
        self.stand_button['state'] = 'disabled'
        self.deal_button['state'] = 'disabled'

        self.betting_chips_gui.enable_bet_buttons()

        self.player_hand.set_hand([])
        self.dealer_hand.set_hand([])

        self.update_current_bet_gui()


    def play_blackljack_hand(self):
        """Function to control the gameplay of a blackjack hand."""
        self.start_new_hand()


    def start_new_hand(self):
        """Function to start a new hand of blackjack."""
        self.winner_lbl.place_forget()

        self.clear_hand_gui()
        self.hand_canvas = self.create_hand_canvas()

        self.enable_hit_stand_btns()
        
        self.deal_button['state'] = 'disabled'

        self.betting_chips_gui.disable_bet_buttons()

        self.player_hand.set_hand([])
        self.dealer_hand.set_hand([])
        self.dealer_hand.show_hand = False
        
        self.deal_cards()
        self.determine_blackjack()


    def deal_cards(self):
        """Function deals cards in sequence to player than dealer."""
        num_cards_to_deal = len(self.players)
        self.deck_of_carks.shuffle()

        # loops to deal the correct amount of cards to players
        for count in range(num_cards_to_deal):
            for player in self.players:  # loop to deal a card to each player
                self.hit(player)


    def hit(self, hand):
        """Function to add card to hand."""
        card_to_add = self.deck_of_carks.deal_card()
        hand.add_card(card_to_add)

        self.update_hand_gui()

        if(self.determine_hand_bust(self.player_hand)):
            self.hit_button['state'] = 'disabled'
    

    def stand(self):
        """Function to control the stand decision of the player."""
        self.disable_hit_stand_btns()

        self.play_dealer_hand()


    def play_dealer_hand(self):
        """Funtion to control the dealer gameplay."""
        hand_value = self.dealer_hand.determine_hand_value()

        if(hand_value < 17):
            self.hit(self.dealer_hand)

            self.play_dealer_hand()

        self.process_winner()

    
    def determine_blackjack(self):
        """Determines if players have natural blackjack."""
        if(self.player_hand.determine_hand_value() == 21 or self.dealer_hand.determine_hand_value() == 21):
            self.process_winner()


    def process_winner(self):
        """Function to contol the end of a hand and determine the winner"""
        winner = self.determine_winner()
        self.dealer_hand.show_hand = True

        self.update_hand_gui()

        self.winner_lbl.config(text=winner) 
        self.winner_lbl.place(anchor='n', relx=.5, rely=.25)

        self.disable_hit_stand_btns()

        self.determine_payout(winner)
        self.betting_chips_gui.reset_bet()


    def determine_winner(self):
        """Function to determine the winner and return winnning status"""
        if (self.determine_hand_bust(self.player_hand) and self.determine_hand_bust(self.dealer_hand)):
            return (self.PUSH_STATUS)
        
        if(self.determine_hand_bust(self.dealer_hand)):
            return (self.PLAYER_WINS_STATUS)

        if(self.determine_hand_bust(self.player_hand)):
            return (self.DEALER_WINS_STATUS)

        if (self.player_hand.determine_hand_value() == self.dealer_hand.determine_hand_value()):
            return (self.PUSH_STATUS)

        if (self.dealer_hand.determine_hand_value() > self.player_hand.determine_hand_value()):
            return (self.DEALER_WINS_STATUS)

        if (self.dealer_hand.determine_hand_value() < self.player_hand.determine_hand_value()):
            return (self.PLAYER_WINS_STATUS)


    def determine_payout(self, winner):
        """Function to payout the player."""
        if(winner == self.PLAYER_WINS_STATUS):
            if(self.player_hand.determine_hand_value() == 21 and len(self.player_hand.hand) <= 2):
                self.credits_widget.add_credits_gui(self.current_bet * self.BLACKJACK_MULTIPLIER)
                return

            self.credits_widget.add_credits_gui(self.current_bet)
            return

        if(winner == self.DEALER_WINS_STATUS):
            self.credits_widget.remove_credits_gui(self.current_bet)
            return

        if(winner == self.PUSH_STATUS):
            return


    def determine_hand_bust(self, hand):
        """Function to determine if the hand bust or not"""
        if hand.determine_hand_value() > 21:
            return True

        return False


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
    

    def update_hand_gui(self):
        """Function to update the hand GUI"""

        for hands in self.players:
            for card in hands.hand:
                if(not hands.show_hand and hands.hand.index(card) == 0):
                    player_card = Image.open(card.back_image)
                else:
                    player_card = Image.open(card.image_path)

                player_card = player_card.resize((int(player_card.width/4), int(player_card.height/4)))
                card_img = ImageTk.PhotoImage(player_card)

                card_lbl = tk.Label(self.hand_canvas[self.players.index(hands)], image=card_img, padx=20)
                card_lbl.image = card_img
                card_lbl.grid(row=0, column=hands.hand.index(card), sticky='w')

        
    def update_current_bet_gui(self):
        """Function to control the current bet GUI to ensure it shows proper amount."""
        self.current_bet_amount_lbl.config(text=str(self.current_bet))

    
    def enable_hit_stand_btns(self):
        """Function to enable the hit and stand buttons"""
        self.hit_button['state'] = 'normal'
        self.stand_button['state'] = 'normal'


    def disable_hit_stand_btns(self):
        """Function to enable the hit and stand buttons"""
        self.hit_button['state'] = 'disabled'
        self.stand_button['state'] = 'disabled'


class Video_Poker(GUI):
    """Class that controls Video Poker GUI"""
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        game_label = tk.Label(self.main_frame, text="Video Poker", font=("Verdana", 20), anchor='center')
        game_label.grid(row=0, column=0,sticky='n')


class Craps(GUI):
    """Class that controls Craps GUI"""
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        game_label = tk.Label(self.main_frame, font=("Verdana", 20), text="Craps",
                            anchor='center')
        game_label.grid(row=0, column=0,sticky='n')


root = CasinoApp() #builds a root widget
root.title('Virtual Casino Machine')

root.mainloop()
