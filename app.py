import streamlit as st

st.set_page_config(
    page_title="Escape Velocity",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 Escape Velocity")

st.subheader("Build Momentum. Escape Debt.")

remaining_debt = 31596
monthly_payment = 1935

col1, col2 = st.columns(2)

with col1:
    st.metric(
        label="Remaining Debt",
        value=f"${remaining_debt:,}"
    )

with col2:
    st.metric(
        label="Monthly Payment",
        value=f"${monthly_payment:,}"
    )

st.divider()

st.header("🎯 Current Mission")

st.info("Destroy CareCredit")

st.progress(0)

st.write("Balance: **$1,385**")
st.write("APR: **32.99%**")
st.write("Extra Payment: **$800/month**")