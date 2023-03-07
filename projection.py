from dataclasses import dataclass
from calculator import Calculator
import pandas as pd
from plotnine import ggplot
import numpy as np
import datetime

@dataclass
class Projector:

    calc: Calculator
    debt = 0
    portfolio_balance = 0
    df = pd.DataFrame({"Simplified Net Worth":np.nan, "Year-End Debt":np.nan, "Ending 401k Balance":np.nan}, index=range(1,6))

    def init(self):
        self.debt = self.calc.get_final_debt(True) 
        self.portfolio_balance = self.calc.get_portfolio_ending_balance(True)


    def get_data(self):
        self.df.iloc[1,0] = self.calc.get_simplified_net_worth()[1]
        self.df.iloc[1,1] = self.debt
        self.df.iloc[1,2] = self.portfolio_balance
        row = 1
        for i in range(4):
            row += 1
            self.df.iloc[row, 1] = self.get_next_final_debt()
            self.df.iloc[row, 2] = self.get_next_portfolio_ending_balance()
            self.df.iloc[row, 0] = self.get_next_simplified_net_worth()
        

    def get_next_final_debt(self):
        self.calc.cc_debt = self.debt 
        self.debt =  self.calc.get_final_debt(True)
        return self.debt

    def get_next_portfolio_ending_balance(self):
        self.calc.balance_401k = self.portfolio_balance
        self.portfolio_balance = self.calc.get_portfolio_ending_balance(True)
        return self.portfolio_balance
    
    def get_next_simplified_net_worth(self):
        return self.calc.get_simplified_net_worth()[1]
