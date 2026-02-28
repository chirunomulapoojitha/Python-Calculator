from tkinter import *
import math

# ---------- Window ----------
root = Tk()
root.title("Smart Calculator")

# Start in maximized mode
root.state("zoomed")

root.config(bg="#111")

# ---------- Outer Box ----------
outer = Frame(root, bg="#000", bd=5, relief=RIDGE)
outer.place(relx=0.5, rely=0.5, anchor="center")

# ---------- Display ----------
display = Entry(outer, font=("Arial", 28, "bold"), bd=0,
                bg="#222", fg="white", justify="right")
display.pack(fill="both", ipadx=8, pady=15, padx=10)

# ---------- Functions ----------
def press(val):
    display.insert(END, val)

def clear():
    display.delete(0, END)

def delete():
    current = display.get()
    display.delete(0, END)
    display.insert(0, current[:-1])

def equal():
    try:
        result = eval(display.get())
        display.delete(0, END)
        display.insert(0, result)
    except:
        display.delete(0, END)
        display.insert(0, "Error")

def square():
    try:
        val = float(display.get())
        display.delete(0, END)
        display.insert(0, val * val)
    except:
        display.delete(0, END)
        display.insert(0, "Error")

def sqrt():
    try:
        val = float(display.get())
        display.delete(0, END)
        display.insert(0, math.sqrt(val))
    except:
        display.delete(0, END)
        display.insert(0, "Error")

# ---------- Buttons Frame ----------
frame = Frame(outer, bg="#111")
frame.pack()

btn_color = "#ff6b6b"
operator_color = "#00c6ff"

buttons = [
    ("C", clear, "red"), ("DEL", delete, btn_color), ("%", lambda: press("%"), btn_color), ("/", lambda: press("/"), operator_color),
    ("7", lambda: press("7"), btn_color), ("8", lambda: press("8"), btn_color), ("9", lambda: press("9"), btn_color), ("*", lambda: press("*"), operator_color),
    ("4", lambda: press("4"), btn_color), ("5", lambda: press("5"), btn_color), ("6", lambda: press("6"), btn_color), ("-", lambda: press("-"), operator_color),
    ("1", lambda: press("1"), btn_color), ("2", lambda: press("2"), btn_color), ("3", lambda: press("3"), btn_color), ("+", lambda: press("+"), operator_color),
    ("√", sqrt, operator_color), ("x²", square, operator_color), (".", lambda: press("."), btn_color), ("0", lambda: press("0"), btn_color),
]

row = 0
col = 0

for text, cmd, color in buttons:
    Button(frame, text=text, command=cmd,
           width=5, height=2,
           font=("Arial", 16, "bold"),
           bg=color, fg="white").grid(row=row, column=col, padx=5, pady=5)

    col += 1
    if col > 3:
        col = 0
        row += 1

# ---------- Rectangle Equal Button ----------
Button(frame, text="=", command=equal,
       font=("Arial", 20, "bold"),
       bg="green", fg="white",
       height=2).grid(row=row+1, column=0, columnspan=4,
                      sticky="nsew", padx=5, pady=5)

root.mainloop()