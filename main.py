from tkinter import *


def main():
    root = Tk()

    class TicTakToe:

        def __init__(self, root):
            self.root = root
            self.root.title("TicTakToe")
            self.root.resizable(False, False)
            self.root.geometry("900x600")
            self._9button = IntVar
            self.player_term = "X"
            self.b = {}
            self.taken_squaresX_row = []
            self.taken_squaresX_column = []
            self.taken_squaresO_row = []
            self.taken_squaresO_column = []

            button_label = LabelFrame(self.root)
            button_label.place(x=150, y=100, relwidth=0.64, relheight=0.66)
            self.b[1] = Button(button_label, text=" ", font=("comicsans", 50), command=lambda: self.change_val(1),height=2, width= 5)
            self.b[2] = Button(button_label, text=" ", font=("comicsans", 50), command=lambda: self.change_val(2),height=2, width= 5)
            self.b[3] = Button(button_label, text=" ", font=("comicsans", 50), command=lambda: self.change_val(3),height=2, width= 5)
            self.b[4] = Button(button_label, text=" ", font=("comicsans", 50), command=lambda: self.change_val(4),height=2, width= 5)
            self.b[5] = Button(button_label, text=" ", font=("comicsans", 50), command=lambda: self.change_val(5),height=2, width= 5)
            self.b[6] = Button(button_label, text=" ", font=("comicsans", 50), command=lambda: self.change_val(6),height=2, width= 5)
            self.b[7] = Button(button_label, text=" ", font=("comicsans", 50), command=lambda: self.change_val(7),height=2, width= 5)
            self.b[8] = Button(button_label, text=" ", font=("comicsans", 50), command=lambda: self.change_val(8),height=2, width= 5)
            self.b[9] = Button(button_label, text=" ", font=("comicsans", 50), command=lambda: self.change_val(9),height=2, width= 5)

            self.b[1].grid(row=0, column=0)
            self.b[2].grid(row=0, column=1)
            self.b[3].grid(row=0, column=2)
            self.b[4].grid(row=1, column=0)
            self.b[5].grid(row=1, column=1)
            self.b[6].grid(row=1, column=2)
            self.b[7].grid(row=2, column=0)
            self.b[8].grid(row=2, column=1)
            self.b[9].grid(row=2, column=2)

            player_label = LabelFrame(self.root)
            player_label.place(x=50, y=5, relwidth=0.9, relheight=0.15)
            self.current_player = Label(player_label, text=" Current player:", font=("comicsans", 56))
            self.current_player.place(relx=0.1,rely=0.05)
            self.x_or_0 = Label(player_label, text=self.player_term, font=("comiscans", 63))
            self.x_or_0.place(relx=0.6, rely=0.05)
            self.restart_button = Button(self.root, text="Restart", height=3, width=4, command=self.restart)
            self.restart_button.place(relx=0.85, rely=0.85)
            self.pinus_label = Label(self.root, text=" ",font=("comicsans",35))
            self.pinus_label.place(relx=0.4, rely=0.85)

        def restart(self):
            self.b[1].configure(text=" ")
            self.b[2].configure(text=" ")
            self.b[3].configure(text=" ")
            self.b[4].configure(text=" ")
            self.b[5].configure(text=" ")
            self.b[6].configure(text=" ")
            self.b[7].configure(text=" ")
            self.b[8].configure(text=" ")
            self.b[9].configure(text=" ")
            self.player_term = "X"
            self.x_or_0.configure(text=self.player_term)
            self.current_player.configure(text=" Current player:")
            self.x_or_0.place(relx=0.6, rely=0.05)


        def change_button(self, butt):
            if self.player_term == "X":
                self.b[butt].configure(text="X")
            elif self.player_term == "0":
                self.b[butt].configure(text="0")

        def check_for_winner(self, curr_row, curr_column, player_symb):
            if player_symb == "X":
                self.taken_squaresX_row.append(curr_row)
                self.taken_squaresX_column.append(curr_column)
                try:
                    if self.b[1].cget("text") == "X" and self.b[4].cget("text") == "X" and self.b[7].cget("text") == "X" or self.b[2].cget("text") == "X" and self.b[5].cget("text") == "X" and self.b[8].cget("text") \
                            == "X" or self.b[3].cget("text") == "X" and self.b[6].cget("text") == "X" and self.b[9].cget("text") == "X":
                        self.current_player.configure(text="")
                        self.x_or_0.configure(text="Player 'X' Wins!")
                        self.x_or_0.place(relx=0.23, rely=0.05)
                    elif self.b[1].cget("text") == "X" and self.b[2].cget("text") == "X" and self.b[3].cget("text") == "X" or self.b[4].cget("text") == "X" and self.b[5].cget("text") == "X" and self.b[6].cget("text") \
                            == "X" or self.b[7].cget("text") == "X" and self.b[8].cget("text") == "X" and self.b[9].cget("text") == "X":
                        self.current_player.configure(text="")
                        self.x_or_0.configure(text="Player 'X' Wins!")
                        self.x_or_0.place(relx=0.23, rely=0.05)
                    elif self.b[7].cget("text") == "X" and self.b[5].cget("text") == "X" and self.b[3].cget("text") == "X" or self.b[3].cget("text") == "X" and self.b[5].cget("text") == "X" and self.b[7].cget("text") == "X":
                        self.current_player.configure(text="")
                        self.x_or_0.configure(text="Player 'X' Wins!")
                        self.x_or_0.place(relx=0.23, rely=0.05)
                    elif self.b[2].cget("text") == "X" and self.b[7].cget("text") == "X" and self.b[9].cget("text") == "X" and self.b[5].cget("text") == "0" and self.b[8].cget("text") == "0":
                        self.pinus_label.configure(text="PINUS!!!!!!!")


                except IndexError:
                    pass
            elif player_symb == "O":
                self.taken_squaresO_row.append(curr_row)
                self.taken_squaresO_column.append(curr_column)
                try:
                    if self.b[1].cget("text") == "0" and self.b[4].cget("text") == "0" and self.b[7].cget("text") == "0" or self.b[2].cget("text") == "0" and self.b[5].cget("text") == "0" and self.b[8].cget("text") \
                            == "0" or self.b[3].cget("text") == "0" and self.b[6].cget("text") == "0" and self.b[9].cget("text") == "0":
                        self.current_player.configure(text="")
                        self.x_or_0.configure(text="Player '0' Wins!")
                        self.x_or_0.place(relx=0.23, rely=0.05)
                    elif self.b[1].cget("text") == "0" and self.b[2].cget("text") == "0" and self.b[3].cget("text") == "0" or self.b[4].cget("text") == "0" and self.b[5].cget("text") == "0" and self.b[6].cget("text") \
                            == "0" or self.b[7].cget("text") == "0" and self.b[8].cget("text") == "0" and self.b[9].cget("text") == "0":
                        self.current_player.configure(text="")
                        self.x_or_0.configure(text="Player '0' Wins!")
                        self.x_or_0.place(relx=0.23, rely=0.05)
                    elif self.b[7].cget("text") == "0" and self.b[5].cget("text") == "0" and self.b[3].cget("text") == "0" or self.b[3].cget("text") == "0" and self.b[5].cget("text") == "0" and self.b[7].cget("text") == "0":
                        self.current_player.configure(text="")
                        self.x_or_0.configure(text="Player '0' Wins!")
                        self.x_or_0.place(relx=0.23, rely=0.05)
                except IndexError:
                    pass

        def change_val(self, butt):
            if self.b[butt].cget("text") != " ":
                print("This button is already used")
                return None
            elif self.current_player.cget("text") == "":
                print("Game over!")
                return None
            else:
                self.change_button(butt)
                if self.player_term == "X":
                    self.player_term = "0"
                    self.x_or_0.configure(text=self.player_term)
                    coord = self.b[butt].grid_info()
                    self.check_for_winner(coord["row"], coord["column"], "X")
                elif self.player_term == "0":
                    self.player_term = "X"
                    self.x_or_0.configure(text=self.player_term)
                    coord = self.b[butt].grid_info()
                    self.check_for_winner(coord["row"], coord["column"], "O")

    TicTakToe(root)
    root.mainloop()


if __name__ == '__main__':
    main()
