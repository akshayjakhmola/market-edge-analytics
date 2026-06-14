import pandas as pd

trades = pd.read_csv(
    "reports/supertrend_trades_2015_2026.csv"
)

trades["Exit Time"] = pd.to_datetime(
    trades["Exit Time"]
)

trades["Month"] = (
    trades["Exit Time"]
    .dt.strftime("%Y-%m")
)

monthly = (
    trades.groupby("Month")
    .agg({
        "PnL INR": "sum",
        "Points": "sum"
    })
    .reset_index()
)

trade_count = (
    trades.groupby("Month")
    .size()
    .reset_index(name="Trades")
)

monthly = monthly.merge(
    trade_count,
    on="Month"
)

monthly["Return %"] = round(
    (monthly["PnL INR"] / 150000) * 100,
    2
)

monthly["Avg PnL/Trade"] = round(
    monthly["PnL INR"] / monthly["Trades"],
    2
)

monthly.to_csv(
    "reports/monthly_report.csv",
    index=False
)

print(monthly.head())

print(
    "\nMonthly report saved."
)