#1 senior_price adult_price child_price
#2 if adult+child+senior >100 repeat while loop

class Tickets:
    def __init__(self, adult, child, senior):
        self.adult = adult
        self.child = child
        self.senior = senior

    def get_ticket(self, adult, child, senior):
        pass #adult = 0 
        
    def calculate(self):
        self.senior_price = 10
        self.child_price = 5
        self.adult_price = 15
        total = (self.senior_price + self.child_price + self.adult_price)
        return total

