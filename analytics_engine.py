import pandas as pd


def run_corporate_analytics(csv_file):
    """Processes raw transaction data to extract high-level corporate KPIs and trends"""
    print(
        "[ANALYTICS ENGINE] Extracting performance metrics from transaction ledger..."
    )

    # Load dataset
    df = pd.read_csv(csv_file)
    df["Date"] = pd.to_datetime(df["Date"])
    df["Month"] = df["Date"].dt.strftime("%Y-%m")

    # 1. High-Level Executive KPIs
    kpis = {
        "Total_Gross_Revenue": round(df["Gross_Revenue"].sum(), 2),
        "Total_Discounts": round(df["Discount_Applied"].sum(), 2),
        "Total_Net_Revenue": round(df["Net_Revenue"].sum(), 2),
        "Total_Net_Profit": round(df["Net_Profit"].sum(), 2),
        "Average_Profit_Margin": round(
            (df["Net_Profit"].sum() / df["Net_Revenue"].sum()) * 100, 2
        ),
    }

    # 2. Product Performance Summary
    product_summary = (
        df.groupby("Product_Name")
        .agg(
            Units_Sold=("Quantity", "sum"),
            Net_Revenue=("Net_Revenue", "sum"),
            Net_Profit=("Net_Profit", "sum"),
        )
        .reset_index()
    )
    product_summary["Profit_Margin_%"] = round(
        (product_summary["Net_Profit"] / product_summary["Net_Revenue"]) * 100, 2
    )
    product_summary = product_summary.sort_values(by="Net_Revenue", ascending=False)

    # 3. Monthly Growth Cohorts
    monthly_trend = (
        df.groupby("Month")
        .agg(Net_Revenue=("Net_Revenue", "sum"), Net_Profit=("Net_Profit", "sum"))
        .reset_index()
        .sort_values(by="Month")
    )

    monthly_trend["MoM_Revenue_Growth_%"] = (
        monthly_trend["Net_Revenue"].pct_change().round(4) * 100
    )
    monthly_trend = monthly_trend.fillna(0)  # Handle first month change

    print("[ANALYTICS ENGINE] Data processing complete. Metrics locked.")
    return kpis, product_summary, monthly_trend


if __name__ == "__main__":
    # Test execution
    kpis, prod, month = run_corporate_analytics("raw_sales_ledger.csv")
    print("\n--- EXECUTIVE SUMMARY PREVIEW ---")
    print(f"Total Corporate Profit: ${kpis['Total_Net_Profit']:,}")
    print(f"Average System Margin: {kpis['Average_Profit_Margin']}%")
