import tkinter
from tkinter import Text
import os

def tips(amount, tip):
    try:
        user_amount = float(amount)
        user_tip = int(tip)
        tip_value = amount * (tip/100)
        print("Your tip value is:", round(tip_value, 2))

    except ValueError:
        pass

# creating a window
root = tkinter.Tk()
root.title('Tip Calculator')
# root.iconbitmap('Users/webster/python projects/tip-calculator/tip.png')
root.geometry("350x300")
root.configure(background="#fde2e4")

header = tkinter.Label(root, text="Tip calculator - Calculate your tips!", bg="#fde2e4", pady=20)
header.config(font=('Poppins', 20))
header.pack()

# the bill space
amount_label = tkinter.Label(root, text="Bill: ", bg="#fde2e4")
amount_label.place(relx=0.15, rely=0.3)

amount = tkinter.Entry(root, bg="white", bd=1)
amount.place(relx=0.27, rely=0.3)


# the tip space
tip_label = tkinter.Label(root, text="Tip%:", bg="#fde2e4")
tip_label.place(relx=0.15, rely=0.5)

tip_amount = tkinter.Entry(root, bg="white", bd=1)
tip_amount.place(relx=0.27, rely=0.5)

# command=tips(int_amount, int_tip)

# button
button = tkinter.Button(width=15, height=2, bg="#eae4e9", text="Calculate",)
button.place(relx=0.31, rely=0.75)
root.mainloop()

