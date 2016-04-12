#The imported modules:
from tkinter import *

class Dot:
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.id = PhotoImage(file = "C://Dot.gif")
        self.canvas.create_image(x, y, image = self.id)

#The 'x' global variable:
x = [-3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = []

def graph():
    #Allowing the User to choose the function they want to use:
    print ("\t\t\t\tGraphing Calculator")
    print (" ")
    print ("Choose a function:")
    print ("1.)   Direct Variation (y = ax)")
    print ("2.)   Linear (y = mx + b)")
    print ("3.)   Inverse Variation (y = a / x)")
    print ("4.)   Quadratic Equation (ax * ax + bx + c = 0)")
    print ("5.)   Other (you piece it together).")
    decision = int(input(" "))

    if decision == 1:
        print ("What does 'a' equal?")
        a = int(input(" "))
        for i in x:
            y.append(a * i)

    if decision == 2:
        print ("What does 'm' equal?")
        m = int(input(" "))
        print ("What does 'b' equal?")
        b = int(input(" "))
        for i in x:
            y.append(m * i + b)

    if decision == 3:
        print ("What does 'a' equal?")
        a = int(input(" "))
        for i in x:
            y.append(a / i)

    if decision == 4:
        print ("What does 'a' equal?")
        a = int(input(" "))
        print ("What does 'c' equal?")
        c = int(input(" "))
        print ("What does 'b' equal?")
        b = int(input(" "))
        for i in x:
           y.append( a * i ** 2 + b * i + c)

    if decision == 5:
        print ("To make your own function, you must answer some questions.")
        print ("The formula will be in the format: y = x ? ?.")
        print ("The first '?' will be an operator, and the second '?' will be a number.")
        print (" ")
        print ("Choose an operator.")
        print ("1.)   +")
        print ("2.)   -")
        print ("3.)   /")
        print ("4.)   *")
        print ("5.)   ** (to the power of)")
        op = int(input(" "))
        print (" ")
        print ("Enter the number.")
        number = int(input(" "))
        if op == 1:
            for i in x:
                y.append(i + number)
        if op == 2:
            for i in x:
                y.append(i - number)
        if op == 3:
            for i in x:
                y.append(i / number)
        if op == 4:
            for i in x:
                y.append(i * number)
        if op == 5:
            for i in x:
                y.append(i ** number)

graph()
tk = Tk()
tk.wm_attributes("-topmost", 1)
tk.title("Graph")
canvas = Canvas(tk, width = 500, height = 500)
graph = PhotoImage(file = "C://Graph.gif")
canvas.create_image(0, 0, anchor = NW, image = graph)
canvas.pack()

dot = []

for j in range(10):
     dot.append(Dot(canvas, x[j] * -15 + 250,  y[j] * 15 + 250))
