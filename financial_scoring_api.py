from flask import Flask, request, jsonify
import pandas as pd
import os

# Initialize Flask app
app = Flask(__name__)

# File path to the dataset
file_path = r"D:\Internship\Data Science Assign Submission\family_financial_and_transactions_data.csv"

# Load and preprocess the dataset
def preprocess_data():
    try:
        # Check if file exists
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found at {file_path}")
        
        # Load the CSV file
        data = pd.read_csv(file_path)
        data.fillna(0, inplace=True)  # Handle missing values
        return data
    except Exception as e:
        raise Exception(f"Error loading or processing the file: {str(e)}")

# Financial Scoring Function
def calculate_financial_score(row):
    savings_to_income = row['Savings'] / row['Income'] if row['Income'] > 0 else 0
    expenses_ratio = row['Expenses'] / row['Income'] if row['Income'] > 0 else 0
    loan_ratio = row['LoanPayments'] / row['Income'] if row['Income'] > 0 else 0
    cc_ratio = row['CreditCardSpending'] / row['Income'] if row['Income'] > 0 else 0
    financial_goals_met = row['FinancialGoalsMet'] /100
    te_amt = row['TravelEntertainment'] / row['Amount']
    
    score = 100
    score -= (1 - savings_to_income) * 25  # Higher savings are better
    score -= (1 -expenses_ratio) * 25  # Lower expenses are better
    score -= (1 -loan_ratio) * 20  # Lower loan payments are better
    score -= (1 -cc_ratio) * 15
    score += financial_goals_met * 10
    score -= (1-te_amt) * 0.05 # High discretionary spending is penalized

    return max(0, min(100, score))  # Ensure score is between 0 and 100

# API endpoint to calculate financial score
@app.route('/get_financial_score', methods=['POST'])
def get_financial_score():
    try:
        family_data = request.json
        family_df = pd.DataFrame([family_data])

        # List of required fields
        required_columns = ['Income', 'Savings', 'Expenses', 'LoanPayments','CreditCardSpending', 'TravelEntertainment','Amount','FinancialGoalsMet']
        
        # Check if all required fields are present
        for col in required_columns:
            if col not in family_data:
                return jsonify({"error": f"Missing required field: {col}"}), 400

        # Calculate the score
        family_df['Score'] = family_df.apply(calculate_financial_score, axis=1)
        
        # Convert the DataFrame to a dictionary
        response = family_df.to_dict(orient='records')[0]
        return jsonify(response), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Health check route
@app.route('/')
def home():
    return "Financial Scoring API is running!"

# Run the Flask app
if __name__ == '__main__':
    # Preprocess the data at startup
    data = preprocess_data()
    app.run(debug=True)
