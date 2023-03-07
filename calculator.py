from dataclasses import dataclass

@dataclass
class Calculator:

    age: int
    yearly_income: float
    yearly_savings: float
    balance_401k: float
    current_contribution_401k: float
    match_percentage_401k: float
    portfolio_mix: str
    primary_card_interest_rate: float
    primary_card_debt: float
    secondary_card_interest_rate: float
    secondary_card_debt: float
    cc_interest_rate = 0
    cc_debt = 0
    expected_portfolio_returns =    {
                                        "20/80": {"Equity": 20, "Fixed Income": 80, "ROI %":5.95}, 
                                        "40/60": {"Equity": 40, "Fixed Income": 60, "ROI %":6.57},
                                        "60/40": {"Equity": 60, "Fixed Income": 40, "ROI %":7.64},
                                        "80/20": {"Equity": 80, "Fixed Income": 20, "ROI %":8.72},
                                        "100/0": {"Equity": 100, "Fixed Income": 0, "ROI %":9.79}
                                    }
    money_allocation = {"Debt": 0, "Invest": 0}

    def init(self):
        self.set_total_cc_interest_rate()
        self.set_cc_debt()
        self.set_money_allocation()
        self.set_total_investing_capital()

    def set_total_cc_interest_rate(self):
        self.cc_interest_rate = (self.primary_card_interest_rate + self.secondary_card_interest_rate)/2

    def set_cc_debt (self):
        self.cc_debt = self.primary_card_debt + self.secondary_card_debt

    def set_money_allocation(self):
        if self.cc_interest_rate > self.expected_portfolio_returns[self.portfolio_mix]["ROI %"]:
            if self.cc_debt > self.yearly_savings:
                self.money_allocation["Debt"] = self.yearly_savings
            else:
                self.money_allocation["Debt"] = self.cc_debt
                self.money_allocation["Invest"] = self.yearly_savings - self.cc_debt

        else:
            self.money_allocation["Invest"] = self.yearly_savings
        return self.money_allocation
    
    def set_total_investing_capital(self):
        employer_match = self.get_employer_match()
        investing_capital = self.money_allocation["Invest"]
        if investing_capital >= employer_match:
            self.money_allocation["Invest"] += employer_match 
 
    def get_tax_amount(self, is_advised =False):
        income_after_contribution = self.yearly_income - self.money_allocation["Invest"] if is_advised else (self.current_contribution_401k/100) * self.yearly_income
        if income_after_contribution < 11_001:
            return 0.1 * income_after_contribution 
        elif income_after_contribution >= 11_001 and income_after_contribution < 44_726:
            return (0.1 * 11_000) + (0.12 * (income_after_contribution - 11_000))
        elif income_after_contribution >= 44_726 and income_after_contribution < 95_376:
            return (0.1 * 11_000) + (0.12 * 33_725) + (0.22 * (income_after_contribution - 44_725))
        elif income_after_contribution >= 95_376 and income_after_contribution < 182_101:
            return (0.1 * 11_000) + (0.12 * 33_725) + (0.22 * 50_650) + (0.24 * (income_after_contribution - 95_375))
        elif income_after_contribution >= 182_101 and income_after_contribution < 231_251:
            return (0.1 * 11_000) + (0.12 * 33_725) + (0.22 * 50_650) + (0.24 * 86_725) + (0.32 * (income_after_contribution - 182_100))
        elif income_after_contribution >= 231_251 and income_after_contribution < 578_126:
            return (0.1 * 11_000) + (0.12 * 33_725) + (0.22 * 50_650) + (0.24 * 86_725) + (0.32 * 49_150) + (0.35 * (income_after_contribution - 231_250))
        
        return (0.1 * 11_000) + (0.12 * 33_725) + (0.22 * 50_650) + (0.24 * 86_725) + (0.32 * 49_150) + (0.35 * 346_875) + (0.37 * (income_after_contribution - 578_125))



    def get_effective_tax_rate(self, is_advised=False):
        return (self.get_tax_amount(is_advised) / (self.yearly_income))  *100

    def get_employer_match(self):
        return self.yearly_income * (self.match_percentage_401k / 100)

    def get_starting_monthly_cost_of_debt(self):
        primary_card_debt = (self.primary_card_interest_rate/100)*self.primary_card_debt
        secondary_card_debt = (self.secondary_card_interest_rate/100)*self.secondary_card_debt
        return round(primary_card_debt + secondary_card_debt / 12,2) 
 
    def get_final_debt(self, is_advised=False):
        return round(self.cc_debt - self.money_allocation["Debt"] if is_advised else 0,2)
    
    def get_monthly_cost_of_debt(self, is_advised=False):
        return round((self.get_final_debt(is_advised)*(self.cc_interest_rate/100))/12,2)
    
    def get_portfolio_key (self):
        keys = list(self.expected_portfolio_returns.keys())
        index = 0 

        if self.age < 30: 
            index = 4
        elif self.age < 40:
            index = 3
        elif self.age < 50:
            index = 2
        elif self.age < 60:
            index = 1

        return keys[index]


    def get_portfolio_ending_balance(self, is_advised=False):
        additional_contribution = self.money_allocation["Invest"] if is_advised else (self.current_contribution_401k/100) * self.yearly_income
        total_401k_balance = self.balance_401k + additional_contribution  
        mix = self.get_portfolio_key() if is_advised else self.portfolio_mix
        roi = 1 + (self.expected_portfolio_returns[mix]["ROI %"] / 100)
        
        return round(roi * total_401k_balance,2)
    
    def get_simplified_net_worth(self):
        unadvised_ending_balnace = self.get_portfolio_ending_balance() - self.get_final_debt()
        advised_ending_balnace = self.get_portfolio_ending_balance(True) - self.get_final_debt()
        return [unadvised_ending_balnace,advised_ending_balnace]


    def get_projected_returns(self):
        return ["test"]

    def generate_reccommendation(self):
        return "Lorem ipsum dolor sit amet, consectetur adipiscing elit"