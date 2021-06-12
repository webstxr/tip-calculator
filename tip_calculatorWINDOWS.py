import tkinter


# function to calculate the tip
def tips(bill, tip):
    try:
        user_amount = float(bill.get())
        user_tip = int(tip.get())
        tip_value = round(user_amount * (user_tip/100), 2)
        result_label.config(text=tip_value)

    except ValueError:
        result_label.config(text='Try again')


# creating a window
root = tkinter.Tk()
root.title('Tip Calculator')
root.geometry("350x300")
root.resizable(width=False, height=False)
root.configure(background="#fde2e4")

# header with title
header = tkinter.Label(root, text="Calculate your tips!", bg="#fde2e4", pady=20, fg="#ff91b9")
header.config(font=('Nexa bold', 20))
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
button = tkinter.Button(width=10, height=1,
                        highlightbackground="#ffafcc",
                        text="Calculate", fg="#ff79aa",
                        command=lambda: tips(amount, tip_amount))
button.place(relx=0.31, rely=0.65)
button.config(font=('Nexa bold', 16))

# space for the result display
result_label = tkinter.Label(root, bg="#fde2e4", bd=2, width=10)
result_label.place(relx=0.35, rely=0.85)

root.mainloop()
