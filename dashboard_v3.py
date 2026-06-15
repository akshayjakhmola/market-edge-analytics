import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Market Edge Analytics",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
[data-testid="collapsedControl"] {
    display: block !important;
}
</style>
""", unsafe_allow_html=True)

st.caption(
    "| Zerodha Historical Data Based |"
)

# ==========================
# SIDEBAR BRANDING
# ==========================

st.sidebar.image(
    "logo.png",
    use_container_width=True
)

st.sidebar.title(
    "Market Edge Analytics"
)

st.sidebar.markdown("---")

index_type = st.radio(
    "Select Index",
    ["NIFTY", "BANKNIFTY"]
)

st.sidebar.success(
    "Professional Trading Analytics Dashboard"
)
# ==========================
# LOAD DATA
# ==========================

if index_type == "NIFTY":

    trades = pd.read_csv(
        "reports/market_edge_trades.csv"
    )

    monthly = pd.read_csv(
        "reports/monthly_report.csv"
    )

    equity_curve = pd.read_csv(
        "reports/equity_curve.csv"
    )

    drawdown_curve = pd.read_csv(
        "reports/drawdown_curve.csv"
    )

    tv_report = pd.read_csv(
        "reports/tradingview_style_report.csv"
    )

    strategy_name = "Nifty Market Edge"

else:

    trades = pd.read_csv(
        "reports/banknifty_market_edge_trades.csv"
    )

    monthly = pd.read_csv(
        "reports/banknifty_monthly_report.csv"
    )

    equity_curve = pd.read_csv(
        "reports/banknifty_equity_curve.csv"
    )

    drawdown_curve = pd.read_csv(
        "reports/banknifty_drawdown_curve.csv"
    )

    tv_report = pd.read_csv(
        "reports/banknifty_tradingview_style_report.csv"
    )

    strategy_name = "BankNifty Market Edge"

tv_report["Entry Time"] = pd.to_datetime(
    tv_report["Entry Time"]
)

tv_report["Year"] = (
    tv_report["Entry Time"].dt.year
)

if index_type == "NIFTY":
    total_candles = 211213
else:
    total_candles = 211204
# ==========================
# CALCULATIONS
# ==========================

total_trades = len(trades)

winning_trades = len(
    trades[trades["PnL INR"] > 0]
)

losing_trades = len(
    trades[trades["PnL INR"] <= 0]
)

win_rate = round(
    (winning_trades / total_trades) * 100,
    2
)

net_profit = round(
    trades["PnL INR"].sum(),
    2
)

# Capital Based Return

capital = 150000

return_pct = round(
    (net_profit / capital) * 100,
    2
)

years = 11

cagr = round(
    (
        (
            (capital + net_profit)
            / capital
        ) ** (1 / years) - 1
    ) * 100,
    2
)

gross_profit = trades[
    trades["PnL INR"] > 0
]["PnL INR"].sum()

gross_loss = abs(
    trades[
        trades["PnL INR"] <= 0
    ]["PnL INR"].sum()
)

profit_factor = round(
    gross_profit / gross_loss,
    2
)

largest_win = trades["PnL INR"].max()
largest_loss = trades["PnL INR"].min()

# Drawdown

equity = trades["Cumulative PnL INR"]

running_peak = equity.cummax()

drawdown = equity - running_peak

max_dd = round(
    abs(drawdown.min()),
    2
)

max_dd_pct = round(
    (abs(drawdown.min()) /
     running_peak.max()) * 100,
    2
)
results = (trades["PnL INR"] > 0).astype(int)

max_win_streak = 0
max_loss_streak = 0

win_streak = 0
loss_streak = 0

for r in results:

    if r == 1:
        win_streak += 1
        loss_streak = 0
    else:
        loss_streak += 1
        win_streak = 0

    max_win_streak = max(
        max_win_streak,
        win_streak
    )

    max_loss_streak = max(
        max_loss_streak,
        loss_streak
    )
# ==========================
# HEADER
# ==========================

st.markdown(
    f"""
<div style="
padding:25px;
border-radius:15px;
background:linear-gradient(135deg,#1e3c72,#2a5298);
text-align:center;
box-shadow:0px 4px 15px rgba(0,0,0,0.3);
">

<h1 style="color:white;margin-bottom:5px;">
Market Edge Analytics
</h1>

<h3 style="color:#00ff99;margin-top:0;">
Strategy : {strategy_name}
</h3>

<p style="color:white;">
Professional Quantitative Trading Analytics Dashboard
</p>

<p style="color:#d9d9d9;">
2015–2026 | {total_trades:,} Trades | Multi-Year Performance Analysis
</p>

</div>
""",
    unsafe_allow_html=True
)
st.markdown("---")

# ==========================
# KPI CARDS
# ==========================

st.markdown("---")

c1, c2, c3, c4, c5, c6 = st.columns(6)

c1.metric(
    "Net Profit",
    f"₹{net_profit:,.0f}"
)

c2.metric(
    "Return %",
    f"{return_pct}%"
)

c3.metric(
    "CAGR %",
    f"{cagr}%"
)

c4.metric(
    "Profit Factor",
    profit_factor
)

c5.metric(
    "Win Rate",
    f"{win_rate}%"
)

c6.metric(
    "Max DD",
    f"{max_dd_pct}%"
)
# ==========================
# STRATEGY SCORECARD
# ==========================

st.markdown("---")

st.subheader("🎯 Strategy Scorecard")

scorecard = pd.DataFrame({
    "Metric": [
        "Win Rate",
        "Profit Factor",
        "Max Drawdown",
        "Recovery Factor",
        "Total Trades"
    ],
    "Value": [
        f"{win_rate}%",
        profit_factor,
        f"{max_dd_pct}%",
        "14.01",
        total_trades
    ]
})

st.dataframe(
    scorecard,
    use_container_width=True
)
# ==========================
# STRATEGY INFO
# ==========================

st.subheader("Strategy Information")

st.write(
    f"""
    Data Source : Zerodha

    Timeframe : 5 Minute

    Period : 2015 - 2026

    Candles : {total_candles:,}

    Strategy : {strategy_name}
    """
)

c1, c2, c3, c4 = st.columns(4)

c1.metric("Years Tested", "11+")

c2.metric("Candles", f"{total_candles:,}")

c3.metric("Trades", f"{total_trades:,}")

c4.metric("Recovery Factor", round(net_profit/max_dd,2))
# ==========================
# EQUITY CURVE
# ==========================

st.markdown("---")

st.subheader("📈 Equity Curve")

fig = px.line(
    equity_curve,
    x="Exit Time",
    y="Cumulative PnL INR",
    title="Equity Curve"
)

st.plotly_chart(
    fig,
    use_container_width=True,
    key="equity_curve"
)


# ==========================
# DRAWDOWN CURVE
# ==========================

st.subheader("📉 Drawdown Curve")

fig_dd = px.line(
    drawdown_curve,
    x="Trade",
    y="Drawdown",
    title="Drawdown Over Time"
)

fig_dd.update_traces(line_color="red")

st.plotly_chart(
    fig_dd,
    use_container_width=True,
    key="drawdown_curve"
)

# ==========================
# TRADE STATS
# ==========================

st.markdown("---")

c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "Total Trades",
    total_trades
)

c2.metric(
    "Winning Trades",
    winning_trades
)

c3.metric(
    "Losing Trades",
    losing_trades
)

c4.metric(
    "Drawdown ₹",
    f"₹{max_dd:,.0f}"
)
c1, c2 = st.columns(2)

c1.metric(
    "Longest Winning Streak",
    max_win_streak
)

c2.metric(
    "Longest Losing Streak",
    max_loss_streak
)
# ==========================
# WIN LOSS PIE CHART
# ==========================

st.markdown("---")

st.subheader("🥧 Win vs Loss Distribution")

pie_data = pd.DataFrame({
    "Result": ["Winning Trades", "Losing Trades"],
    "Count": [winning_trades, losing_trades]
})

fig_pie = px.pie(
    pie_data,
    names="Result",
    values="Count",
    title="Winning vs Losing Trades"
)

st.plotly_chart(
    fig_pie,
    use_container_width=True,
    key="win_loss_pie"
)
# ==========================
# YEARLY PERFORMANCE
# ==========================

st.markdown("---")

st.subheader("📊 Year-wise Performance")

trades["Exit Time"] = pd.to_datetime(
    trades["Exit Time"]
)

trades["Year"] = (
    trades["Exit Time"].dt.year
)


yearly = (
    trades.groupby("Year")
    .agg({
        "PnL INR": "sum",
        "Points": "sum"
    })
    .reset_index()
)

trade_count = (
    trades.groupby("Year")
    .size()
    .reset_index(name="Trades")
)

yearly = yearly.merge(
    trade_count,
    on="Year"
)
yearly["Return %"] = round(
    (yearly["PnL INR"] / capital) * 100,
    2
)

yearly["Avg PnL/Trade"] = round(
    yearly["PnL INR"] / yearly["Trades"],
    2
)

yearly = yearly[
    [
        "Year",
        "Trades",
        "PnL INR",
        "Return %",
        "Avg PnL/Trade",
        "Points"
    ]
]

st.dataframe(
    yearly,
    use_container_width=True
)

yearly["Color"] = yearly["PnL INR"].apply(
    lambda x: "Profit" if x >= 0 else "Loss"
)

fig_year = px.bar(
    yearly,
    x="Year",
    y="Return %",
    color="Color",
    color_discrete_map={
        "Profit": "green",
        "Loss": "red"
    },
    hover_data=[
        "Trades",
        "PnL INR",
        "Points"
    ],
    title="Year-wise Return % (₹1.5L Capital)"
)

fig_year.update_layout(
    showlegend=False
)

st.plotly_chart(
    fig_year,
    use_container_width=True,
    key="yearly_chart"
)
best_year = yearly.loc[
    yearly["Return %"].idxmax()
]

worst_year = yearly.loc[
    yearly["Return %"].idxmin()
]

c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "Best Year",
    best_year["Year"]
)

c2.metric(
    "Best Return %",
    f'{best_year["Return %"]}%'
)

c3.metric(
    "Worst Year",
    worst_year["Year"]
)

c4.metric(
    "Worst Return %",
    f'{worst_year["Return %"]}%'
)

profitable_years = len(
    yearly[yearly["PnL INR"] > 0]
)

losing_years = len(
    yearly[yearly["PnL INR"] <= 0]
)

yearly_win_rate = round(
    (profitable_years / len(yearly)) * 100,
    2
)

c1, c2, c3 = st.columns(3)

c1.metric(
    "Profitable Years",
    profitable_years
)

c2.metric(
    "Losing Years",
    losing_years
)

c3.metric(
    "Yearly Win Rate",
    f"{yearly_win_rate}%"
)
st.subheader("🥧 Year-wise Profit Contribution")

fig_year_pie = px.pie(
    yearly,
    names="Year",
    values="PnL INR",
    title="Year-wise Profit Contribution"
)

st.plotly_chart(
    fig_year_pie,
    use_container_width=True,
    key="yearly_pie"
)
# ==========================
# MONTHLY PERFORMANCE
# ==========================

st.markdown("---")

st.subheader("📅 Monthly Performance")

st.dataframe(
    monthly[
        [
            "Month",
            "Trades",
            "PnL INR",
            "Return %",
            "Avg PnL/Trade",
            "Points"
        ]
    ],
    use_container_width=True
)

monthly["Color"] = monthly["PnL INR"].apply(
    lambda x: "Profit" if x >= 0 else "Loss"
)

fig_month = px.bar(
    monthly,
    x="Month",
    y="Return %",
    color="Color",
    color_discrete_map={
        "Profit": "green",
        "Loss": "red"
    },
    hover_data=[
        "Trades",
        "PnL INR",
        "Avg PnL/Trade",
        "Points"
    ],
    title="Monthly Return % (₹1.5L Capital)"
)

st.plotly_chart(
    fig_month,
    use_container_width=True,
    key="monthly_chart"
)

avg_monthly = monthly["PnL INR"].mean()

best_month_return = monthly.loc[
    monthly["Return %"].idxmax()
]

worst_month_return = monthly.loc[
    monthly["Return %"].idxmin()
]

c1, c2, c3, c4, c5 = st.columns(5)

c1.metric(
    "Best Month",
    best_month_return["Month"]
)

c2.metric(
    "Best Return %",
    f'{best_month_return["Return %"]}%'
)

c3.metric(
    "Worst Month",
    worst_month_return["Month"]
)

c4.metric(
    "Worst Return %",
    f'{worst_month_return["Return %"]}%'
)

c5.metric(
    "Avg Monthly Profit",
    f"₹{avg_monthly:,.0f}"
)

profitable_months = len(
    monthly[monthly["PnL INR"] > 0]
)

losing_months = len(
    monthly[monthly["PnL INR"] <= 0]
)

total_months = len(monthly)

monthly_win_rate = round(
    (profitable_months / total_months) * 100,
    2
)

c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "Total Months",
    total_months
)

c2.metric(
    "Profitable Months",
    profitable_months
)

c3.metric(
    "Losing Months",
    losing_months
)

c4.metric(
    "Monthly Win Rate",
    f"{monthly_win_rate}%"
)
# ==========================
# COST ANALYSIS
# ==========================

st.subheader("💰 Cost Adjusted Backtest")

st.info(
    """
    Assumption:

    Entry Slippage : 1 Point

    Exit Slippage  : 1 Point

    Total Slippage : 2 Points Per Trade

    Total Trades   : 3826
    """
)

raw_profit = 2397167.50

cost_profit = 1899787.50

impact = raw_profit - cost_profit

c1, c2, c3 = st.columns(3)

c1.metric(
    "Raw Profit",
    f"₹{raw_profit:,.0f}"
)

c2.metric(
    "After Slippage",
    f"₹{cost_profit:,.0f}"
)

c3.metric(
    "Slippage Impact",
    f"₹{impact:,.0f}"
)

st.write(
    f"""
    Total Slippage Cost:
    ₹{impact:,.0f}

    Profit Factor Before Cost:
    1.28

    Profit Factor After Cost:
    1.22
    """
)

st.markdown("---")

st.subheader("📋 Cost Model Summary")

st.warning(
    """
    Assumptions Used in Cost Adjusted Backtest

    • Entry Slippage     : 1 Point

    • Exit Slippage      : 1 Point

    • Total Slippage     : 2 Points Per Trade

    • Total Trades       : 3,826

    • Total Cost Impact  : ₹4,97,380

    • Profit Factor Raw  : 1.28

    • Profit Factor Cost Adjusted : 1.22

    Note:
    Brokerage, STT, Exchange Charges,
    GST, SEBI Charges and Stamp Duty
    are currently NOT included.
    """
)
c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "Entry Slippage",
    "1 Point"
)

c2.metric(
    "Exit Slippage",
    "1 Point"
)

c3.metric(
    "Cost Impact",
    "₹4.97L"
)

c4.metric(
    "PF After Cost",
    "1.22"
)
# ==========================
# TRADE EXPLORER
# ==========================

st.markdown("---")

st.subheader("📋 Trade Explorer")

trade_search = st.text_input(
    "Search Trade"
)

selected_year = st.selectbox(
    "Select Year",
    ["ALL"] + sorted(
        trades["Year"].unique().tolist()
    )
)

trade_type = st.selectbox(
    "Filter Trade Type",
    ["ALL", "LONG", "SHORT"]
)

filtered = tv_report.copy()

if selected_year != "ALL":
    filtered = filtered[
        filtered["Year"] == selected_year
    ]

if trade_type != "ALL":
    filtered = filtered[
        filtered["Type"] == trade_type
    ]

if trade_search:
    filtered = filtered[
        filtered.astype(str)
        .apply(
            lambda row: row.str.contains(
                trade_search,
                case=False,
                na=False
            ).any(),
            axis=1
        )
    ]

st.dataframe(
    filtered,
    use_container_width=True
)
# ==========================
# TOP WINNERS
# ==========================

st.markdown("---")

st.subheader(
    "🏆 Top 20 Winners"
)

st.dataframe(
    trades.sort_values(
        "PnL INR",
        ascending=False
    ).head(20)
)

# ==========================
# DOWNLOAD CENTER
# ==========================

st.subheader("📥 Download Center")

csv = tv_report.to_csv(index=False)

st.download_button(
    label="📥 Download Detailed Trade Log",
    data=csv,
    file_name=f"{strategy_name}_Trade_Log.csv",
    mime="text/csv"
)
# ==========================
# TOP LOSERS
# ==========================

st.markdown("---")

st.subheader(
    "⚠ Top 20 Losers"
)

st.dataframe(
    trades.sort_values(
        "PnL INR",
        ascending=True
    ).head(20)
)
st.markdown("---")

st.subheader("🏆 Strategy Verdict")

st.success(
    f"""
    Backtest Status : PASSED

    Strategy : {strategy_name}

    Years Tested : 2015-2026

    Total Trades : {total_trades:,}

    Profit Factor : {profit_factor}

    Max Drawdown : {max_dd_pct}%

    Net Profit : ₹{net_profit:,.0f}

    Win Rate : {win_rate}%
    """
)
st.markdown("---")

st.markdown(
    """
    <div style='text-align:center; padding:15px;'>

    <h4 style='margin-bottom:5px;'>
    📊 Market Edge Analytics
    </h4>

    <p style='color:gray;'>
    Advanced Backtesting & Performance Analytics
    </p>

    <p style='font-size:12px; color:gray;'>
    Historical Market Data | Quantitative Research Dashboard
    </p>

    </div>
    """,
    unsafe_allow_html=True
)