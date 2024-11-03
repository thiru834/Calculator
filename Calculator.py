import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("300x400")
        
       
        self.input_text = ""
        self.input_var = tk.StringVar()
        
        
        self.display = tk.Entry(root, textvariable=self.input_var, font=('Arial', 18), bd=10, insertwidth=8, width=14, borderwidth=4)
        self.display.grid(row=0, column=0, columnspan=4)
        
        
        self.create_buttons()
    
    
    def press(self, value):
        self.input_text += str(value)
        self.input_var.set(self.input_text)
    
    
    def clear(self):
        self.input_text = ""
        self.input_var.set("")

    
    def calculate(self):
        try:
            result = str(eval(self.input_text))  
            self.input_var.set(result)           
            self.input_text = result             
        except Exception as e:
            messagebox.showerror("Error", "Invalid Input")
            self.clear()

    
    def create_buttons(self):
        
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
            ('C', 5, 0)
        ]
        
        
        for (text, row, col) in buttons:
            if text == "=":
                button = tk.Button(self.root, text=text, padx=20, pady=20, font=('Arial', 18),
                                   command=self.calculate)
            elif text == "C":
                button = tk.Button(self.root, text=text, padx=20, pady=20, font=('Arial', 18),
                                   command=self.clear)
            else:
                button = tk.Button(self.root, text=text, padx=20, pady=20, font=('Arial', 18),
                                   command=lambda val=text: self.press(val))
            button.grid(row=row, column=col, sticky="nsew")
        
        
        for i in range(5):
            self.root.grid_rowconfigure(i, weight=1)
            self.root.grid_columnconfigure(i, weight=1)


if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
