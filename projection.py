from dataclasses import dataclass

@dataclass
class Projector:

    primary_card_interest_rate: float
    primary_card_debt: float
    secondary_card_debt: float
    secondary_card_interest_rate: float
    projected_returns: list