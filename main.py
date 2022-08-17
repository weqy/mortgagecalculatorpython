import tkinter as tk  # gui
from tkinter import *

ws = tk.Tk()  # canvas
ws.title('mortgage calculator weq')  # canvas title

canvas1 = tk.Canvas(width=400, height=300)  # canvas height and width
canvas1.pack()  # create canvas

money_range_x = [0, 300000, 100000, 2000]
money_range_y = [7, 600000, 200000, 27000]
user_instructions = ["Annual Interest Rate:", "Price of House:", "Downpayment:", "Yearly Property Tax:"]
var_names = ["interest_val", "house_val", "payment_val", "tax_val"]
widget_coordinates_x = [65, 100, 140, 180]
label_names = ["interestLabel", "houseLabel", "paymentLabel", "taxLabel"]
instruction_labels = ["instructions", "instructions2", "instructions3", "instructions4"]
scale_names = ["interest_rate", "house_price", "downpayment", "yearly_tax"]


x = 0
for x in range(4):
    instruction_labels[x] = tk.Label(ws, text=user_instructions[x], font=('helvetica', 10), width=16, anchor="e")
    canvas1.create_window(120, widget_coordinates_x[x], window=instruction_labels[x])  # show instructions
    var_names[x] = IntVar()
    scale_names[x] = tk.Scale(ws, from_=money_range_x[x], to=money_range_y[x], orient=HORIZONTAL, variable=var_names[x], showvalue=bool(0))
    canvas1.create_window(250, widget_coordinates_x[x], window=scale_names[x])  # shows entry in canvas
    label_names[x] = tk.Label(ws, textvariable=var_names[x])
    canvas1.create_window(330, widget_coordinates_x[x], window=label_names[x])

    x += x+1

ws.btn = tk.Button(ws, text = 'Enter', bd = '5', command= (lambda: create_loan())) # create button that runs welMsg
canvas1.create_window(200, 260, window=ws.btn) # show button
interest1 = tk.Entry(ws)


def create_canvas(): # define function
    canvas1.delete("all")  # delete everything in canvas

def create_loan():
    P = float(scale_names[1].get()) - float(scale_names[2].get())
    months = 30 * 12
    rate = float(scale_names[0].get())/100
    tax_yearly = float(scale_names[3].get())


    create_canvas()

    result2 = tk.Label(ws, text="Your monthly payment is:", font=('helvetica', 10))  # instructions for user
    canvas1.create_window(200, 140, window=result2)  # show instructions

    result2 = tk.Label(ws, text="$" + str(round((rate / 12) * (1 / (1 - (1 + rate / 12) ** (-months))) * P + (tax_yearly/12), 2)), font=('helvetica', 10))  # instructions for user
    canvas1.create_window(200, 160, window=result2)  # show instructions

ws.mainloop() # run tkinter event loop
