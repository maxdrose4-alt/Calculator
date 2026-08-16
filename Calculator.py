try:
    import tkinter as tk
    from tkinter import messagebox
except ImportError:
    print("Install tkinter to run this program")

def math(): #calculator operations 

    def add(x, y): return x + y
    def subtract(x, y): return x - y
    def multiply(x, y): return x * y
    def divide(x, y): return x / y if y != 0 else print("Error, division by 0")

def buttons(): #them buttons
    
        btn_add = tk.Button(root, text="+", width=2, font=("Arial", 30), command="")
        btn_add.grid(row=1, column=4, sticky="ew")

        btn_subtract = tk.Button(root, text="-", width=2, font=("Arial", 30), command="")
        btn_subtract.grid(row=2, column=4, sticky="ew")

        btn_multiply = tk.Button(root, text="x", width=2, font=("Arial", 30), command="")
        btn_multiply.grid(row=3, column=4, sticky="ew")

        btn_divide = tk.Button(root, text="/", width=2, font=("Arial", 30), command="")
        btn_divide.grid(row=4, column=4, sticky="ew")

        btn1 = tk.Button(root, text="1", width=2, font=("Arial", 30), command="")
        btn1.grid(row=1, column=1, sticky="ew")

        btn2 = tk.Button(root, text="2", width=2, font=("Arial", 30), command="")
        btn2.grid(row=1, column=2, sticky="ew")

        btn3 = tk.Button(root, text="3", width=2, font=("Arial", 30), command="")
        btn3.grid(row=1, column=3, sticky="ew")

        btn4 = tk.Button(root, text="4", width=2, font=("Arial", 30), command="")
        btn4.grid(row=2, column=1, sticky="ew")

        btn5 = tk.Button(root, text="5", width=2, font=("Arial", 30), command="")
        btn5.grid(row=2, column=2, sticky="ew")

        btn6 = tk.Button(root, text="6", width=2, font=("Arial", 30), command="")
        btn6.grid(row=2, column=3, sticky="ew")

        btn7 = tk.Button(root, text="7", width=2, font=("Arial", 30), command="")
        btn7.grid(row=3, column=1, sticky="ew")

        btn8 = tk.Button(root, text="8", width=2, font=("Arial", 30), command="")
        btn8.grid(row=3, column=2, sticky="ew")

        btn9 = tk.Button(root, text="9", width=2, font=("Arial", 30), command="")
        btn9.grid(row=3, column=3, sticky="ew")

        btn0 = tk.Button(root, text="0", width=2, font=("Arial", 30), command="")
        btn0.grid(row=4, column=2, sticky="ew")

        btnac = tk.Button(root, text="AC", width=2, font=("Arial", 30), command="")
        btnac.grid(row=4, column=1, sticky="ew")

        btncalc = tk.Button(root, text="calc", width=2, font=("arial", 30), command="")
        btncalc.grid(row=4, column=3, sticky="ew")

def label_updater():
    label = tk.Label(root, text="", font=("Arial", 60))
    label.grid(row=0, column=0, columnspan=2, pady=20)


calc = []
calc2 = []

root = tk.Tk() #creating the window for the calc
root.geometry("310x400")
root.title("Python Calculator")

label_updater()
buttons()

root.mainloop()