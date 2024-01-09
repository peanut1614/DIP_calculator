import tkinter as tk

class mycalculator:
    title = "my Calculator"
    def __init__(self):

        self.root = tk.Tk()
        self.label_taxt = tk.StringVar()
        self.label_taxt.set("")

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
        self.button.bind( "<Button-1>" , self.action2)

        self.button=tk.Button(self.root, text='%', height=3, width=7)
        self.button.place(x=150, y=50)

        self.button=tk.Button(self.root, text='9', height=3, width=7)
        self.button.place(x=150, y=110)
        self.button.bind( "<Button-1>" , self.action9)

        self.button=tk.Button(self.root, text='6', height=3, width=7)
        self.button.place(x=150, y=170)
        self.button.bind( "<Button-1>" , self.action6)

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
        self.label_taxt.set(self.label_taxt.get()+"0")
        self.label.pack()
    
    def action2(self, event):
        print(event)
        self.title = "Test"
        self.root.title(self.title)
        self.label_taxt.set(self.label_taxt.get()+"2")
        self.label.pack()

    def action9(self, event):
        print(event)
        self.title = "Test"
        self.root.title(self.title)
        self.label_taxt.set(self.label_taxt.get()+"9")
        self.label.pack() 

    def action6(self, event):
        print(event)
        self.title = "Test"
        self.root.title(self.title)
        self.label_taxt.set(self.label_taxt.get()+"6")
        self.label.pack()    

mycalculator()        

## Disclaimer
for educational purpose only. Run on your own risk.
    def evaluate(self):
        self.total_expression += self.current_expression
        self.update_total_label()
        try:
            self.current_expression = str(eval(self.total_expression))

            self.total_expression = ""
        except Exception as e:
            self.current_expression = "Error"
        finally:
            self.update_label()

    def create_equals_button(self):
        button = tk.Button(self.buttons_frame, text="=", bg=LIGHT_BLUE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=self.evaluate)
        button.grid(row=4, column=3, columnspan=2, sticky=tk.NSEW)

    def create_buttons_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame

    def update_total_label(self):
        expression = self.total_expression
        for operator, symbol in self.operations.items():
            expression = expression.replace(operator, f' {symbol} ')
        self.total_label.config(text=expression)

    def update_label(self):
        self.label.config(text=self.current_expression[:11])

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    calc = Calculator()
    calc.run()