import streamlit as st
from projection import Projector
from calculator import Calculator
from pathlib import Path
from PIL import Image

def get_formated_portfolio_mix(mix):
    mix = mix.split("/")
    return f"Stocks: {mix[0]}%, Bonds: {mix[1]}%"

st.write("# Financial Freedom")

with st.form("Your Financials"):
    st.write("## Your Financials")

    st.write("### Personal Information")
    age = st.text_input("Age")

    st.write("### Income/Savings")
    yearly_income = st.text_input("Yearly Income ($)")
    yearly_savings = st.text_input("Yearly Savings ($)")

    st.write("### 401k")
    balance_401k = st.text_input("401k Balance ($)")
    current_contribution_401k = st.text_input("Current Contribution (%)")
    match_percentage_401k = st.text_input("Employer Match (%)")

    st.write("### Portfolio Mix")
    portfolio_mix = st.selectbox("Stocks/Bonds", ["20/80","40/60","60/40","80/20","100/0"])

    st.write("### Credit Cards")
    st.write("##### Primary Card")
    primary_card_interest_rate = st.text_input("Primary Interest Rate (%)")
    primary_card_debt = st.text_input("Total Primary Debt ($)")
    st.write("##### Secondary Card")
    secondary_card_interest_rate = st.text_input("Secondary Interest Rate (%)")
    secondary_card_debt = st.text_input("Total Secondary Debt ($)")

    if st.form_submit_button("Submit"):
        if float(yearly_savings) > ((float(current_contribution_401k)/100) * float(yearly_income)):    
            try:
                calculator = Calculator(
                    int(age),
                    float(yearly_income),
                    float(yearly_savings),
                    float(balance_401k),
                    float(current_contribution_401k),
                    float(match_percentage_401k),
                    portfolio_mix,
                    float(primary_card_interest_rate),
                    float(primary_card_debt),
                    float(secondary_card_interest_rate),
                    float(secondary_card_debt)
                )

                calculator.initialize()
                            
                st.write("## Your Current Financials")
                
                st.write(f"Monthly Cost of Debt: ${calculator.get_starting_monthly_cost_of_debt()}")

                unadvised_ending_balnace,advised_ending_balnace = calculator.get_simplified_net_worth()
                
                st.write("### Without Advice")
                st.write(f"Yearly Ending Balance: ${unadvised_ending_balnace}")
                st.write(f"Current Debt: ${calculator.cc_debt}")
                st.write(f"Effective Tax Rate: {calculator.get_effective_tax_rate()}%")
                st.write(f"Monthly Cost of Debt: ${calculator.get_monthly_cost_of_debt()}")

                st.write("### With Advice")
                debt,invest = calculator.money_allocation.values()
                st.write("We reccomend that you:")
                if invest != 0:
                    st.write(f"- Invest ${invest} in your 401k")
                else:
                    st.write("- Since the interest rate on your card is higher than your expected portfolio return, we recccomend that you pay off your credit card debt first.")
                if debt != 0:
                    st.write(f"- Pay off ${debt} credit card debt")

                if portfolio_mix != calculator.get_portfolio_key():
                    
                    st.write(f"- Currently you have a portfolio mix of {get_formated_portfolio_mix(portfolio_mix)} and we reccomend you move to a portfolio mix of {get_formated_portfolio_mix(calculator.get_portfolio_key())}")

                st.write("### Projections With Advice")

                st.write(f"Yearly Ending Balance: ${advised_ending_balnace}")
                st.write(f"Final Debt: ${calculator.get_final_debt()}")
                st.write(f"Effective Tax Rate: {calculator.get_effective_tax_rate(True)}%")
                st.write(f"Monthly Cost of Debt: ${calculator.get_monthly_cost_of_debt(True)}")

                projector = Projector(calculator)
                projector.initialize()
                for image_path in projector.get_image_paths():
                    plot_image = Image.open(Path(image_path))
                    st.image(plot_image)

            except:
                st.error('Invalid Input', icon="🚨")
        else:
            st.error('401 K contribution cannot be higher than yearly savings.', icon="🚨")
