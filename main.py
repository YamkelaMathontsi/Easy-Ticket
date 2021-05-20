from tkinter import *
from tkinter import messagebox


class TicketSales(object):
    def __init__(self,root):

        self.root = root
        self.root.title("TicketSales")
        self.root.geometry("400x500")
        self.root.config(bg="grey")

        # Cell number label and entry
        self.cell_entry_lbl = Label(self.root, text="Enter Cell Number:", bg="green")
        self.cell_entry = Entry(self.root)
        self.cell_entry_lbl.place(x=10, y=10)
        self.cell_entry.place(x=220, y=10)

        # Type of ticket
        self.ticket_label = Label(self.root, text="Select Ticket Category:", bg="pink")
        self.options = ["Soccer", "Movie", "Theater"]
        self.variable = StringVar(self.root)
        self.variable.set("Select Ticket")
        self.ticket_menu = OptionMenu(root, self.variable, *self.options)
        self.ticket_label.place(x=10, y=50)
        self.ticket_menu.place(x=220, y=45)

        # Number of tickets
        self.ticket_no_label = Label(self.root, text="Number of Tickets Bought:", bg="aqua")
        self.ticket_spinbox = Spinbox(self.root, width=10, from_=0, to=100)
        self.ticket_no_label.place(x=10, y=90)
        self.ticket_spinbox.place(x=220, y=90)

        # Calculation button
        self.calc_button = Button(self.root, text='Calculate Ticket', bg="orange", command=self.calc_payment)
        self.clear_button = Button(self.root, text='Clear Entries', bg="orange", command=self.clear)
        self.calc_button.place(x=40, y=200)
        self.clear_button.place(x=250, y=200)

        # X Border
        self.border1 = Label(self.root, text="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", bg="gold")
        self.border2 = Label(self.root, text="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", bg="gold")
        self.border1.place(y=260)
        self.border2.place(y=450)

        # Results
        self.amount_pay = Label(self.root, text="", bg="#346ab3")
        self.reserve = Label(self.root, text="", bg="#346ab3")
        self.cell_label = Label(self.root, text="", bg="#346ab3")
        self.amount_pay.place(x=50, y=300)
        self.reserve.place(x=50, y=350)
        self.cell_label.place(x=50, y=400)

    # Calculations
    def calc_payment(self):
        ticket_no = int(self.ticket_spinbox.get())
        vat = 0.14
        try:
            int(self.cell_entry.get())
            if len(self.cell_entry.get()) < 10 or len(self.cell_entry.get()) > 10:
                raise ValueError

            elif self.variable.get() == "Select Ticket":
                raise ValueError

            elif int(self.ticket_spinbox.get()) == 0:
                raise ValueError

            # Soccer
            elif self.variable.get() == "Soccer":
                price = 40
                price_pay = (price * ticket_no) + (price * ticket_no * vat)
                text = ("Amount Payable: R{}".format(price_pay))
                self.amount_pay.config(text=text)

            # Movie
            elif self.variable.get() == "Movie":
                price = 75
                price_pay = (price * ticket_no) + (price * ticket_no * vat)
                text = ("Amount Payable: R{}".format(price_pay))
                self.amount_pay.config(text=text)

            # Theater
            elif self.variable.get() == "Theater":
                price = 100
                price_pay = (price * ticket_no) + (price * ticket_no * vat)
                text = ("Amount Payable: R{}".format(price_pay))
                self.amount_pay.config(text=text)

            # Reservation
            reserve_text = "Reservation for {} for : {} ".format(self.variable.get(), ticket_no)
            cell_text = "Reservation Made By: {}".format(self.cell_entry.get())
            self.reserve.config(text=reserve_text)
            self.cell_label.config(text=cell_text)

        except ValueError:  # Error Message
            messagebox.showerror(message="INVALID - Please Try Again")

    def clear(self):
        self.cell_entry.delete(0, END)
        self.cell_entry.focus()
        self.variable.set("Select Ticket")
        self.ticket_spinbox.delete(0, END)
        self.ticket_spinbox.insert(0, 0)
        self.amount_pay.config(text="")
        self.reserve.config(text="")
        self.cell_label.config(text="")


root = Tk()
TicketSales(root)
root.mainloop()
