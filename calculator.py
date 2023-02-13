from dataclasses import dataclass

@dataclass
class Calculator:

    match_percentage_401k: float
    stocks_401k: float
    bonds_401k: float
    expected_ira_return: float
    stocks_401k: float
    bonds_ira: float
    primary_card_interest_rate: float
    primary_card_debt: float
    secondary_card_debt: float
    secondary_card_interest_rate: float

    def generate_reccommendation(self):
        return "Lorem ipsum dolor sit amet, consectetur adipiscing elit"