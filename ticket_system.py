import tkinter as tk
from tkinter import messagebox

class Ticket:
    def __init__(self, price, quantity=0):
        self.price = price
        self.quantity = quantity

    def calc_subtotal(self):
        return self.price * self.quantity

class TicketBookingSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Ticket Booking System")

        # Ticket prices
        self.adult_ticket = Ticket(price=15)
        self.child_ticket = Ticket(price=5)
        self.student_ticket = Ticket(price=10)

        self.create_widgets()

    def create_widgets(self):
        #labels and entry boxes for ticket amounts
        tk.Label(self.root, text="Adult Tickets ($15 each):").grid(row=0, column=0, padx=10, pady=5)
        self.adult_quantity = tk.Entry(self.root)
        self.adult_quantity.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Child Tickets ($5 each):").grid(row=1, column=0, padx=10, pady=5)
        self.child_quantity = tk.Entry(self.root)
        self.child_quantity.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Student/Senior Tickets ($10 each):").grid(row=2, column=0, padx=10, pady=5)
        self.student_quantity = tk.Entry(self.root)
        self.student_quantity.grid(row=2, column=1, padx=10, pady=5)

        #Button to calculate total
        self.calculate_button = tk.Button(self.root, text="Calculate Total", command=self.calculate_total)
        self.calculate_button.grid(row=3, columnspan=2, pady=10)

        self.total_label = tk.Label(self.root, text="Total: $0")
        self.total_label.grid(row=4, columnspan=2, pady=5)

        self.error_label = tk.Label(self.root, text="", fg="red")
        self.error_label.grid(row=5, columnspan=2, pady=5)

    def calculate_total(self):
        self.error_label.config(text="")

        adult_qty_valid, adult_qty_error = self.validate_input(self.adult_quantity.get(), "Adult")
        child_qty_valid, child_qty_error = self.validate_input(self.child_quantity.get(), "Child")
        student_qty_valid, student_qty_error = self.validate_input(self.student_quantity.get(), "Student/Senior")

        if not adult_qty_valid:
            self.error_label.config(text=adult_qty_error)
            return
        if not child_qty_valid:
            self.error_label.config(text=child_qty_error)
            return
        if not student_qty_valid:
            self.error_label.config(text=student_qty_error)
            return

        adult_qty = int(self.adult_quantity.get())
        child_qty = int(self.child_quantity.get())
        student_qty = int(self.student_quantity.get())

        #Check total number of tickets
        total_tickets = adult_qty + child_qty + student_qty
        if total_tickets > 100:
            self.error_label.config(text="Total number of tickets exceeds 100")
            return

        self.adult_ticket.quantity = adult_qty
        self.child_ticket.quantity = child_qty
        self.student_ticket.quantity = student_qty

        #calculate
        total_price = (self.adult_ticket.calc_subtotal() + 
                       self.child_ticket.calc_subtotal() + 
                       self.student_ticket.calc_subtotal())

        #display total
        self.total_label.config(text=f"Total: ${total_price}")

    def validate_input(self, value, ticket_type):
        if not value.isdigit():
            return False, f"{ticket_type} ticket quantity must be an integer"
        qty = int(value)
        if qty < 0 or qty > 100:
            return False, f"{ticket_type} ticket quantity must be between 0 and 100"
        return True, ""

if __name__ == "__main__":
    root = tk.Tk()
    app = TicketBookingSystem(root)
    root.mainloop()