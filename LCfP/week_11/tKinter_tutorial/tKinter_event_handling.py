from tkinter import *


class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):

        self.master.title("GUI")

        self.pack(fill=BOTH, expand=1)

        quit_button = Button(self, text="Quit", command=self.client_exit)

        quit_button.place(x=0, y=0)

    def client_exit(self):
        print("Exiting because the button was pushed")
        exit()


root = Tk()
root.geometry("400x300")

app = Window(root)
root.mainloop()
