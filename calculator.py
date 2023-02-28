from dataclasses import dataclass

@dataclass
class Calculator:

    yearly_income: float
    yearly_savings: float
    current_contribution_401k: float
    match_percentage_401k: float
    portfolio_mix_401k: str
    portfolio_mix_ira: str
    primary_card_interest_rate: float
    primary_card_debt: float
    secondary_card_debt: float
    secondary_card_interest_rate: float

    def get_projected_returns(self):
        return ["test"]

    def generate_reccommendation(self):
        return "Lorem ipsum dolor sit amet, consectetur adipiscing elit"