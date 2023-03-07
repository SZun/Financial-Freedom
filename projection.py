import pandas as pd
import numpy as np
import os
from dataclasses import dataclass
from calculator import Calculator
from pathlib import Path
from plotnine import ggplot, geom_line, labs, aes

@dataclass
class Projector:

    calc: Calculator
    debt = 0
    portfolio_balance = 0
    df = pd.DataFrame(
        {
            "Simplified Net Worth": np.nan,
            "Year-End Debt": np.nan,
            "Investing Capital": np.nan,
            "Ending 401k Balance": np.nan,
            "Year": range(1,6)
        }
    )

    def initialize(self):
        self.debt = self.calc.get_final_debt(True) 
        self.portfolio_balance = self.calc.get_portfolio_ending_balance(True)
        self.get_data()


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
        investment_capital = self.calc.money_allocation["Invest"]
        self.calc.cc_debt = self.debt 
        self.debt =  self.calc.get_final_debt(True)

        if self.debt < 0:
            temp_debt = self.debt*-1
            self.debt = 0
            return [0, temp_debt+investment_capital]

        return [self.debt, investment_capital]

    def get_next_portfolio_ending_balance(self):
        self.calc.balance_401k = self.portfolio_balance
        self.portfolio_balance = self.calc.get_portfolio_ending_balance(True)

        return self.portfolio_balance
    
    def get_next_simplified_net_worth(self):
        return self.calc.get_simplified_net_worth()[1]

    def get_save_line_plot(self, y_value):
        plot = (
            ggplot(self.df, aes(x='Year', y=y_value))
            + geom_line()
            + labs(x='Year', y=y_value, title=f"Projected {y_value} Over The Next 5 Years")
        )

        path = Path(f"./assets/images/plots/{y_value.replace(' ', '_')}.png")

        if path.is_file():
            os.remove(path)

        plot.save(path)

        return path
    
    def get_image_paths(self):
        paths = []

        for i in self.df.columns.values[:-1]:
            paths.append(self.get_save_line_plot(i))

        return paths

