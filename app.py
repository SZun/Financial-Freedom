import streamlit as st
from calculator import Calculator

st.write("# TBD")

st.write("## Your Financials")

st.write("### 401k")
match_percentage_401k = st.text_input("Employer Match %")
st.write("#### Portfolio Mix")
st.write("##### Stocks")
stocks_401k = st.text_input("401k Stock %")
st.write("##### Bonds")
bonds_401k = st.text_input("401k Bonds %")


st.write("### IRA")
expected_ira_return = st.text_input("Expected Yearly Return")
st.write("#### Portfolio Mix")
st.write("##### Stocks")
stocks_ira = st.text_input("IRA Stock %")
st.write("##### Bonds")
bonds_ira = st.text_input("IRA Bonds %")

st.write("### Credit Cards")
st.write("##### Primary Card")
primary_card_interest_rate = st.text_input("Primary Interest Rate")
primary_card_debt = st.text_input("Total Primary Debt")
st.write("##### Secondary Card")
secondary_card_interest_rate = st.text_input("Secondary Interest Rate")
secondary_card_debt = st.text_input("Total Secondary Debt")

if st.button("Submit"):
    calculator = Calculator(
        match_percentage_401k,
        stocks_401k,
        bonds_401k,
        expected_ira_return,
        stocks_ira,
        bonds_ira,
        primary_card_interest_rate,
        primary_card_debt,
        secondary_card_interest_rate,
        secondary_card_debt
    )

    calculator.generate_reccommendation()
