class ROI:
    
    
    def income(self):  
        rental = int(input("What is the total rental income? "))
        laundry = int(input("What is the total laundry income? "))
        storages = int(input("What is the total storage income? "))
        misc = int(input("Are there any misc incomes and what is the total of those costs? "))
        self.total_income = rental + laundry + storages + misc
        print(f"The total income per month from your unit will be {self.total_income}.")
    


    def expenses(self):
        tax = int(input("What is the total of the taxes paid on the unit? "))
        insurance = int(input("What is the total cost of insurance? "))
        utilities = int(input("What utilities do you have and how much do they cost? "))
        hoa = int(input("What is the total of the HOA costs? "))
        lawn = int(input("How much is lawn/snow care? "))
        vacancy = int(input("How much would you like to put away for vacany purposes per month? "))
        repairs = int(input("What is the total cost of repairs? "))
        capex = int(input("What is the total capex? "))
        property_management = int(input("What is the total cost of property management fees? "))
        morgage =  int(input("How much is the morgage per month? "))
        self.total_expenses = tax + insurance + utilities + hoa + lawn + vacancy + repairs + capex + property_management + morgage
        print(f"The total expenses per month from your unit will be {self.total_expenses}.")



    def cash_flow(self):
        self.total_cash_flow = self.total_income - self.total_expenses
        print(f"The total cash flow from your unit will be {self.total_cash_flow}.")



    def cash_on_cash(self):
        downpayment = int(input("What is the total downpayment? "))
        closing_cost = int(input("What is the total closing cost? "))
        repair_budget = int(input("What is the total repair budget? "))
        misc_cost = int(input("What are the total misc costs if any? "))
        total_cash_on_cash = downpayment + closing_cost + repair_budget + misc_cost
        total_investment = self.total_cash_flow / total_cash_on_cash
        print(f"Total ROI: {100 * total_investment:.2f}%")
    
roi = ROI()

roi.income()
roi.expenses()
roi.cash_flow()
roi.cash_on_cash()
