import streamlit as st
from database import init_db
from transactions import add_transaction, get_summary
from visualization import expense_chart

init_db()

st.title("finance tracker")

t_type = st.selectbox("type", ["income", "expense"])
category = st.text_input("category")
amount = st.number_input("amount", min_value=0.0)
date = st.date_input("date")
description = st.text_area("description")

if st.button("Add Transaction"):
    add_transaction(t_type, category, amount, date, description)
    st.success("Transaction added!")

income, expense, balance = get_summary()
st.metric("Total Income", f"{income}")
st.metric("Total Expense", f"{expense}")
st.metric("Balance", f"{balance}")

if st.button("show expense chart"):
    expense_chart()