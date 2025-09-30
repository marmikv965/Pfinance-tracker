 Finance Tracker
A simple personal finance tracker built with Python, SQLite, and Streamlit.
It helps you track income, expenses, and balance and visualize spending with charts

 Features

✅ Add income & expenses with category, date, and description
✅ View total income, expenses, and balance
✅ Pie chart of expenses by category
✅ Stores data in SQLite database
✅ Run as a Streamlit web app

Tech Stack
Python 3.9+
Streamlit → interactive UI
SQLite → database
Pandas & Matplotlib → data analysis & visualization

Installation & Setup

Install dependencies
pip install -r requirements.txt

run the app
streamlit run app.py


Project Structure
personal-finance-tracker/
│── app.py             # Main Streamlit app
│── database.py        # Database setup & connection
│── transactions.py    # Add/view transactions
│── visualization.py   # Charts & graphs
│── requirements.txt   # Dependencies
│── README.md          # Documentation
│── .gitignore         # Ignore db & venv
