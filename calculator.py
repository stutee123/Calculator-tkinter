from tkinter import *

root = Tk()
root.title("Calculator")
root.geometry=("500x500")
#entry box in calculator

box=Entry(root, width=65, borderwidth=10, bg="light blue")
box.grid(row=0, column=0, columnspan=5,pady=5)
#buttons GUI 
button1 = Button(root, text="1",borderwidth=5,bg="light blue", padx=40, pady=10, command=lambda: calculate(1)).grid(row=1, column=0)
button2 = Button(root, text="2",borderwidth=5,bg="light blue", padx=40, pady=10, command=lambda: calculate(2)).grid(row=1, column=1)
button3 = Button(root, text="3",borderwidth=5,bg="light blue", padx=40, pady=10, command=lambda: calculate(3)).grid(row=1, column=2)
button4 = Button(root, text="4",borderwidth=5,bg="light blue", padx=40, pady=10, command=lambda: calculate(4)).grid(row=2, column=0)
button5 = Button(root, text="5",borderwidth=5,bg="light blue", padx=40, pady=10, command=lambda: calculate(5)).grid(row=2, column=1)
button6 = Button(root, text="6",borderwidth=5,bg="light blue", padx=40, pady=10, command=lambda: calculate(6)).grid(row=2, column=2)
button7 = Button(root, text="7",borderwidth=5,bg="light blue", padx=40, pady=10, command=lambda: calculate(7)).grid(row=3, column=0)
button8 = Button(root, text="8",borderwidth=5,bg="light blue", padx=40, pady=10, command=lambda: calculate(8)).grid(row=3, column=1)
button9 = Button(root, text="9",borderwidth=5,bg="light blue", padx=40, pady=10, command=lambda: calculate(9)).grid(row=3, column=2)
button0 = Button(root, text="0",borderwidth=5,bg="light blue", padx=40, pady=10, command=lambda: calculate(0)).grid(row=4, column=0)

buttonAdd = Button(root, text="+",borderwidth=5,bg="light blue", padx=40, pady=10, command=lambda: add()).grid(row=1, column=4)
buttonSubtract = Button(root, text="-",borderwidth=5,bg="light blue", padx=40, pady=10, command=lambda: subtract()).grid(row=2, column=4)
buttonMultiply = Button(root, text="x",borderwidth=5,bg="light blue", padx=40, pady=10, command=lambda: multiply()).grid(row=3, column=4)
buttonDivide = Button(root, text="/",borderwidth=5,bg="light blue", padx=40, pady=10, command=lambda: divide()).grid(row=4, column=4)

buttonEqual= Button(root, text="=",borderwidth=5,bg="light blue", padx=40, pady=10, command=lambda: equal()).grid(row=4, column=2)
buttonClear= Button(root, text="C",borderwidth=5,bg="light blue", padx=40, pady=10, command=lambda: clear()).grid(row=4, column=1)
#to get the number from input box
def calculate(number):
    firstNum = box.get()
    box.delete(0, END)
    box.insert(0,str(firstNum) + str(number))
#for clearing
def clear():
    box.delete(0,END)
#for addition
def add():
    global num1
    global math
    math = "add"
    num1 = box.get()
    box.delete(0,END)
#for subtraction
def subtract():
    global num1
    global math
    math = "subtract"
    num1=box.get()
    box.delete(0, END)
#for division
def divide():
    global num1
    global math
    math = "divide"
    num1 = box.get()
    box.delete(0,END)
#for multiplication
def multiply():
    global num1
    global math
    math = "multiply"
    num1 = box.get()
    box.delete(0,END)
#for remainder
#for equal
def equal():
    num2=box.get()
    box.delete(0, END)
    if math == "add":
        box.insert(0, int(num1) + int(num2))
    elif math == "subtract":
        box.insert(0, int(num1) - int(num2))
    elif math == "multiply":
        box.insert(0, int(num1) * int(num2))
    else:
        box.insert(0, int(num1) / int(num2))

   
root.mainloop()