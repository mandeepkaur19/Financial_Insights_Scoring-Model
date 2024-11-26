# Financial Insights Dashboard and Scoring Model

This project implements a **Financial Insights Dashboard and Scoring Model** to analyze financial data, assess financial health, and provide actionable insights.

---

## Features

- **Data Analysis**:
  - Identify family-level and member-level spending patterns.
  - Understand correlations between financial metrics (e.g., income vs. expenses, savings vs. spending habits).
  
- **Financial Scoring Model**:
  - Calculates a score (range: 0–100) based on financial parameters.
  - Factors:
    - Savings-to-Income Ratio
    - Monthly Expenses as a percentage of Income
    - Loan Payments as a percentage of Income
    - Credit Card Spending trends
    - Spending category distribution
    - Financial Goals Met (%)

- **Visualization**:
  - Spending distribution across categories.
  - Family-wise financial scores.
  - Member-wise spending trends.

- **API Deployment**:
  - Deployed using **Flask**.
  - Input: Family financial and transaction data (JSON format).
  - Output: Financial score and insights.

- **Interactive Dashboard**:
  - Built using **Streamlit** for a user-friendly experience.

---

## Prerequisites

Make sure you have the following installed on your machine:

1. **Python 3.7+**
2. **pip** for managing Python packages

### Required Python Packages

Install the following dependencies:

```bash
pip install flask streamlit pandas matplotlib seaborn plotly
```

---

## Project Setup

1. **Clone the Repositor**:
2. ```bash
   git clone https://github.com/yourusername/financial-scoring-app.git
   cd financial-scoring-app
   ```
3. Set Up Virtual Environment
   ```bash
    python -m venv env
    source env/bin/activate  # On Windows: env\Scripts\activate
4. Run the Flask API: Start the Flask server
```bash
 python financial_scoring_api.py
```
5.Run the Streamlit App: Start the Streamlit server
```bash
streamlit run financial_scoring_app.py
```

---

## Testing the API with Postman
1.**Install Postman**:
  * Download and install Postman from Postman Official Website.
2. **Setup a POST Request**:
    * URL: http://127.0.0.1:5000/get_financial_score
    * Method: POST
    * Headers: Set Content-Type to application/json
3. **Sample JSON Input**:
```bash
{
  "Income": 50000,
  "Savings": 15000,
  "Expenses": 20000,
  "LoanPayments": 5000,
  "CreditCardSpending": 3000,
  "TravelEntertainment": 1000,
  "Amount": 25000,
  "FinancialGoalsMet": 80
}
```
4. **Send Request**: Click "Send" to test the API.

5. **Sample JSON Response**:
   ```bash
   {
    "Income": 50000,
    "Savings": 15000,
    "Expenses": 20000,
    "LoanPayments": 5000,
    "CreditCardSpending": 3000,
    "TravelEntertainment": 1000,
    "Amount": 25000,
    "FinancialGoalsMet": 80,
    "Score": 75.4
    }
   ```

---

## Visualizations
 1. **Spending Patterns**:
   * Visualize expense distribution across categories like travel and entertainment.
 2. **Family Scores**:                                                                                                                                            
   * Analyze family-wise financial scores.
 4. **Member Insights**:
   * Explore individual member spending trends.

---
