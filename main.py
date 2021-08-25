from tkinter import *

def main():
    root = Tk()

    class TicTakToe:

        def __init__(self, root):
            self.root = root
            self.root.title("TicTakToe")
            self.root.geometry("900x600")
            self._9button = IntVar
            self.player_term = "X"
            self.b = {}


            button_label = LabelFrame(self.root)
            button_label.place(x=100, y=100, relwidth=0.75, relheight= 0.7)
            self.b[1] = Button(button_label, text=" ",font=("comicsans",50), command=lambda:self.change_val(1))
            self.b[2] = Button(button_label, text=" ",font=("comicsans",50), command=lambda:self.change_val(2))
            self.b[3] = Button(button_label, text=" ",font=("comicsans",50), command=lambda:self.change_val(3))
            self.b[4] = Button(button_label, text=" ",font=("comicsans",50), command=lambda:self.change_val(4))
            self.b[5] = Button(button_label, text=" ",font=("comicsans",50), command=lambda:self.change_val(5))
            self.b[6] = Button(button_label, text=" ",font=("comicsans",50), command=lambda:self.change_val(6))
            self.b[7] = Button(button_label, text=" ",font=("comicsans",50), command=lambda:self.change_val(7))
            self.b[8] = Button(button_label, text=" ",font=("comicsans",50), command=lambda:self.change_val(8))
            self.b[9] = Button(button_label, text=" ",font=("comicsans",50), command=lambda:self.change_val(9))

            self.b[1].grid(row=0, column=0, padx=75, pady=20)
            self.b[2].grid(row=0, column=1, padx=100, pady=20)
            self.b[3].grid(row=0, column=2, padx=100, pady=20)
            self.b[4].grid(row=1, column=0, padx=75, pady=50)
            self.b[5].grid(row=1, column=1, padx=100, pady=50)
            self.b[6].grid(row=1, column=2, padx=100, pady=50)
            self.b[7].grid(row=2, column=0, padx=75, pady=50)
            self.b[8].grid(row=2, column=1, padx=100, pady=50)
            self.b[9].grid(row=2, column=2, padx=100, pady=50)

            player_label = LabelFrame(self.root)
            player_label.place(x=50, y=5, relwidth=0.9, relheight=0.15)
            self.current_player = Label(player_label, text=" Current player:", font=("comicsans",32))
            self.current_player.grid(row=0, column=0, padx=150)
            self.x_or_0 = Label(player_label, text=self.player_term, font=("comiscans",56))
            self.x_or_0.grid(row=0, column=1)


        def change_button(self,butt):
            if self.player_term == "X":
                self.b[butt].configure(text="X")
            elif self.player_term == "0":
                self.b[butt].configure(text="0")


        def change_val(self, butt):
            if self.b[butt].cget("text") != " ":
                print("This button is already used")
                return None
            else:
                self.change_button(butt)
                if self.player_term == "X":
                    self.player_term = "0"
                    self.x_or_0.configure(text=self.player_term)
                elif self.player_term == "0":
                    self.player_term = "X"
                    self.x_or_0.configure(text=self.player_term)






    TicTakToe(root)
    root.mainloop()






if __name__ == '__main__':
    main()