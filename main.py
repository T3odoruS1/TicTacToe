from tkinter import *

def main():
    root = Tk()

    class TicTakToe:

        def __init__(self, root):
            self.root = root
            self.root.title("TicTakToe")
            self.root.geometry("900x600")

            button_label = LabelFrame(self.root)
            button_label.place(x=100, y=100, relwidth=0.7, relheight= 0.7)
            self.up_left_bt = Button(button_label, text="")
            self.up_cent_bt = Button(button_label, text="")
            self.up_right_bt = Button(button_label, text="")
            self.cent_left_bt = Button(button_label, text="")
            self.up_left_bt = Button(button_label, text="")
            self.up_left_bt = Button(button_label, text="")
            self.up_left_bt = Button(button_label, text="")
            self.up_left_bt = Button(button_label, text="")
            self.up_left_bt = Button(button_label, text="")

    TicTakToe(root)
    root.mainloop()






if __name__ == '__main__':
    main()