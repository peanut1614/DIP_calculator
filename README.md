# MyCalculator
ตัวอย่างโครงการในวิชา AI

## Introduction
เครื่องคิดเลข

## Installation
1. Install python
2. execute python main.py

## Note
### 2023-11-29
1. เชื่อม vscode กับ github ปุ่ม  download git on window
2. กดปุ่ม clone ใน vscode
3. พิมพ์จดหัวข้อต่างๆ ที่ต้องการ โดย # จะแทนหัวข้อใหญ่ ## แทนหัวข้อย่อย
4. control s เพื่อเซฟงานที่จด
5. กด terminal เลือก new terminal 
6. config git ในเครื่อง โดยพิมพ์ git config --global user.name "peanut1614" และ git config --global user.email ratnalinrp@gmail.com ในอีกบรรทัด
7. ตั้งชื่อไฟล์ใน massage และกด commit

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