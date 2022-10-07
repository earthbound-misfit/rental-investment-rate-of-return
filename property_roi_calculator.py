class PropertyROI():
    def __init__(self, income=0, expenses=0, investment=0, cash_flow=0, rate_of_return=0):
        self.income = income
        self.expenses = expenses
        self.investment = investment
        self.cash_flow = cash_flow
        self.rate_of_return = rate_of_return

    def monthly_income(self):
        self.income += float(input('What is the monthly rental income? '))
        self.income += float(input('Enter dollar amount for any additional income (i.e. laundry, storage): '))
        print('Your total monthly income is: {:0.2f}'.format(self.income))
        return self.income

    def monthly_expenses(self):
        self.expenses += float(input('What is the monthly mortgage? '))
        self.expenses += float(input('What is the monthly taxes? '))
        self.expenses += float(input('What is the monthly insurance? '))
        self.expenses += float(input('What is the monthly utilities (if none, enter 0)? '))
        self.expenses += float(input('How much would you like to set aside for repairs each month? '))
        self.expenses += float(input('How much would you like to set aside each month in case of vacancy? '))
        self.expenses += float(input('What is the monthly HOA (if none, enter 0)? '))
        self.expenses += float(input('How much would you like to set aside each month for capital expenditures? '))
        self.expenses += float(input('How much do you pay a property manager each month (if none, enter 0)? '))
        print('Your total monthly expenses are: {:0.2f}'.format(self.expenses))
        return self.expenses

    def total_investment(self):
        self.investment += float(input('What is your down payment? '))
        self.investment += float(input('What are your total closing costs? '))
        self.investment += float(input('What is the estimate cost to rehab? '))
        return self.investment

    def annual_cash_flow(self):
        return (self.income - self.expenses) * 12
        
    def cash_on_cash_roi(self):
        rate = (self.cash_flow / self.investment) * 100
        print('Your cash on cash rate of return is {:0.2f}%'.format(rate))
        return rate

def Calculate(self):
    
    while True:
        user_input = input('What would you like to do?\nEnter "c" to calculate your rate of return on a property.\nOr enter "q" to quit: ')

        if user_input.lower() == 'q':
            print('Have a great day!')
            break
        elif user_input.lower() == 'c':
            print("Please enter all input in numbers; if none, enter 0: ")
            self.income = float(self.monthly_income())
            self.expenses = float(self.monthly_expenses())
            self.investment = float(self.total_investment())
            self.cash_flow = float(self.annual_cash_flow())
            self.rate_of_return = float(self.cash_on_cash_roi())
        else:
            print('Invalid input, please enter a valid option.')
            Calculate(self)

property1 = PropertyROI()

Calculate(property1)