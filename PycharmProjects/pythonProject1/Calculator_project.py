from tkinter import *

expression = ""


def press(var):
    global expression
    expression = expression + str(var)
    equation.set(expression)


def equal_press():
    global expression
    result = str(eval(expression))
    equation.set(result)
    expression = ""


def clear():
    equation.set("")
    expression = ""


if __name__ == "__main__":
    window = Tk()
    window.geometry("400x400")
    window.title("Calculator")
    window.configure(bg="#4a0000")

    equation = StringVar()

    expression_field = Entry(window, textvariable=equation,width=24)
    expression_field.grid(columnspan=4, ipadx=50, pady=(100, 10), padx=(100, 10))  #columnspan was very helpful


    button1 = Button(window, text="1", width=5, height=2, fg="red", command=lambda: press(1))
    button2 = Button(window, text="2", width=5, height=2, fg="red", command=lambda: press(2))
    button3 = Button(window, text="3", width=5, height=2, fg="red", command=lambda: press(3))
    button4 = Button(window, text="4", width=5, height=2, fg="red", command=lambda: press(4))
    button5 = Button(window, text="5", width=5, height=2, fg="red", command=lambda: press(5))
    button6 = Button(window, text="6", width=5, height=2, fg="red", command=lambda: press(6))
    button7 = Button(window, text="7", width=5, height=2, fg="red", command=lambda: press(7))
    button8 = Button(window, text="8", width=5, height=2, fg="red", command=lambda: press(8))
    button9 = Button(window, text="9", width=5, height=2, fg="red", command=lambda: press(9))
    button0 = Button(window, text="0", width=5, height=2, fg="red", command=lambda: press(0))
    button_add = Button(window, text="+", width=5, height=2, fg="red", command=lambda: press("+"))
    button_sub = Button(window, text="-", width=5, height=2, fg="red", command=lambda: press("-"))
    button_mult = Button(window, text="*", width=5, height=2, fg="red", command=lambda: press("*"))
    button_div = Button(window, text="/", width=5, height=2, fg="red", command=lambda: press("/"))
    button_res = Button(window, text="=", width=5, height=2, fg="red", command=equal_press)
    button_clear = Button(window, text="CLR", width=5, height=2, fg="red", command=clear)
    button_dot = Button(window, text=".", width=5, height=2, fg="red", command=lambda: press("."))

    button1.grid(row=0, column=0, sticky=W, pady=(200, 10), padx=(100, 10))
    button2.grid(row=0, column=1, sticky=W, pady=(200, 10), padx=10)
    button3.grid(row=0, column=2, sticky=W, pady=(200, 10), padx=10)
    button4.grid(row=1, column=0, sticky=W, pady=10, padx=(100, 10))
    button5.grid(row=1, column=1, sticky=W, pady=10, padx=10)
    button6.grid(row=1, column=2, sticky=W, pady=10, padx=10)
    button7.grid(row=2, column=0, sticky=W, pady=10, padx=(100, 10))
    button8.grid(row=2, column=1, sticky=W, pady=10, padx=10)
    button9.grid(row=2, column=2, sticky=W, pady=10, padx=10)
    button0.grid(row=3, column=1, sticky=W, pady=10, padx=10)
    button_add.grid(row=0, column=3, sticky=W, pady=(200, 10), padx=10)
    button_sub.grid(row=1, column=3, sticky=W, pady=10, padx=10)
    button_div.grid(row=2, column=3, sticky=W, pady=10, padx=10)
    button_mult.grid(row=3, column=3, sticky=W, pady=10, padx=10)
    button_res.grid(row=3, column=0, sticky=W, pady=10, padx=(100, 10))
    button_clear.grid(row=3, column=3, sticky=W, pady=10, padx=10)
    button_dot.grid(row=3, column=2, sticky=W, pady=10, padx=10)

    # label.pack()

    window.mainloop()
    print("End")
