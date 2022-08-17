import tkinter as tk  # gui
from tkinter import *

ws = tk.Tk()  # canvas
ws.title('fibonacci numbers python')  # canvas title

canvas1 = tk.Canvas(width=400, height=300)  # canvas height and width
canvas1.pack()  # create canvas

instructions = tk.Label(ws, text='Annual Interest Rate:', font=('helvetica', 10))  # instructions for user
canvas1.create_window(120, 60, window=instructions)  # show instructions

interest_val = IntVar()
interest_rate = tk.Scale(ws, from_=0, to=7, orient=HORIZONTAL, variable=interest_val, showvalue=bool(0))
canvas1.create_window(250, 65, window=interest_rate)  # shows entry in canvas
interestLabel = tk.Label(ws, textvariable=interest_val)
canvas1.create_window(310, 65, window= interestLabel)

instructions2 = tk.Label(ws, text='Price of House:', font=('helvetica', 10))  # instructions for user
canvas1.create_window(120, 100, window=instructions2)  # show instructions

house_val = IntVar()
house_price = tk.Scale(ws, from_=300000, to=600000, orient=HORIZONTAL, variable=house_val, showvalue=bool(0)) # create entry
canvas1.create_window(250, 100, window=house_price)  # shows entry in canvas
houseLabel = tk.Label(ws, textvariable=house_val)
canvas1.create_window(325, 100, window= houseLabel)

instructions3 = tk.Label(ws, text='Downpayment:', font=('helvetica', 10))  # instructions for user
canvas1.create_window(120, 140, window=instructions3)  # show instructions

payment_val = IntVar()
downpayment = tk.Scale(ws, from_=100000, to=200000, orient=HORIZONTAL, variable=payment_val, showvalue=bool(0)) # create entry
canvas1.create_window(250, 140, window=downpayment) # shows entry in canvas
paymentLabel = tk.Label(ws, textvariable=payment_val)
canvas1.create_window(325, 140, window= paymentLabel)


instructions4 = tk.Label(ws, text='Yearly Property Tax:', font=('helvetica', 10)) # instructions for user
canvas1.create_window(120, 180, window=instructions4) # show instructions

tax_val = IntVar()
yearly_tax = tk.Scale(ws, from_=2000, to=27000, orient=HORIZONTAL, variable=tax_val, showvalue=bool(0)) # create entry
canvas1.create_window(250, 180, window=yearly_tax) # shows entry in canvas
taxLabel = tk.Label(ws, textvariable=tax_val)
canvas1.create_window(325, 180, window= taxLabel)



ws.btn = tk.Button(ws, text = 'Enter', bd = '5', command= (lambda: create_loan())) # create button that runs welMsg
canvas1.create_window(200, 260, window=ws.btn) # show button
interest1 = tk.Entry(ws)


def create_canvas(): # define function
    canvas1.delete("all")  # delete everything in canvas

def create_loan():
    P = float(house_price.get()) - float(downpayment.get())
    months = 30 * 12
    rate = float(interest_rate.get())/100
    tax_yearly = float(yearly_tax.get())


    create_canvas()

    result2 = tk.Label(ws, text="Your monthly payment is:", font=('helvetica', 10))  # instructions for user
    canvas1.create_window(200, 140, window=result2)  # show instructions

    result2 = tk.Label(ws, text="$" + str(round((rate / 12) * (1 / (1 - (1 + rate / 12) ** (-months))) * P + (tax_yearly/12), 2)), font=('helvetica', 10))  # instructions for user
    canvas1.create_window(200, 160, window=result2)  # show instructions

ws.mainloop() # run tkinter event loop
