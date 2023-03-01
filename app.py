import streamlit as st
from projection import Projector
from calculator import Calculator

def get_reccomendation():
    return "Lorem ipsum dolor sit amet, consectetur adipiscing elit"

st.write("# Financial Freedom")

with st.form("Your Financials"):
    st.write("## Your Financials")

    st.write("### Personal Information")
    age = st.text_input("Age")

    st.write("### Income/Savings")
    yearly_income = st.text_input("Yearly Income")
    yearly_savings = st.text_input("Yearly Savings")

    st.write("### 401k")
    balance_401k = st.text_input("401k Balance")
    current_contribution_401k = st.text_input("Current Contribution %")
    match_percentage_401k = st.text_input("Employer Match %")

    st.write("### Portfolio Mix")
    portfolio_mix = st.selectbox("Stocks/Bonds", ["20/80","40/60","60/40","80/20","100/0"])

    st.write("### Credit Cards")
    st.write("##### Primary Card")
    primary_card_interest_rate = st.text_input("Primary Interest Rate")
    primary_card_debt = st.text_input("Total Primary Debt")
    st.write("##### Secondary Card")
    secondary_card_interest_rate = st.text_input("Secondary Interest Rate")
    secondary_card_debt = st.text_input("Total Secondary Debt")

    if st.form_submit_button("Submit"):

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

            projected_returns = calculator.get_projected_returns()

            projector = Projector(
                float(primary_card_interest_rate),
                float(primary_card_debt),
                float(secondary_card_interest_rate),
                float(secondary_card_debt),
                projected_returns
            )

            st.write("## Your Reccomendation")
            st.write(get_reccomendation())
        except:
            st.error('Invalid Input', icon="🚨")

