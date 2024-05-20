class Tickets:
    def __init__(self, price, quantity=0): 
        self.price = price
        self.quantity = quantity 
        
    def calc_subtotal(self): 
        return self.price * self.quantity
    
import tkinter as tk
from tkinter import messagebox
class TicketBookingSystem:
    def __init__(self, root):
        self.root = root 
        self.root.title("Ticket Booking System") 
        #Ticket prices 
        self.adult_ticket = Tickets(price=15) 
        self.child_ticket = Tickets(price=5)
        self.student_ticket = Tickets(price=10) 
        #GUI elements 
        self.create_widgets()
    def create_widgets(self):
        tk.Label(self.root, text="Adult Tickets ($15 each):").grid(row=0, column=0) 
        self.adult_quantity = tk.Entry(self.root) 
        self.adult_quantity.grid(row=0, column=1) 
        tk.Label(self.root, text="Child Tickets ($5 each):").grid(row=1, column=0) 
        self.child_quantity = tk.Entry(self.root) 
        self.child_quantity.grid(row=1, column=1) 
        tk.Label(self.root, text="Student/Senior Tickets ($10 each):").grid(row=2, column=0)
        self.student_quantity = tk.Entry(self.root)
        self.student_quantity.grid(row=2, column=1)
        self.calculate_button = tk.Button(self.root, text="Calculate Total", command=self.calculate_total)
        self.calculate_button.grid(row=3, columnspan=2)
        self.total_label = tk.Label(self.root, text="Total: $0")
        self.total_label.grid(row=4, columnspan=2)
    def calculate_total(self):
        pass
        #try:self.adult_ticket.quantity = int(self.adult_quantity.get())
        #self.child_ticket.quantity = int(self.child_quantity.get())
        #self.student_ticket.quantity = int(self.student_quantity.get())
        #total_tickets = (self.adult_ticket.quantity + self.child_ticket.quantity + self.student_ticket.quantity) 
        #if total_tickets > 100: raise ValueError("Total number of tickets exceeds 100")
        #total_price = (self.adult_ticket.calc_subtotal() + self.child_ticket.calc_subtotal() + self.student_ticket.calc_subtotal())
        #self.total_label.config(text=f"Total: ${total_price}")
        #except ValueError as e: messagebox.showerror("Input Error", str(e)) 
        
        
        
        
if __name__ == "__main__": 
    root = tk.Tk()
app = TicketBookingSystem(root) 
root.mainloop()