from dataclasses import dataclass
from calculator import Calculator
import pandas as pd
from plotnine import ggplot
import numpy as np
import datetime

@dataclass
class Projector:

    calc= Calculator(25, 200000, 20000, 100000, 5, 5, "20/80", 15, 5000, 15, 5000)
    debt = 0
    portfolio_balance = 0
    df = pd.DataFrame(
        {
            "Simplified Net Worth": np.nan,
            "Year-End Debt": np.nan,
            "Investing Capital": np.nan,
            "Ending 401k Balance": np.nan
        }, index=range(1,6))

    def init(self):
        self.debt = self.calc.get_final_debt(True) 
        self.portfolio_balance = self.calc.get_portfolio_ending_balance(True)


    def get_data(self):
        row = 0
        self.df.iloc[row,0] = self.calc.get_simplified_net_worth()[1]
        self.df.iloc[row,1] = self.debt
        self.df.iloc[row,2] = self.calc.money_allocation["Invest"]
        self.df.iloc[row,3] = self.portfolio_balance
        
        for i in range(4):
            row += 1
            self.df.iloc[row, 1] = self.get_next_final_debt()[0]
            self.df.iloc[row, 2] = self.get_next_final_debt()[1]
            self.df.iloc[row, 3] = self.get_next_portfolio_ending_balance()
            self.df.iloc[row, 0] = self.get_next_simplified_net_worth()
        

    def get_next_final_debt(self):
        cc_debt = self.calc.cc_debt
        if cc_debt < 0:
            self.debt = 0
            return [self.debt, (cc_debt * -1) + self.calc.money_allocation["Invest"]]
        else:
            self.calc.cc_debt = self.debt 
            self.debt =  self.calc.get_final_debt(True)
            return [self.debt, 0]

    def get_next_portfolio_ending_balance(self):
        self.calc.balance_401k = self.portfolio_balance
        self.portfolio_balance = self.calc.get_portfolio_ending_balance(True)
        return self.portfolio_balance
    
    def get_next_simplified_net_worth(self):
        return self.calc.get_simplified_net_worth()[1]

    def check(self):
        self.calc.init()
        self.init()
        self.get_data()
        print(self.df)

