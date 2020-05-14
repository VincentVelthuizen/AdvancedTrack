from tkinter import *


def icalc(source, side):
    store_obj = Frame(source, borderwidth=4, bd=4, bg="powder blue")
    store_obj.pack(side=side, expand=YES, fill=BOTH)
    return store_obj


def button(source, side, text, command=None):
    store_obj = Button(source, text=text, command=command)
    store_obj.pack(side=side, expand=YES, fill=BOTH)
    return store_obj


class Calculator(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master=master)
        self.option_add("*Font", "arial 20 bold")
        self.pack(expand=YES, fill=BOTH)
        self.master.title("Calculator")

        display = StringVar()
        Entry(self, textvariable=display,
                    justify='right').pack(side=TOP, expand=YES, fill=BOTH)

        for clearButton in (["C"]):
            erase = icalc(self, TOP)
            for ichar in clearButton:
                button(erase, LEFT, ichar, lambda
                    store_obj=display, q=ichar: store_obj.set(''))

        for num_button in ("789/", "456*", "123-", "0.+"):
            function_num = icalc(self, TOP)
            for iEquals in num_button:
                button(function_num, LEFT, iEquals, lambda
                    store_obj=display, q=iEquals: store_obj
                       .set(store_obj.get() + q))


if __name__ == "__main__":
    root = Tk()
    root.geometry("800x600")

    Calculator(root).mainloop()
