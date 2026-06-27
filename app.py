import streamlit as st
from utils.calculations import load_debts, total_debt, next_target, avalanche_order

st.set_page_config(page_title="Escape Velocity", layout="wide")

df = load_debts()

total = total_debt(df)
target = next_target(df)
ordered = avalanche_order(df)

st.title("🚀 Escape Velocity")

col1, col2, col3 = st.columns(3)

col1.metric("Remaining Debt", f"${float(total):,.0f}")
col2.metric("Current Target", target["Name"])
col3.metric("APR", f"{target['APR']}%")

st.divider()

st.subheader("🔥 Debt Avalanche Order")

st.dataframe(ordered)