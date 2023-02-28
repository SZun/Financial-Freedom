from dataclasses import dataclass

@dataclass
class Calculator:

    age: int
    yearly_income: float
    yearly_savings_rate: float
    current_contribution_401k: float
    match_percentage_401k: float
    portfolio_mix_401k: str
    portfolio_mix_ira: str
    primary_card_interest_rate: float
    primary_card_debt: float
    secondary_card_interest_rate: float
    secondary_card_debt: float
    expected_portfolio_returns =  {
                                    "7%": {"Equity": 20, "Fixed Income": 80, "ROI %":7}, 
                                    "8%": {"Equity": 40, "Fixed Income": 60, "ROI %":8},
                                    "9%": {"Equity": 60, "Fixed Income": 40, "ROI %":9},
                                    "10%": {"Equity": 80, "Fixed Income": 20, "ROI %":10},
                                    "11%": {"Equity": 100, "Fixed Income": 0, "ROI %":11}
                                     }


    # Caluclations:
    ## Calculate monthly savings (yearly_income * savings_rate) / 12
    ## Calculate taxes based on federal tax bracket and 401k contributions
    ## Caclulate cost of debt from credit card info
    def monthly_cost_of_debt (self):
        return ((self.primary_card_interest_rate*self.primary_card_debt) + (self.secondary_card_interest_rate*self.secondary_card_debt)) / 12 
        
    
    ## Expected Return vs Cost of Debt
    def money_allocation_advice (self):
        is_in_debt = ((self.primary_card_interest_rate + self.secondary_card_interest_rate)/2) > self.portfolio_recommendation["ROI %"]:
        return "Pay off credit card debt" if is_in_debt else "Invest money into your portfolio"


    # Money allocation:
    ## From savings reccomend money allocation (debt pay off and investment)
    
    ## Based on age reccomend portfolio mix
    def portfolio_recommendation (self):
        if self.age < 30: 
            return self.expected_portfolio_returns["11%"]
        elif self.age < 40:
            return self.expected_portfolio_returns["10%"]
        elif self.age < 50:
            return self.expected_portfolio_returns["9%"] 
        elif self.age < 60:
            return self.expected_portfolio_returns["8%"]
        elif self.age > 60:
            return self.expected_portfolio_returns["7%"]




    def get_projected_returns(self):
        return ["test"]

    def generate_reccommendation(self):
        return "Lorem ipsum dolor sit amet, consectetur adipiscing elit"