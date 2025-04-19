import streamlit as st

import requests

import pandas as pd

from datetime import datetime, timedelta


# Your short-lived OAuth token from eBay

EBAY_TOKEN = "v^1.1#i^1#p^3#r^0#I^3#f^0#t^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"


st.set_page_config(page_title="Zeovant eBay Dashboard", layout="wide")

st.title("Zeovant eBay Order Tracker")


# Request headers

headers = {

    "Authorization": f"Bearer {EBAY_TOKEN}",

    "Content-Type": "application/json",

    "Accept": "application/json"

}


# Pull orders from eBay

def get_orders(days_back=100):

    start_time = (datetime.utcnow() - timedelta(days=days_back)).isoformat() + "Z"

    end_time = datetime.utcnow().isoformat() + "Z"

    url = "https://api.ebay.com/sell/fulfillment/v1/order"

    params = {

        "filter": f"creationdate:[{start_time}..{end_time}]",

        "limit": "10"

    }

    response = requests.get(url, headers=headers, params=params)

    orders = response.json().get("orders", [])

    data = []

    for order in orders:

        title = order["lineItems"][0]["title"]

        total = float(order["pricingSummary"]["total"]["value"])

        created = order["creationDate"]

        data.append({"Item": title, "Revenue": total, "Date": created})

    return pd.DataFrame(data)


try:

    df = get_orders()

    st.dataframe(df)

    st.metric("Total Revenue (Last 30 Days)", f"${df['Revenue'].sum():.2f}")

except Exception as e:

    st.error(f"Failed to load orders: {e}")

