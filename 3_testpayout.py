import streamlit as st
import requests
from utils.ebay_auth import get_access_token

EBAY_TOKEN = get_access_token()

headers = {
    "Authorization": f"Bearer {EBAY_TOKEN}",
    "Content-Type": "application/json",
    "Accept": "application/json"
}

def get_transactions():
    url = "https://api.ebay.com/sell/finances/v1/transaction?limit=5"
    st.write(f"🔗 Testing URL: {url}")

    try:
        res = requests.get(url, headers=headers)
        st.write(f"✅ Status Code: {res.status_code}")
        if res.status_code == 200:
            st.success("✅ Your eBay account is eligible for the Finances API (transactions).")
            st.json(res.json())
        elif res.status_code == 404:
            st.error("❌ 404 Not Found – This likely means your eBay account is not yet activated for Finances API.")
            st.code(res.text)
        elif res.status_code == 401:
            st.error("❌ 401 Unauthorized – Your token is likely expired or missing the correct scope.")
            st.code(res.text)
        else:
            st.warning(f"Unexpected status code: {res.status_code}")
            st.code(res.text)
    except Exception as e:
        st.error("Error occurred while trying to fetch transactions.")
        st.exception(e)

# ==== UI ====
st.set_page_config(page_title="eBay Finances API Debug", layout="wide")
st.title("🧪 eBay Finances API Debug: Transaction Endpoint")

st.markdown("""
This tool will test your access to the `/sell/finances/v1/transaction` endpoint and print the raw response.

- ✅ If you get `200`, your account has API access to finances.
- ❌ If you get `404`, your eBay seller account may not be fully linked to the Finances API yet.
- ❌ If
