import tkinter
from tkinter import ttk


def tips(bill, tip):
    try:
        user_amount = float(bill.get())
        user_tip = int(tip.get())
        tip_value = round(user_amount * (user_tip/100), 2)
        result_label.config(text=tip_value)

    except ValueError:
        print("Value Error")

# creating a window
root = tkinter.Tk()
root.title('Tip Calculator')
root.geometry("350x300")
root.configure(background="#fde2e4")

# header with title
header = tkinter.Label(root, text="Tip calculator - Calculate your tips!", bg="#fde2e4", pady=20)
header.config(font=('Poppins', 20))
header.pack()

# the bill space
amount_label = tkinter.Label(root, text="Bill: ", bg="#fde2e4")
amount_label.place(relx=0.15, rely=0.3)

amount = tkinter.StringVar()
amount = tkinter.Entry(root, bg="white", bd=1)
amount.place(relx=0.27, rely=0.3)


# the tip space
tip_label = tkinter.Label(root, text="Tip%:", bg="#fde2e4")
tip_label.place(relx=0.15, rely=0.5)

tip_amount = tkinter.IntVar()
tip_amount = tkinter.Entry(root, bg="white", bd=1)
tip_amount.place(relx=0.27, rely=0.5)


# button
button = tkinter.Button(width=15, height=2, bg="#003B73", text="Calculate", command=lambda: tips(amount, tip_amount))
button.place(relx=0.31, rely=0.7)

# space for a result
result_label = tkinter.Label(root, bg="#fde2e4", bd=2, width=10)
result_label.place(relx=0.35, rely=0.85)

root.mainloop()
