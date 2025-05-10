import streamlit as st

import requests

import pandas as pd

from datetime import datetime, timedelta


# Your short-lived OAuth token from eBay

EBAY_TOKEN = "v^1.1#i^1#p^3#I^3#r^0#f^0#t^H4sIAAAAAAAA/+VZeWwcVxn3+gg4we4VIFQVLONCoe7svpmd2ZkdxWvG9rq242PtdeLGEjJvZt54Xz07M555Y3utqHIsUY6mjSqioNKiRoUi/kCqelGRuhxVERWERhUSRIpQWySOQgCRFgIICd6sj2wMSezdQFdi/1nNe9/1+953vAMs7Wi+/d6+ey+0RN5Vf2IJLNVHItwu0Lyjqb21of7mpjpQRhA5sXTrUuNyw2/2+rBgucoY8l3H9lF0oWDZvlIa7GACz1Yc6GNfsWEB+QrRlZw6NKjwMaC4nkMc3bGYaH9PBwN5SeK1BEppSRkmDI6O2usyx50OhucSugQ0LgU4jkM8oPO+H6B+2yfQJnQe8CILRJYD45ygiEAR5BifAJNM9ADyfOzYlCQGmHTJXKXE65XZemVToe8jj1AhTLpf7c2NqP09meHxvfEyWek1P+QIJIF/6Ve3Y6DoAWgF6Mpq/BK1kgt0Hfk+E0+varhUqKKuG1OB+SVXp2QNJZJSEvGirENDuyau7HW8AiRXtiMcwQZrlkgVZBNMilfzKPWGdjfSydrXMBXR3xMN/0YDaGETI6+DyXSpB/fnMmNMNJfNes4cNpARIuUlXk6kBElOMOlF5MxReGsqVuWsOXiTjm7HNnDoLj867JAuRO1Fm70ilHmFEo3YI55qktCWcrrkuvd4ShdfX7+A5O1wRVGBuiBa+ry679eD4eLyX6twkHURAk02pJQoiHySu0w4hLm+rZBIh6uiZrPx0BakwSJbgN4MIq4FdcTq1L1BAXnYUBKiySdkE7FGMmWyQso0WU00kixnIgQQ0jQ9Jf9/RAYhHtYCgjaiY/NECV4Hk9MdF2UdC+tFZjNJqc6sxcKC38HkCXGVeHx+fj42n4g53nScB4CL3zU0mNPzqACZDVp8dWIWl6JCR5TLxwoputSaBRp0VLk9zaQTnpGFHinmkGXRgfWQvcS29ObRy4DstjD1wDhVUVsY+xyfIKMqaAaawzqawkZtIeN5TuSAIPNhrosASFWBtJxpbA8hkndqDGZYD/p7qsJGyycktYWqrLoAaa0KcWKCpR8AVAVWdd3+QiEgULNQf42tpciLHCdWBc8NglpLxCIhM5BA2mqSVUELu66CoakQZwbZ/7mUhrn+TmIdy/SOZXJ9U+Mj+zLDVaEdQ6aH/Px4iLXW4lQdVfep9Dc0Ys0uptwscl3V7LWlsQzB4p3zA2hYWIgPzQzMDKQWi8nMaCYJDKMvmbDz4/KwJczNYi/bvo+QofmOjqqclEO6h2qsdDmp3oMTVq87OzooDvcANDHUNdLO5fzZRavPVLun2/cBz3YnVRNnqgM/NF1rmb7Rcqtut+OXT/ENgGGuvwMgvdXEnCpVoSn6VRXQzHTN1WtBMjkpkeS5FABQE3TZkGWBNwTThIIMTa3q9ltjeCdh0bgzD0127ejEZsd6WIkXJT4pcTprSkDgeLm6XYdbc6t8rbqyH57e/uvQwlzfFrxQhk+FQBfHwo1DTHcKcQcGJB8OTZWsjm6FKO7T019s9bBPJcc8BA3HtoqVMG+DB9tz9LzoeMVKFG4wb4MH6roT2KQSdWus2+AwA8vElhVeClSisIx9O2ba0CoSrPsVqcR2GG3+NlhcWCwBNLDvhvmyJU46VkCejmLYWL1SrMRYD1GFsHSNVgnTNlVumGw7BJtYX5XhB5qve9jduhXrcsJcv7ysSvzh01zY1tKtMmxJVRkXMpCF55BXrO40jgzsIZ1MBR6urZYRNsqpsFOa0GM3dU02X5jzUVXAQ3fW4g1LVs3lJkbGqrtj6UFztbbv4YEgGCnJYAUjmWKFFBBZTRYNlpNFMQF0OqpVt9fbwq1S4+Gz/1vQnCQkZVlOClve9WwaKLvN/rcnjPilr4fputKPW468CJYj366PRMBe8BGuDXx4R8P+xob33OxjQgs9NGM+nrYhCTwUm0FFF2Kv/qa6062DxuG+wT8vacFzE293ynUtZY+XJz4J9mw8XzY3cLvK3jLBLRdnmrjr3t9Cj2P0WMYJIj2aTYK2i7ON3Psad3//Quvx4J5Hj330uydXzgz4K7eopxnQskEUiTTVNS5H6lba+T0LO2/4rfeVJ/70dWfxU+c/qO4/0vQy4H519uDxYwcOMKkH73vhCzs/P/nDx3sfvOnQmc7zk1+OdR/egb75x2f/do/wxh9Ofu6up+0fP9J52yfGn+9++ieJxx62H3np1VNtRz/++PHcd25cPPRim3b+6OnZOzrfPDb1/K5DX/xYFl33Ruvdj83sbH3hgXTk/vce0txfvPbXVxb3j54bfQ6sfOnUkQfaX37qQnL38s8fOiL+/uFfNzff98zXbv/pV5l33/iXla7P/uOc/tLRt/mT6u9eaU1Ndj4ka2f5vbPqL0+9+lZmKbr7Z59+/a2WPWfuf3LGOctJbQM/8K+v//sHXv/Ma/Dck48+dce3kl03THzje+KH3uz6Ueafnatr+S+nNJLAVh4AAA=="
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

        "limit": "100"

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

