import streamlit as st
from calculator import Calculator

st.write("# Next Dollar")

with st.form("Your Financials"):
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

    if st.form_submit_button("Submit"):

        try:
            calculator = Calculator(
            float(match_percentage_401k),
            float(stocks_401k),
            float(bonds_401k),
            float(expected_ira_return),
            float(stocks_ira),
            float(bonds_ira),
            float(primary_card_interest_rate),
            float(primary_card_debt),
            float(secondary_card_interest_rate),
            float(secondary_card_debt)
        )

            st.write("## Your Reccomendation")
            st.write(calculator.generate_reccommendation())
        except:
            st.error('Invalid Input', icon="🚨")