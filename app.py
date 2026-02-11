import sys
sys.path.append("/content/smartsupply")  # Add smartsupply folder to path

import streamlit as st
from database import Database
from inventory import Inventory
from sales import Sales
from analytics import Analytics

db = Database()
inventory = Inventory(db)
sales = Sales(db)
analytics = Analytics(db)

st.set_page_config(page_title="SmartSupply", layout="wide")
st.title("SmartSupply — Inventory & Sales System")

menu = st.sidebar.selectbox("Menu", ["Inventory", "Sales", "Analytics"])

if menu == "Inventory":
    st.header("Inventory Management")

    name = st.text_input("Product Name")
    price = st.number_input("Price", min_value=0.0)
    stock = st.number_input("Stock", min_value=0, step=1)

    if st.button("Add Product"):
        inventory.add_product(name, price, stock)
        st.success("Product added successfully")

    st.subheader("Product List")
    st.table(inventory.get_products())

elif menu == "Sales":
    st.header("Sales")

    products = inventory.get_products()
    product_map = {f"{p[1]} (Stock: {p[3]})": p[0] for p in products}

    if products:
        product_name = st.selectbox("Select Product", list(product_map.keys()))
        quantity = st.number_input("Quantity", min_value=1, step=1)

        if st.button("Record Sale"):
            success = sales.record_sale(product_map[product_name], quantity)
            if success:
                st.success("Sale recorded successfully")
            else:
                st.error("Not enough stock")

        st.subheader("Sales Records")
        st.table(sales.get_sales())
    else:
        st.info("No products available. Add products first.")

elif menu == "Analytics":
    st.header("Business Analytics")

    report = analytics.sales_report()
    st.dataframe(report)

    if not report.empty:
        st.metric("Total Revenue", f"₹ {report['revenue'].sum():.2f}")
    else:
        st.info("No sales data available yet.")
