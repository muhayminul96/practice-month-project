import tkinter as tk

root = tk.Tk()
root.title("calculator")

e = tk.Entry(root, width=35, borderwidth=10)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def add_data(number):
    current = e.get()
    e.delete(0, tk.END)
    e.insert(0, str(current) + str(number))


def allclear():
    e.delete(0, tk.END)


def add_value():
    first_number = e.get()
    global f_vallue
    global math
    math = 'add'
    f_vallue = int(first_number)
    e.delete(0, tk.END)


def minus_value():
    first_number = e.get()
    global f_vallue
    global math
    math = 'minus'
    f_vallue = int(first_number)
    e.delete(0, tk.END)


def divition_value():
    first_number = e.get()
    global f_vallue
    global math
    math = 'divition'
    f_vallue = int(first_number)
    e.delete(0, tk.END)


def multiply_value():
    first_number = e.get()
    global f_vallue
    global math
    math = 'multiply'
    f_vallue = int(first_number)
    e.delete(0, tk.END)


def equal_value():
    sec_number=e.get()
    e.delete(0, tk.END)
    if math=="add":
        e.insert(0, f_vallue + int(sec_number))
    elif math == "minus":
        e.insert(0, f_vallue - int(sec_number))
    elif math == "divition":
        e.insert(0, f_vallue / int(sec_number))
    elif math == "multiply":
        e.insert(0, f_vallue * int(sec_number))



buttun_1 = tk.Button(root, text='1', padx=40, pady=20, command=lambda: add_data(1))
buttun_2 = tk.Button(root, text='2', padx=40, pady=20, command=lambda: add_data(2))
buttun_3 = tk.Button(root, text='3', padx=40, pady=20, command=lambda: add_data(3))
buttun_4 = tk.Button(root, text='4', padx=40, pady=20, command=lambda: add_data(4))
buttun_5 = tk.Button(root, text='5', padx=40, pady=20, command=lambda: add_data(5))
buttun_6 = tk.Button(root, text='6', padx=40, pady=20, command=lambda: add_data(6))
buttun_7 = tk.Button(root, text='7', padx=40, pady=20, command=lambda: add_data(7))
buttun_8 = tk.Button(root, text='8', padx=40, pady=20, command=lambda: add_data(8))
buttun_9 = tk.Button(root, text='9', padx=40, pady=20, command=lambda: add_data(9))
buttun_0 = tk.Button(root, text='0', padx=40, pady=20, command=lambda: add_data(0))
buttun_plus = tk.Button(root, text='+', padx=39, pady=20, command=add_value)
buttun_minus = tk.Button(root, text='-', padx=39, pady=20, command=minus_value)
buttun_divison = tk.Button(root, text='/', padx=39, pady=20, command=divition_value)
buttun_multiply = tk.Button(root, text='*', padx=39, pady=20, command=multiply_value)
buttun_equal = tk.Button(root, text='=', padx=83, pady=20, command=equal_value)
buttun_clear = tk.Button(root, text='clear', padx=74, pady=20, command=lambda: allclear())
# position
buttun_1.grid(row=3, column=0)
buttun_2.grid(row=3, column=1)
buttun_3.grid(row=3, column=2)

buttun_4.grid(row=2, column=0)
buttun_5.grid(row=2, column=1)
buttun_6.grid(row=2, column=2)

buttun_7.grid(row=1, column=0)
buttun_8.grid(row=1, column=1)
buttun_9.grid(row=1, column=2)

buttun_0.grid(row=6, column=0)
buttun_plus.grid(row=5, column=0)
buttun_equal.grid(row=6, column=1, columnspan=2)
buttun_clear.grid(row=5, column=1, columnspan=2)
buttun_minus.grid(row=4, column=0)
buttun_divison.grid(row=4, column=1)
buttun_multiply.grid(row=4, column=2)
root.mainloop()
