import tkinter as tk

class mycalculator:
    title = "my Calculator"
    def __init__(self):

        self.root = tk.Tk()
        self.label_taxt = tk.StringVar()
        self.label_taxt.set("Hello DIP01")

        self.root.geometry("300x300")
        self.root.title(self.title)

        self.label = tk.Label(self.root, textvariable=self.label_taxt, font=('Arial', 18))
        self.label.pack()

        self.button_trig = tk.Button(self.root, text="trigger change title to \"Test\"", height=4, )
        self.button_my_cal = tk.Button(self.root, text="trigger change title to \"My Calculator\"", height=4, )
        

        self.button=tk.Button(self.root, text='C', height=3, width=7)
        self.button.place(x=20, y=50)

        self.button=tk.Button(self.root, text='7', height=3, width=7)
        self.button.place(x=20, y=110)

        self.button=tk.Button(self.root, text='4', height=3, width=7)
        self.button.place(x=20, y=170)

        self.button=tk.Button(self.root, text='1', height=3, width=7)
        self.button.place(x=20, y=230)

        self.button=tk.Button(self.root, text='0', height=3, width=16)
        self.button.place(x=20, y=290)

        self.button.bind( "<Button-1>" , self.action0)

        self.button=tk.Button(self.root, text='+/-', height=3, width=7)
        self.button.place(x=85, y=50)

        self.button=tk.Button(self.root, text='8', height=3, width=7)
        self.button.place(x=85, y=110)

        self.button=tk.Button(self.root, text='5', height=3, width=7)
        self.button.place(x=85, y=170)

        self.button=tk.Button(self.root, text='2', height=3, width=7)
        self.button.place(x=85, y=230)

        self.button=tk.Button(self.root, text='%', height=3, width=7)
        self.button.place(x=150, y=50)

        self.button=tk.Button(self.root, text='9', height=3, width=7)
        self.button.place(x=150, y=110)

        self.button=tk.Button(self.root, text='6', height=3, width=7)
        self.button.place(x=150, y=170)

        self.button=tk.Button(self.root, text='3', height=3, width=7)
        self.button.place(x=150, y=230)

        self.button=tk.Button(self.root, text='.', height=3, width=7)
        self.button.place(x=150, y=290)

        self.button=tk.Button(self.root, text='/', height=3, width=7)
        self.button.place(x=215, y=50)

        self.button=tk.Button(self.root, text='*', height=3, width=7)
        self.button.place(x=215, y=110)

        self.button=tk.Button(self.root, text='-', height=3, width=7)
        self.button.place(x=215, y=170)

        self.button=tk.Button(self.root, text='+', height=3, width=7)
        self.button.place(x=215, y=230)

        self.button=tk.Button(self.root, text='=', height=3, width=7)
        self.button.place(x=215, y=290)

        self.root.mainloop()

    def action0(self, event):
        print(event)
        self.title = "Test"
        self.root.title(self.title)
        self.label_taxt.set("DIP 01")
        self.label.pack()
    

mycalculator()        