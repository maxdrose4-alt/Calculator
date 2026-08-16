import time
import threading
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

ltxt = []
label = None

def label_updater():
    global label
    label = tk.Label(root, text="", font=("Arial", 30), wraplength=root.winfo_width())
    label.grid(row=0, column=1, columnspan=3, pady=20, sticky="ew")
    while True:
        label.config(text=''.join(map(str, ltxt)))
        time.sleep(0.1)
        oplist = ("x", "-", "+", "/")
        for target in oplist:
            if target in ltxt:
                position = ltxt.index(target)

def buttons():
    # Number buttons grid layout: rows 1-3, columns 1-3
    button_map = {
        '1': (1, 1), '2': (1, 2), '3': (1, 3),
        '4': (2, 1), '5': (2, 2), '6': (2, 3),
        '7': (3, 1), '8': (3, 2), '9': (3, 3),
        '0': (4, 2)
    }
    
    for num, (row, col) in button_map.items():
        tk.Button(root, text=num, width=2, font=("Arial", 30),
                  command=lambda n=num: ltxt.append(n)).grid(row=row, column=col, sticky="nsew")
    
    # Operation buttons in column 4
    operations = [('+', 1), ('-', 2), ('x', 3), ('/', 4)]
    for op, row in operations:
        tk.Button(root, text=op, width=2, font=("Arial", 30),
                  command=None).grid(row=row, column=4, sticky="nsew")
    
    # Special buttons: AC (clear) and calc (equals)
    tk.Button(root, text="AC", width=2, font=("Arial", 30),
              command=lambda: ltxt.clear()).grid(row=4, column=1, sticky="nsew")
    tk.Button(root, text="calc", width=2, font=("Arial", 30),
              command=None).grid(row=4, column=3, sticky="nsew")

root = tk.Tk()
root.geometry("310x400")
root.title("Python Calculator")

for col in range(1, 5):
    root.columnconfigure(col, weight=1)
for row in range(0, 5):
    root.rowconfigure(row, weight=1)

labelthread = threading.Thread(target=label_updater, daemon=True)
labelthread.start()
buttons()

root.mainloop()