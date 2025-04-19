import streamlit as st
import requests
import pandas as pd
from datetime import datetime, timedelta

EBAY_TOKEN = "v^1.1#i^1#f^0#r^0#I^3#p^3#t^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"
headers = {
    "Authorization": f"Bearer {EBAY_TOKEN}",
    "Content-Type": "application/json",
    "Accept": "application/json"
}

def get_payouts(days_back=30):
    start_time = (datetime.utcnow() - timedelta(days=days_back)).isoformat() + "Z"
    url = "https://api.ebay.com/sell/finances/v1/transaction"
    params = {
        "transaction_date": f"{start_time}..",
        "limit": "50"
    }

    all_txns = []

    while url:
        res = requests.get(url, headers=headers, params=params)
        if res.status_code != 200:
            st.error(f"API Error {res.status_code}")
            st.code(res.text)
            return pd.DataFrame()

        try:
            data = res.json()
            txns = data.get("transactions", [])
            all_txns += txns
            url = data.get("next", None)
            params = None  # don't resend params when using pagination URL
        except Exception as e:
            st.error("❌ JSON parse failed")
            st.error(f"Exception: {e}")
            st.code(res.text)
            return pd.DataFrame()

    rows = []
    for txn in all_txns:
        ttype = txn.get("transactionType", "N/A")
        amount = float(txn.get("transactionAmount", {}).get("value", 0))
        date = txn.get("transactionDate", "")
        order = txn.get("orderId", "N/A")
        rows.append({
            "Date": date,
            "Type": ttype,
            "Order ID": order,
            "Amount": amount
        })
    return pd.DataFrame(rows)


# Streamlit UI
st.title("💰 Payouts & Transaction Summary")
days = st.slider("Look back (days)", 7, 90, 30)

try:
    df = get_payouts(days)
    st.dataframe(df.sort_values("Date", ascending=False), use_container_width=True)
    st.metric("Net Total", f"${df['Amount'].sum():.2f}")
except Exception as e:
    st.error(f"Failed to load payouts: {e}")
