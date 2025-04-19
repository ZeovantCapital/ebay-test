import streamlit as st
import requests
import pandas as pd
from datetime import datetime, timedelta

# ==== INSERT YOUR ACCESS TOKEN HERE ====
EBAY_TOKEN = "v^1.1#i^1#p^3#f^0#r^0#I^3#t^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"
# =======================================

headers = {
    "Authorization": f"Bearer {EBAY_TOKEN}",
    "Content-Type": "application/json",
    "Accept": "application/json"
}

def get_all_orders(days_back=30):
    start_time = (datetime.utcnow() - timedelta(days=days_back)).isoformat() + "Z"
    end_time = datetime.utcnow().isoformat() + "Z"
    url = "https://api.ebay.com/sell/fulfillment/v1/order"
    params = {
        "filter": f"creationdate:[{start_time}..{end_time}]",
        "limit": "50"
    }

    all_orders = []
    while url:
        response = requests.get(url, headers=headers, params=params)
        data = response.json()
        orders = data.get("orders", [])
        all_orders.extend(orders)
        url = data.get("next") if "next" in data else None
        params = None

    return all_orders

def format_orders(raw_orders):
    rows = []
    for o in raw_orders:
        try:
            title = o["lineItems"][0]["title"]
            qty = o["lineItems"][0]["quantity"]
            revenue = float(o["pricingSummary"]["total"]["value"])
            status = o.get("orderFulfillmentStatus", "N/A")
            date = o["creationDate"]
            rows.append({
                "Item": title,
                "Qty": qty,
                "Revenue": revenue,
                "Status": status,
                "Date": date
            })
        except Exception as e:
            pass
    return pd.DataFrame(rows)

# ==== Streamlit UI ====
st.title("🧾 Orders & Sales History")
days = st.slider("Look back (days)", 7, 90, 30)
st.info("Showing orders from the last {} days".format(days))

try:
    raw_orders = get_all_orders(days_back=days)
    df = format_orders(raw_orders)
    st.dataframe(df.sort_values("Date", ascending=False), use_container_width=True)
    st.metric("Total Orders", len(df))
    st.metric("Total Revenue", f"${df['Revenue'].sum():.2f}")
except Exception as e:
    st.error(f"Failed to load orders: {e}")
