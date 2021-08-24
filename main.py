from tkinter import *

def main():
    root = Tk()

    class TicTakToe:

        def __init__(self, root):
            self.root = root
            self.root.title("TicTakToe")
            self.root.geometry("900x600")

            button_label = LabelFrame(self.root)
            button_label.place(x=100, y=100, relwidth=0.75, relheight= 0.7)
            self.up_left_bt = Button(button_label, text=" ",font=("comicsans",50))
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


    TicTakToe(root)
    root.mainloop()






if __name__ == '__main__':
    main()