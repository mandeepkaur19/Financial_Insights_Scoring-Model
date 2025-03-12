# Importing libraries
import streamlit as st
import pandas as pd
import base64

# Financial Scoring Function
def calculate_financial_score(row):
    savings_to_income = row['Savings'] / row['Income'] if row['Income'] > 0 else 0
    expenses_ratio = row['Expenses'] / row['Income'] if row['Income'] > 0 else 0
    loan_ratio = row['LoanPayments'] / row['Income'] if row['Income'] > 0 else 0
    cc_ratio = row['CreditCardSpending'] / row['Income'] if row['Income'] > 0 else 0
    financial_goals_met = row['FinancialGoalsMet'] / 100  # Convert percentage to decimal
    te_amt = row['TravelEntertainment'] / row['Amount'] if row['Amount'] > 0 else 0

    score = 100
    score -= (1 - savings_to_income) * 25  # Higher savings are better
    score -= (1 - expenses_ratio) * 25  # Lower expenses are better
    score -= (1 - loan_ratio) * 20  # Lower loan payments are better
    score -= (1 - cc_ratio) * 15  # Penalize higher credit card spending
    score += financial_goals_met * 10  # Reward for achieving financial goals
    score -= (1 - te_amt) * 0.05  # Penalize high discretionary spending (TravelEntertainment/Amount)

    return max(0, min(100, score))  # Ensure score is between 0 and 100

# Streamlit App
def add_bg_image(image_file):
    with open(image_file, "rb") as img_file:
        encoded_string = base64.b64encode(img_file.read()).decode()
    bg_image = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{encoded_string}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>
    """
    st.markdown(bg_image, unsafe_allow_html=True)

# Add background image
add_bg_image("bg.png")
def main():
    
    # App title
    st.title("Financial Scoring App")

    st.subheader('Overview')
    st.write('Welcome to the Financial Scoring App! This app helps you calculate a financial score based on various financial parameters such as income, savings, expenses, loan payments, credit card spending, and more. By entering your financial details, you can assess how well you are managing your finances and make informed decisions to improve your financial health.')
    
    # Input fields for the user to enter financial data
    income = st.number_input("Income 💵", min_value=0, step=1000)
    savings = st.number_input("Savings 💰", min_value=0, step=100)
    expenses = st.number_input("Monthly Expenses 💸", min_value=0, step=100)
    loan_payments = st.number_input("Loan Payments 🏠", min_value=0, step=100)
    credit_card_spending = st.number_input("Credit Card Spending 💳", min_value=0, step=100)
    travel_entertainment = st.number_input("Travel & Entertainment Spending 🌍")
    amount = st.number_input("Total Amount Spent 🛍️", min_value=0, step=100)
    financial_goals_met = st.number_input("Financial Goals Met 🎯", min_value=0, max_value=100, step=1)

    # Button to calculate the score
    if st.button("Calculate Financial Score"):
        # Creating a DataFrame from the input data
        data = {
            'Income': income,
            'Savings': savings,
            'Expenses': expenses,
            'LoanPayments': loan_payments,
            'CreditCardSpending': credit_card_spending,
            'TravelEntertainment': travel_entertainment,
            'Amount': amount,
            'FinancialGoalsMet': financial_goals_met
        }
        
        # Calculate the financial score
        df = pd.DataFrame([data])
        df['Score'] = df.apply(calculate_financial_score, axis=1)

        # Display the result
        st.write("Financial Score Calculated:")
        st.write(df[['Income', 'Savings', 'Expenses', 'LoanPayments', 'CreditCardSpending', 'TravelEntertainment', 'Score']])

        # Show the calculated score
        st.subheader(f"Your Financial Score: {df['Score'].iloc[0]:.2f}")

# Run the Streamlit app
if __name__ == "__main__":
    main()

st.markdown("""
    ---
    <div style="text-align: center;">
        Created by Mandeep Kaur <br>
        🚀 <a href="https://www.linkedin.com/in/mandeepkaur19/" target="_blank">LinkedIn</a>
    </div>
""", unsafe_allow_html=True)
