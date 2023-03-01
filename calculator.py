from dataclasses import dataclass

@dataclass
class Calculator:

    age: int
    yearly_income: float
    yearly_savings: float
    current_contribution_401k: float
    match_percentage_401k: float
    portfolio_mix_401k: str
    portfolio_mix_ira: str
    primary_card_interest_rate: float
    primary_card_debt: float
    secondary_card_interest_rate: float
    secondary_card_debt: float
    cc_interest_rate = 0
    expected_portfolio_returns =  {
                                    "20_80": {"Equity": 20, "Fixed Income": 80, "ROI %":7}, 
                                    "40_60": {"Equity": 40, "Fixed Income": 60, "ROI %":8},
                                    "60_40": {"Equity": 60, "Fixed Income": 40, "ROI %":9},
                                    "80_20": {"Equity": 80, "Fixed Income": 20, "ROI %":10},
                                    "100_0": {"Equity": 100, "Fixed Income": 0, "ROI %":11}
                                     }
    
    def init(self):
        tax_amount = self.get_tax_amount()

   
    def get_tax_amount(self):

        if self.yearly_income < 11_001 :
            return 0.1 * self.yearly_income 
        elif self.yearly_income >= 11_001 and self.yearly_income < 44_726 :
            return (0.1 * 11_000) + (0.12 * (self.yearly_income - 11_000))
        elif self.yearly_income >= 44_726 and self.yearly_income < 95_376:
            return (0.1 * 11_000) + (0.12 * 33_725) + (0.22 * (self.yearly_income - 44_725))
        elif self.yearly_income >= 95_376 and self.yearly_income < 182_101:
            return (0.1 * 11_000) + (0.12 * 33_725) + (0.22 * 50_650) + (0.24 * (self.yearly_income - 95_375))
        elif self.yearly_income >= 182_101 and self.yearly_income < 231_251:
            return (0.1 * 11_000) + (0.12 * 33_725) + (0.22 * 50_650) + (0.24 * 86_725) + (0.32 * (self.yearly_income - 182_100))
        elif self.yearly_income >= 231_251 and self.yearly_income < 578_126:
            return (0.1 * 11_000) + (0.12 * 33_725) + (0.22 * 50_650) + (0.24 * 86_725) + (0.32 * 49_150) + (0.35 * (self.yearly_income - 231_250))
        else :
            return (0.1 * 11_000) + (0.12 * 33_725) + (0.22 * 50_650) + (0.24 * 86_725) + (0.32 * 49_150) + (0.35 * 346_875) + (0.37 * (self.yearly_income - 578_125))

    def get_effective_tax_rate(self):
        return (self.get_tax_amount() / self.yearly_income) * 100




    def get_monthly_cost_of_debt(self):
        return ((self.primary_card_interest_rate*self.primary_card_debt) + (self.secondary_card_interest_rate*self.secondary_card_debt)) / 12 
        
    
    def set_total_cc_interest_rate(self):
        self.cc_interest_rate = (self.primary_card_interest_rate + self.secondary_card_interest_rate)/2


    def get_money_allocation(self):
        res = {"Debt" : 0, "Invest" : 0}
        if self.cc_interest_rate > self.portfolio_recommendation["ROI %"]:
            cc_debt = self.primary_card_debt + self.secondary_card_debt
            if cc_debt > self.yearly_savings:
                res["Debt"] = self.yearly_savings
            else :
                res["Debt"] = cc_debt
                res["Invest"] = self.yearly_savings - cc_debt

        else:
            res["Invest"] = self.yearly_savings
        return res
 

    def get_portfolio_recommendation (self):
        if self.age < 30: 
            return self.expected_portfolio_returns["100_0"]
        elif self.age < 40:
            return self.expected_portfolio_returns["80_20"]
        elif self.age < 50:
            return self.expected_portfolio_returns["60_40"] 
        elif self.age < 60:
            return self.expected_portfolio_returns["40_60"]
        else :
            return self.expected_portfolio_returns["20_80"]




    def get_projected_returns(self):
        return ["test"]

    def generate_reccommendation(self):
        return "Lorem ipsum dolor sit amet, consectetur adipiscing elit"