import sys
import time
try:
    import tkinter as tk
    from tkinter import messagebox
except ImportError:
    print("Install tkinter first")
    while True:
        awnser = input("need help(y/n): ")
        if awnser == "y":
            print("https://www.google.com/search?q=how+to+download+tkinter+for+python+on+windows+and+linux&client=firefox-b-lm&hs=E87&sca_esv=adee44be14316a28&sxsrf=APpeQnss0B9EcKiGBgGFe2zRZzWUiF_FrQ%3A1786990673363&udm=50&fbs=ABfTbFVyMZGZf1hfvX9uKjN_-G8cxpBkeIeqYwoCbfNVc4vKE96grTuFPBRY0pmGfUF9Jyg22UXWVTXr_K4O7baggKlov48NXS5kRplAMJjbPPm0X9zx9XJOt5E0nixXQZ6ClmxeNesnKPOEsv_UauTBzQDb7CVCiTOdZZHLjS3PdL7LnlkOsTi1XwuRJnK7lO0dgYC4wQZ1&aep=1&ntc=1&cs=1&sa=X&ved=2ahUKEwiYv7WCo6iWAxVaRPEDHdVFMIMQ2J8OegQICxAD&biw=1920&bih=938&dpr=1&atvm=2&mstk=AUtExfCnz-Qz9xhbEbUIwxbr03HaTkIC5LH7EK9HdtPA1PWw-Arrin9onzIGFH4WZ1nbU7nbaYYTJSZ6eYqVzc4gOt8lnqjybf8OmQhXUdryM0V_wBLr8LTNTmwusARj2_q3OwdQUdWvcvbg-fvrguvzQACOFF621ZSgogARODzy8sHszgQ3rRGWgRiTy4t4mYEcWDURbCo87tbB5MmaTfyefGgu-yguwkXjgSndbLR10N5qMQ2dngwUv1lBEOeuXybkQ_e23mj1N4LfmGikHLGE9goZkTdv7LB0i7nTW0YYQ0oiKZD-KkhUeyPUTuGUjbYi-gtucARMIL1nxw&csuir=1&mtid=U1CDavesF-2Txc8Pra_AwA8")
            sys.exit()
        elif awnser == "n":
            print("okay bye")
            sys.exit()
        else: print(f"type y or n not sum {awnser} bullshit\nbut i like you\nso here have a poem:\n\nroses are red so much is true\nbut your inputs are not\nso fuck you")
        time.sleep(10)

ltxt = []

def math():
    def add(x, y): x+y
    def sub(x, y): x-y
    def mult(x, y): x*y
    def div(x, y): x/y
    def exp(x, y): x**y
    def roo(x): x**0.5

    ops = {
            "+":add,
            "-":sub,
            "*":mult,
            "/":div,
            "^":exp,
            "√":roo
                    }
math()

def matherror():
    messagebox.showerror( "Error!!", "Please enter a valid calculatio\nyour calculation will now be deleted.")
    clear_label()

def remove_last():
    if len(ltxt) != 0: del ltxt[-1]
    update_label()

def clear_label():
    ltxt.clear()
    update_label()

def calc():
    calcu = "".join(map(str, ltxt))
    for op in opmap.keys():
        if op != "-":
            if op in calcu:
                if calcu.startswith(op): matherror()
        for opa in opmap.keys(): 
            if op+opa in calcu: matherror()
                


def update_label():
    if len(ltxt)>36:
        messagebox.showerror("Too big", f"the calculatoin:\n{"".join(map(str, ltxt))}\nis to big for me press your super(windows) key and type 'calc' then hit enter\nyour calculation will now be deleted")
        clear_label()
    label.config(text="".join(map(str, ltxt)))

def presskey(char):
    ltxt.append(char)
    update_label()

def buttons():
    bmap = {1: (2, 1), 2: (2, 2), 3: (2, 3),
            4: (3, 1), 5: (3, 2), 6: (3, 3),
            7: (4, 1), 8: (4, 2), 9: (4, 3),
            0: (5, 1), ".": (5, 2)
                       }
    for num, (row, col) in bmap.items():#number buttons
        tk.Button(root, text=num, width=2, font=("Arial", 30),   command=lambda n = num: presskey(n)).grid(row=row, column= col, sticky="nsew")
    global opmap 
    opmap = {"+": (2, 4), "^": (1, 2),
             "-": (3, 4), 
             "-": (3, 4), "√": (1, 3),
             "-": (3, 4), 
             "*": (4, 4),
             "/": (5, 4)
            }
    
    for op, (row, col) in opmap.items(): #operation buttons
        tk.Button(root, width=2, text=op, font=("Arial", 30),  command=lambda o = op: presskey(o)).grid(row=row, column=col, sticky="nsew")

    #the special buttons vol. 1 AC
    tk.Button(root, text="AC", width=2, font=("Arial", 30), command=lambda: clear_label()).grid(row=1, column=1, sticky="nsew")

    #the special buttons vol. 2 Backspace
    tk.Button(root, text="⌫", width=2, font=("arial", 30), command=lambda: remove_last()).grid(row=5, column=3, sticky="nsew")

    #the special buttons vol. 3 "="
    tk.Button(root, text="=", width=2, font=("Arial", 30), command=calc).grid(row= 1, column=4)


root = tk.Tk()
root.geometry("290x445")
root.title("python calculator")
root.resizable(False, False)

label = tk.Label(root, text="", font=("arial", 30), wraplength=280, height=3, anchor="e")
label.grid(row=0, column=1,columnspan=4)
buttons()
root.mainloop()