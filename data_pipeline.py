import pandas as pd
import numpy as np
from datetime import datetime, timedelta


def generate_enterprise_raw_data():
    """Generates a professional, realistic 12-month transaction ledger for business analytics"""
    np.random.seed(42)
    start_date = datetime(2026, 1, 1)

    products = {
        "Enterprise Server Suite": ("Electronics", 1200, 0.25),
        "Cloud Workspace Pro": ("SaaS", 45, 0.15),
        "AI Analytics API Token": ("SaaS", 250, 0.10),
        "Workstation Pro Setup": ("Electronics", 850, 0.20),
        "Cybersecurity Firewall V4": ("Software", 600, 0.30),
    }

    data = []
    # 1500 realistic corporate entries over the year
    for _ in range(1500):
        days_offset = np.random.randint(0, 240)
        txn_date = start_date + timedelta(days=days_offset)

        prod_name = np.random.choice(list(products.keys()))
        category, unit_price, discount_max = products[prod_name]

        qty = (
            np.random.randint(1, 15) if category != "SaaS" else np.random.randint(5, 50)
        )
        gross_revenue = qty * unit_price

        # Professional adjustments: Discounts, COGS (Cost of goods sold) and Net Margins
        applied_discount = round(np.random.uniform(0, discount_max) * gross_revenue, 2)
        net_revenue = gross_revenue - applied_discount
        cogs = round(net_revenue * np.random.uniform(0.4, 0.6), 2)
        profit = net_revenue - cogs

        data.append(
            [
                txn_date.strftime("%Y-%m-%d"),
                f"TXN-{np.random.randint(100000, 999999)}",
                prod_name,
                category,
                qty,
                unit_price,
                gross_revenue,
                applied_discount,
                net_revenue,
                profit,
            ]
        )

    columns = [
        "Date",
        "Transaction_ID",
        "Product_Name",
        "Category",
        "Quantity",
        "Unit_Price",
        "Gross_Revenue",
        "Discount_Applied",
        "Net_Revenue",
        "Net_Profit",
    ]
    df = pd.DataFrame(data, columns=columns)

    # Save as enterprise raw CSV
    df.to_csv("raw_sales_ledger.csv", index=False)
    print(
        "[PIPELINE COMPLETE] Generated 1,500 enterprise records in 'raw_sales_ledger.csv'"
    )


if __name__ == "__main__":
    generate_enterprise_raw_data()
