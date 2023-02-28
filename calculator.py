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
    


    # Caluclations:
    ## Calculate monthly savings (yearly_income * savings_rate) / 12
    ## Calculate taxes based on federal tax bracket and 401k contributions
    ## Caclulate cost of debt from credit card info
     
    # Money allocation:
    ## From savings reccomend money allocation (debt pay off and investment)
    ## Based on age reccomend portfolio mix


    def get_projected_returns(self):
        return ["test"]

    def generate_reccommendation(self):
        return "Lorem ipsum dolor sit amet, consectetur adipiscing elit"