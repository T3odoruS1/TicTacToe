from tkinter import *

def main():
    root = Tk()

    class TicTakToe:

        def __init__(self, root):
            self.root = root
            self.root.title("TicTakToe")
            self.root.geometry("900x600")
            self._9button = IntVar


            button_label = LabelFrame(self.root)
            button_label.place(x=100, y=100, relwidth=0.75, relheight= 0.7)
            self.up_left_bt = Button(button_label, text=" ",font=("comicsans",50), command=self.change_player)
            self.up_cent_bt = Button(button_label, text=" ",font=("comicsans",50))
            self.up_right_bt = Button(button_label, text=" ",font=("comicsans",50))
            self.cent_left_bt = Button(button_label, text=" ",font=("comicsans",50))
            self.cent_cent_bt = Button(button_label, text=" ",font=("comicsans",50))
            self.cent_right_bt = Button(button_label, text=" ",font=("comicsans",50))
            self.down_left_bt = Button(button_label, text=" ",font=("comicsans",50))
            self.down_cent_bt = Button(button_label, text=" ",font=("comicsans",50))
            self.down_right_bt = Button(button_label, text=" ",font=("comicsans",50))

            self.up_left_bt.grid(row=0, column=0, padx=75, pady=20)
            self.up_cent_bt.grid(row=0, column=1, padx=100, pady=20)
            self.up_right_bt.grid(row=0, column=2, padx=100, pady=20)
            self.cent_left_bt.grid(row=1, column=0, padx=75, pady=50)
            self.cent_cent_bt.grid(row=1, column=1, padx=100, pady=50)
            self.cent_right_bt.grid(row=1, column=2, padx=100, pady=50)
            self.down_left_bt.grid(row=2, column=0, padx=75, pady=50)
            self.down_cent_bt.grid(row=2, column=1, padx=100, pady=50)
            self.down_right_bt.grid(row=2, column=2, padx=100, pady=50)

            player_label = LabelFrame(self.root)
            player_label.place(x=50, y=5, relwidth=0.9, relheight=0.15)
            self.current_player = Label(player_label, text=" Current player:", font=("comicsans",32))
            self.current_player.grid(row=0, column=0, padx=150)
            self.x_or_0 = Label(player_label, text="X", font=("comiscans",56))
            self.x_or_0.grid(row=0, column=1)

        def change_player(self):

            if self.x_or_0.cget("text") == "X":
                self.x_or_0.configure(text="0")
            else:
                self.x_or_0.configure(text="X")



    TicTakToe(root)
    root.mainloop()






if __name__ == '__main__':
    main()