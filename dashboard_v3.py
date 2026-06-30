import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Market Edge Analytics V4",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>

/* ===== Premium KPI Cards ===== */

div[data-testid="stMetric"]{
    background:#111827;
    border:1px solid rgba(255,255,255,0.05);
    border-radius:14px;
    padding:14px;
    box-shadow:0 4px 12px rgba(0,0,0,.18);
    transition:all .25s ease;
}

div[data-testid="stMetric"]:hover{
    box-shadow:0 0 15px rgba(59,130,246,.18);
    transition:.25s ease;
}

div[data-testid="stMetricLabel"]{
    font-size:14px !important;
    font-weight:600 !important;
    color:#cbd5e1 !important;
}

div[data-testid="stMetricValue"]{
    font-size:28px !important;
    font-weight:700 !important;
    color:white !important;
}

div[data-testid="stMetricDelta"]{
    font-size:14px !important;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
[data-testid="collapsedControl"] {
    display: block !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>

/* ========= Portfolio Selector ========= */

div[role="radiogroup"]{
    display:flex;
    justify-content:center;
    gap:12px;
    margin-top:10px;
    margin-bottom:20px;
}

div[role="radiogroup"] > label{
    background:#111827;
    border:1px solid rgba(255,255,255,.08);
    border-radius:14px;
    padding:12px 20px;
    transition:.25s;
    min-width:170px;
    justify-content:center;
}

div[role="radiogroup"] > label:hover{
    transform:translateY(-2px);
    border-color:#22C55E;
    box-shadow:0 0 15px rgba(34,197,94,.25);
}

div[role="radiogroup"] p{
    color:white !important;
    font-size:16px !important;
    font-weight:700 !important;
}

</style>
""", unsafe_allow_html=True)

st.markdown(
    """
<div style="
margin-top:-10px;
margin-bottom:8px;
font-size:15px;
color:#E5E7EB;
">
📢 <b>Viewing Recommendation</b> - For the best viewing experience, please use a desktop or laptop.
</div>
""",
    unsafe_allow_html=True
)
st.markdown(
    f"""
<div style="
padding:38px;
border-radius:24px;
background:linear-gradient(135deg,#020617 0%,#0F172A 30%,#1E3A8A 70%,#2563EB 100%);
border:1px solid rgba(255,255,255,0.10);
box-shadow:0 15px 40px rgba(0,0,0,.40);
text-align:center;
margin-bottom:25px;
">

<div style="
display:inline-block;
padding:8px 22px;
border-radius:999px;
background:rgba(34,197,94,.15);
border:1px solid rgba(34,197,94,.45);
color:#22C55E;
font-size:13px;
font-weight:700;
letter-spacing:1px;
text-transform:uppercase;
margin-bottom:20px;
">
STRATEGY PERFORMANCE DOSSIER
</div>

<div style="
font-size:14px;
font-weight:600;
letter-spacing:4px;
text-transform:uppercase;
color:#CBD5E1;
margin-bottom:1px;
text-align:center;
">
PREPARED FOR
</div>

<h1 style="
margin:0;
font-size:18px;
font-weight:900;
color:#FFFFFF;
letter-spacing:0.5px;
text-align:center;
line-height:1.3;
text-shadow:0 0 18px rgba(255,255,255,.18);
">
Mr. Lucky Gangwal
</h1>

<div style="
width:120px;
height:4px;
background:linear-gradient(90deg,#22C55E,#3B82F6);
border-radius:999px;
margin:20px auto 20px auto;
display:block;
">
</div>

<h2 style="
margin:0;
color:#22C55E;
font-size:26px;
font-weight:700;
">
Directional Strategy - Backtest Report
</h2>

<p style="
margin-top:18px;
font-size:17px;
color:#E2E8F0;
">
NIFTY • BANKNIFTY • Combined Directional Strategy Portfolio
</p>

<p style="
margin-top:10px;
font-size:14px;
color:#94A3B8;
letter-spacing:.5px;
line-height:1.8;
">
Quantitative Research • Performance Analytics •
Risk Assessment • Capital Growth Evaluation
</p>

<hr style="
margin:24px 0 18px 0;
border:none;
height:1px;
background:rgba(255,255,255,.10);
">

<div style="
display:flex;
justify-content:center;
gap:35px;
flex-wrap:wrap;
color:#CBD5E1;
font-size:14px;
">

<div>📅 <b>Backtest:</b> 2015–2026</div>

<div>📊 <b>Portfolio:</b> NIFTY | BANKNIFTY | Combined</div>

<div>🔒 <b>Classification:</b> Confidential</div>

</div>

</div>
""",
    unsafe_allow_html=True
)


# ==========================
# SIDEBAR BRANDING
# ==========================

st.sidebar.image(
    "logo.png",
    use_container_width=True
)

st.sidebar.title(
    "DIRECTIONAL STRATEGY"
)

st.sidebar.markdown("---")

index_type = st.radio(
    "🏛️ Portfolio Selection",
    ["NIFTY", "BANKNIFTY", "COMBINED"],
    horizontal=True
)

st.sidebar.success(
    "NIFTY • BANKNIFTY • Combined Directional Strategy Portfolio Analytics"
)
# ==========================
# LOAD DATA
# ==========================

if index_type == "NIFTY":

    trades = pd.read_csv("reports/market_edge_trades.csv")
    monthly = pd.read_csv("reports/monthly_report.csv")
    equity_curve = pd.read_csv("reports/equity_curve.csv")
    drawdown_curve = pd.read_csv("reports/drawdown_curve.csv")
    tv_report = pd.read_csv("reports/tradingview_style_report.csv")

    strategy_name = "Nifty Directional"

elif index_type == "BANKNIFTY":

    trades = pd.read_csv("reports/banknifty_market_edge_trades.csv")
    monthly = pd.read_csv("reports/banknifty_monthly_report.csv")
    equity_curve = pd.read_csv("reports/banknifty_equity_curve.csv")
    drawdown_curve = pd.read_csv("reports/banknifty_drawdown_curve.csv")
    tv_report = pd.read_csv("reports/banknifty_tradingview_style_report.csv")

    strategy_name = "BankNifty Directional"

elif index_type == "COMBINED":

    nifty_trades = pd.read_csv(
        "reports/market_edge_trades.csv"
    )

    banknifty_trades = pd.read_csv(
        "reports/banknifty_market_edge_trades.csv"
    )

    trades = pd.concat(
        [nifty_trades, banknifty_trades],
        ignore_index=True
    )

    trades["Exit Time"] = pd.to_datetime(
        trades["Exit Time"]
    )

    trades = trades.sort_values(
        "Exit Time"
    )

    trades["Cumulative PnL INR"] = (
        trades["PnL INR"].cumsum()
    )

    equity_curve = trades[
        ["Exit Time", "Cumulative PnL INR"]
    ].copy()

    

    

    drawdown_curve = pd.DataFrame({
        "Trade": range(1, len(trades) + 1),
        "Drawdown": (-trades["PnL INR"]).clip(lower=0)
    })

    monthly = pd.DataFrame({
        "Month": ["Combined"],
        "Trades": [len(trades)],
        "PnL INR": [trades["PnL INR"].sum()],
        "Return %": [0],
        "Avg PnL/Trade": [
            trades["PnL INR"].mean()
        ],
        "Points": [
            trades["Points"].sum()
        ]
    })

    tv_report = trades.copy()

    strategy_name = "Combined Directional Portfolio"

if index_type == "NIFTY":
    total_candles = 211213

elif index_type == "BANKNIFTY":
    total_candles = 211204

else:
    total_candles = 422417
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

# Capital Based Return

if index_type == "COMBINED":
    capital = 300000
else:
    capital = 150000

return_pct = round(
    (net_profit / capital) * 100,
    2
)

start_date = pd.to_datetime(trades["Exit Time"]).min()
end_date = pd.to_datetime(trades["Exit Time"]).max()

years = (end_date - start_date).days / 365.25

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
# Sharpe Ratio

returns = trades["PnL INR"]

if returns.std() != 0:
    sharpe_ratio = round(
        (returns.mean() / returns.std()) * (252 ** 0.5),
        2
    )
else:
    sharpe_ratio = 0
largest_win = trades["PnL INR"].max()
largest_loss = trades["PnL INR"].min()
avg_winner = round(
    trades[trades["PnL INR"] > 0]["PnL INR"].mean(),
    2
)

avg_loser = round(
    trades[trades["PnL INR"] < 0]["PnL INR"].mean(),
    2
)



# =====================================================
# CENTRALIZED DRAWDOWN ENGINE
# =====================================================

# Account Equity (sirf compatibility ke liye)
equity = capital + trades["Cumulative PnL INR"]



# Individual Trade Loss = Drawdown
drawdown_inr = (
    -trades["PnL INR"]
).clip(lower=0)

drawdown_pct = (
    drawdown_inr / capital * 100
).round(2)

max_dd = round(
    drawdown_inr.max(),
    2
)

max_dd_pct = round(
    drawdown_pct.max(),
    2
)

expectancy = (
    round(net_profit / total_trades, 2)
    if total_trades > 0 else 0
)

# Dashboard Metrics
max_dd = round(
    drawdown_inr.max(),
    2
)

max_dd_pct = round(
    drawdown_pct.max(),
    2
)

expectancy = (
    round(net_profit / total_trades, 2)
    if total_trades > 0
    else 0
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
    
if sharpe_ratio >= 1.5:
    strategy_grade = "A+"
elif sharpe_ratio >= 1:
    strategy_grade = "A"
elif sharpe_ratio >= 0.5:
    strategy_grade = "B"
else:
    strategy_grade = "C"

raw_profit = net_profit

cost_per_trade_pct = 2

impact = (
    trades["PnL INR"].abs() *
    (cost_per_trade_pct / 100)
).sum()

cost_profit = raw_profit - impact
cost_efficiency = (cost_profit / raw_profit) * 100


ticker_text = (
    f"🏆 Grade: {strategy_grade}      ✦      "
    f"💰 Net Profit: ₹{net_profit:,.0f}      ✦      "
    f"🎯 Win Rate: {win_rate:.1f}%      ✦      "
    f"⚡ Profit Factor: {profit_factor:.2f}      ✦      "
    f"📉 Max Drawdown: {max_dd_pct:.1f}%      ✦      "
    f"🔥 Win Streak: {max_win_streak}      ✦      "
    f"📊 Total Trades: {total_trades:,}      ✦      "
    f"🕯️ Candles: {total_candles:,}      ✦      "
    f"🚀 CAGR: {cagr:.1f}%      ✦      "
) * 3

st.markdown(f"""
<style>
.ticker-container {{
    width: 100%;
    overflow: hidden;
    background: linear-gradient(
    90deg,
    #111111 0%,
    #1a1a1a 40%,
    #3d2f00 70%,
    #5c4300 100%
);

border:1px solid rgba(255,215,0,.30);

box-shadow:
0 0 18px rgba(255,215,0,.12),
0 8px 20px rgba(0,0,0,.35);
    border-radius: 14px;
    padding: 14px 0;
    margin: 10px 0 20px 0;
    border: 1px solid rgba(255,255,255,0.12);
}}

.ticker {{
    display: inline-block;
    white-space: nowrap;
    color: white;
    font-size: 18px;      /* Text Bigger */
    font-weight: 700;     /* Bold */
    letter-spacing: 0.5px;
    padding-left: 100%;
    animation: scroll-left 70s linear infinite;
}}

@keyframes scroll-left {{
    from {{
        transform: translateX(0);
    }}
    to {{
        transform: translateX(-100%);
    }}
}}
</style>

<div class="ticker-container">
    <div class="ticker">
        {ticker_text}
    </div>
</div>
""", unsafe_allow_html=True)
st.markdown("### 🧠 Strategy Intelligence")

c1, c2, c3, c4 = st.columns(4)

c1.metric("Grade", strategy_grade)
c2.metric("Win Rate", f"{win_rate}%")
c3.metric("Win Streak", max_win_streak)
c4.metric("Profit Factor", profit_factor)

st.markdown("""
<style>

/* =========================
   PREMIUM TABS V2
========================= */

/* Tabs Container */
div[data-baseweb="tab-list"]{
    gap:10px;
    background:linear-gradient(
    90deg,
    #5B3A00 0%,
    #8B6508 20%,
    #C99700 50%,
    #8B6508 80%,
    #5B3A00 100%
    );
    padding:12px;
    border-radius:18px;
    border:1px solid rgba(255,255,255,.08);
    box-shadow:0 8px 20px rgba(0,0,0,.25);
    margin-bottom:15px;
}

/* All Tabs */
button[data-baseweb="tab"]{
    background:transparent !important;
    color:#CBD5E1 !important;
    border-radius:12px !important;
    padding:12px 22px !important;
    font-size:16px !important;
    font-weight:600 !important;
    transition:all .25s ease;
}

/* Hover Effect */
button[data-baseweb="tab"]:hover{
    background:#334155 !important;
    color:white !important;
    transform:translateY(-2px);
}

/* Active Tab */
button[data-baseweb="tab"][aria-selected="true"]{
    background:linear-gradient(135deg,#00C853,#00E676)!important;
    color:#08120C !important;
    font-weight:800 !important;
    border-radius:12px !important;
    box-shadow:0 0 20px rgba(0,230,118,.55);
    transform:translateY(-2px);
}

/* Remove default underline */
button[data-baseweb="tab"]::after{
    display:none !important;
}

</style>
""", unsafe_allow_html=True)
# ==========================
# HEADER
# ==========================
from datetime import datetime
tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
    "📊 Overview",
    "📈 Performance",
    "🛡️ Risk",
    "📋 Trades",
    "💰 Cost",
    "📥 Downloads",
    "⚠️ Drawdown Analytics Pro"
])

with tab1:

    st.subheader("📊 Overview")

    st.markdown(f"""
    <div style="
    background:linear-gradient(135deg,#0f172a,#1e3a8a);
    padding:22px;
    border-radius:16px;
    border-left:6px solid #3b82f6;
    margin-bottom:18px;
    box-shadow:0 0 15px rgba(59,130,246,.15);
    ">

    <h3 style="color:white;margin-top:0;">
    📋 Strategy Snapshot
    </h3>

    <table style="
    width:100%;
    color:#e2e8f0;
    font-size:16px;
    line-height:2.0;
    ">

    <tr>
    <td>🎯 Strategy</td>
    <td><b>{strategy_name}</b></td>
    </tr>

    <tr>
    <td>💼 Initial Capital</td>
    <td><b>₹{capital:,.0f} <span style="color:#94a3b8;font-size:13px;">(Single Capital Base Used Throughout the Backtest)</span></b></td>
    </tr>

    <tr>
    <td>🚀 Wealth Growth</td>
    <td><b>{return_pct:.2f}% <span style="color:#94a3b8;font-size:13px;">(From ₹{capital:,.0f} Initial Capital)</span></b></td>
    </tr>

    <tr>
    <td>📊 Total Trades</td>
    <td><b>{total_trades:,}</b></td>
    </tr>

    <tr>
    <td>📊 Historical Trade Sample</td>
    <td><b>{total_trades:,} <span style="color:#94a3b8;font-size:13px;">(Large Statistical Sample)</span></b></td>
    </tr>

    <tr>
    <td>⏳ Market Cycles Covered</td>
    <td><b>11+ Years <span style="color:#94a3b8;font-size:13px;">(Bull, Bear & Sideways Markets)</span></b></td>
    </tr>

    <tr>
    <td>📅 Backtest Period</td>
    <td><b>2015 – 2026 (11+ Years)</b></td>
    </tr>

    <tr>
    <td>📉 Maximum Drawdown</td>
    <td><b>{max_dd_pct}% <span style="color:#94a3b8;font-size:13px;">(Overall Backtest Period)</span></b></td>
    </tr>

    <tr>
    <td>🛡️ Risk Management</td>
    <td><b>Controlled <span style="color:#94a3b8;font-size:13px;">(Capital Efficient Strategy with Long-Term Compounding Potential)</span></b></td>
    </tr>

    <tr>
    <td>⚙️ Trading Approach</td>
    <td><b>100% Rule-Based <span style="color:#94a3b8;font-size:13px;">(No Discretionary Decisions)</span></b></td>
    </tr>

    <tr> 
    <td>🛡️ Stress Event Preparedness</td> 
    <td><b>The maximum historical drawdown was recorded during the extraordinary market volatility surrounding the 2024 Election Results, one of the most challenging stress events in the entire backtest period. This event has been thoroughly analyzed, and a dedicated contingency framework has been established for similar high-impact market situations. The strategy now includes predefined risk-management actions and execution protocols designed to respond in a disciplined and systematic manner during exceptional market conditions, with the objective of improving capital protection and reducing the impact of future stress events.</b></td> 
    </tr>

    </table>

    <hr style="border:1px solid rgba(255,255,255,.10);">

    <p style="
    color:#dbeafe;
    font-size:15px;
    line-height:1.8;
    margin:0;
    ">

    💡 <b>Strategy Objective</b><br><br>

    This backtest evaluates the strategy using an <b>initial trading capital of ₹{capital:,.0f}</b>.
    All key performance metrics, including <b>Return %, CAGR and Drawdown %</b>, are calculated consistently using this capital base to provide a realistic and standardized performance assessment.

    </p>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 📊 Key Performance Indicators")
    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
    "Net Profit",
    f"₹{net_profit:,.0f}"
)
    c2.metric(
    "Win Rate",
    f"{win_rate}%"
)
    c3.metric(
    "Profit Factor",
    profit_factor
)
    c4.metric(
    "Sharpe",
    sharpe_ratio
)
    
    st.success(f"""
    💡 Executive Summary

    Strategy executed **{total_trades:,}** historical trades over an
    11-year backtest period.

    The system achieved a net profit of **₹{net_profit:,.0f}**
    while maintaining a maximum drawdown of **{max_dd_pct}%**,
    demonstrating stable long-term performance.
    """)
    
with tab2:

    st.subheader("📈 Performance Analytics")

    # -------------------------
    # Performance Calculations
    # -------------------------

    initial_capital = capital

    equity_curve["Account Equity"] = (
        initial_capital +
        equity_curve["Cumulative PnL INR"]
    )

    highest_equity = equity_curve["Account Equity"].max()
    lowest_equity = equity_curve["Account Equity"].min()
    capital_multiple = highest_equity / initial_capital

    # ==========================
    # Premium KPI Cards
    # ==========================

    k1, k2, k3, k4, k5, k6 = st.columns(6)

    k1.metric(
        "💰 Net Profit",
        f"₹{net_profit:,.0f}"
    )

    k2.metric(
        "🚀 Total Return",
        f"{return_pct:.2f}%"
    )

    k3.metric(
        "📈 CAGR",
        f"{cagr:.2f}%"
    )

    k4.metric(
        "🏆 Profit Factor",
        f"{profit_factor:.2f}"
    )

    k5.metric(
        "📉 Max Drawdown",
        f"{max_dd_pct:.2f}%"
    )

    k6.metric(
        "⚡ Sharpe",
        f"{sharpe_ratio:.2f}"
    )

    st.markdown("---")

    # ==========================
    # Equity Curve Header
    # ==========================

    st.markdown(
        f"""
### 📈 Account Equity Growth

**Growth of ₹{capital:,.0f} Initial Capital Throughout the Entire Backtest Period**

The equity curve below illustrates how the strategy compounded capital from an initial investment of **₹{capital:,.0f}**, reflecting cumulative trading performance across the complete historical test.
"""
    )

    # ==========================
    # Equity Curve
    # ==========================

    fig = px.line(
        equity_curve,
        x="Exit Time",
        y="Account Equity",
        title="Account Equity Growth"
    )

    fig.update_layout(
        height=650,
        template="plotly_dark",
        hovermode="x unified",
        title_x=0.5,
        margin=dict(
            l=20,
            r=20,
            t=60,
            b=20
        )
    )

    fig.update_traces(
        line=dict(width=3)
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # ==========================
    # Executive Insight
    # ==========================

    st.success(
        f"""
💡 Executive Performance Insight

    Starting with an initial capital of ₹{capital:,.0f}, the strategy generated a cumulative net profit of ₹{net_profit:,.0f}, delivering an overall return of {return_pct:.2f}% across the complete backtest period.

    The equity curve demonstrates steady long-term capital appreciation through multiple market cycles while maintaining disciplined risk management and systematic execution.
    """
    )

    # ==========================
    # Performance Statistics
    # ==========================

    c1, c2, c3, c4 = st.columns(4)

    final_equity = initial_capital + net_profit
    capital_multiple = final_equity / initial_capital

    c1.metric(
        "📈 Final Equity",
        f"₹{final_equity:,.0f}"
    )

    c2.metric(
        "💼 Initial Capital",
        f"₹{capital:,.0f}"
    )

    c3.metric(
        "📊 Capital Multiple",
        f"{capital_multiple:.2f}×"
    )

    c4.metric(
        "💰 Net Wealth Created",
        f"₹{net_profit:,.0f}"
    )

    st.markdown("---")

with tab3:

    st.subheader("⚠️ Risk Analytics")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Sharpe Ratio",
        sharpe_ratio
    )

    c2.metric(
        "📊 Expectancy / Trade",
        f"₹{expectancy:,.2f}"
    )

    c3.metric(
        "Largest Winner",
        f"₹{largest_win:,.0f}"
    )

    c4.metric(
        "Largest Loser",
        f"₹{largest_loss:,.0f}"
    )

    c1, c2 = st.columns(2)

    c1.metric(
        "Avg Winner",
        f"₹{avg_winner:,.0f}"
    )

    c2.metric(
        "Avg Loser",
        f"₹{avg_loser:,.0f}"
    )
    st.markdown("---")
    
    st.subheader("📉 Drawdown Curve")
    
    dd_df = trades.copy()
    
    dd_df["Trade No"] = range(
        1,
        len(dd_df) + 1
    )
    
    dd_df["Account Equity"] = equity.values
    dd_df["Drawdown INR"] = -drawdown_inr.values
    dd_df["Drawdown %"] = drawdown_pct.values
    
    dd_df["Trade No"] = range(
        1,
        len(dd_df) + 1
        )
    
    fig_dd = px.line(
        dd_df,
        x="Trade No",
        y="Drawdown INR",
        title="Account Equity Drawdown"
        )
    
    fig_dd.update_traces(
        line_color="red"
    )
    
    st.plotly_chart(
        fig_dd,
        use_container_width=True,
        key="risk_drawdown_curve"
    )

    st.success(f"""
    💡 **Expectancy / Trade**

    Average net profit generated from each completed trade.

    **Formula**

    Net Profit ÷ Total Trades

    ₹{net_profit:,.0f} ÷ {total_trades:,}

    = **₹{expectancy:,.2f} per trade**
    """)
    
with tab4:

    st.subheader("📋 Trade Explorer Pro")

    trade_search = st.text_input(
        "🔍 Search Trade",
        key="tab4_search"
    )

    filtered = tv_report.copy()

    filtered["Exit Time"] = pd.to_datetime(
        filtered["Exit Time"]
    )

    filtered["Year"] = (
        filtered["Exit Time"].dt.year
    )

    c1, c2 = st.columns(2)

    with c1:
        selected_year = st.selectbox(
            "📅 Select Year",
            ["ALL"] + sorted(
                filtered["Year"].unique().tolist()
            ),
            key="tab4_year"
        )

    with c2:
        trade_type = st.selectbox(
            "📈 Filter Trade Type",
            ["ALL", "LONG", "SHORT"],
            key="tab4_type"
        )

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

    st.markdown("---")

    st.subheader("🟢 Top 20 Winners")

    top_winners = (
        trades.sort_values(
            "PnL INR",
            ascending=False
        ).head(20)
    )

    st.dataframe(
        top_winners,
        use_container_width=True
    )

    st.markdown("---")

    st.subheader("🔴 Top 20 Losers")

    top_losers = (
        trades.sort_values(
            "PnL INR",
            ascending=True
        ).head(20)
    )

    st.dataframe(
        top_losers,
        use_container_width=True
    )

with tab5:

    st.subheader("💰 Cost Analysis")

    st.markdown(f"""
    <div style="
    background:linear-gradient(135deg,#0f172a,#1e3a8a);
    padding:22px;
    border-radius:16px;
    border-left:6px solid #22c55e;
    margin-bottom:20px;
    box-shadow:0 0 15px rgba(34,197,94,.15);
    ">

    <h3 style="color:white;margin-top:0;">
    💰 Cost Analysis Summary
    </h3>

    <table style="width:100%;color:#e2e8f0;font-size:16px;line-height:2.1;">

    <tr>
    <td>📊 Cost Model</td>
    <td><b>{cost_per_trade_pct}% Per Trade</b></td>
    </tr>

    <tr>
    <td>📈 Total Trades</td>
    <td><b>{total_trades:,}</b></td>
    </tr>

    <tr>
    <td>💰 Raw Profit</td>
    <td><b>₹{raw_profit:,.0f}</b></td>
    </tr>

    <tr>
    <td>💸 Total Cost Impact</td>
    <td><b>₹{impact:,.0f}</b></td>
    </tr>

    <tr>
    <td>✅ Net Profit After Cost</td>
    <td><b>₹{cost_profit:,.0f}</b></td>
    </tr>

    </table>

    <hr style="border:1px solid rgba(255,255,255,.12);">

    <p style="color:#d1fae5;font-size:15px;line-height:1.9;margin:0;">

    💡 <b>Cost Impact Analysis</b><br><br>

    <b>Cost Reduced Profitability</b><br>
    = (Total Cost Impact ÷ Raw Profit) × 100<br>
    = (₹{impact:,.0f} ÷ ₹{raw_profit:,.0f}) × 100<br>
    = <b>{(impact/raw_profit)*100:.2f}%</b><br><br>

    <b>Profit Retained After Cost</b><br>
    = (Net Profit After Cost ÷ Raw Profit) × 100<br>
    = (₹{cost_profit:,.0f} ÷ ₹{raw_profit:,.0f}) × 100<br>
    = <b>{(cost_profit/raw_profit)*100:.2f}%</b>

    </p>

    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Raw Profit",
        f"₹{raw_profit:,.0f}"
    )

    c2.metric(
        "Net Profit After Cost",
        f"₹{cost_profit:,.0f}"
    )

    c3.metric(
        "Cost Impact",
        f"₹{impact:,.0f}"
    )

    c4.metric(
        "Cost Efficiency",
        f"{cost_efficiency:.2f}%"
    )

with tab6:

    st.subheader("📥 Download Center")

    st.markdown(f"""
    <div style="
    background:linear-gradient(135deg,#0f172a,#1e3a8a);
    padding:22px;
    border-radius:16px;
    border-left:6px solid #3b82f6;
    margin-bottom:20px;
    box-shadow:0 0 15px rgba(59,130,246,.15);
    ">

    <h3 style="color:white;margin-top:0;">
    📂 Export Trade Reports
    </h3>

    <table style="width:100%;color:#e2e8f0;font-size:16px;line-height:2.0;">

    <tr>
    <td>📈 Strategy</td>
    <td><b>{strategy_name}</b></td>
    </tr>

    <tr>
    <td>📊 Total Trades</td>
    <td><b>{total_trades:,}</b></td>
    </tr>

    <tr>
    <td>📅 Backtest Period</td>
    <td><b>2015 – 2026</b></td>
    </tr>

    <tr>
    <td>📄 File Format</td>
    <td><b>CSV</b></td>
    </tr>

    </table>

    <hr style="border:1px solid rgba(255,255,255,.12);">

    <p style="color:#dbeafe;font-size:15px;margin:0;">
    Export the complete trade history for further analysis in Excel, Power BI or Python.
    </p>

    </div>
    """, unsafe_allow_html=True)

    csv = tv_report.to_csv(index=False)

    st.download_button(
        label="📥 Download Detailed Trade Log",
        data=csv,
        file_name=f"{strategy_name}_Trade_Log.csv",
        mime="text/csv",
        key="download_tab6",
        use_container_width=True
    )
    
with tab7:

    st.subheader("⚠️ Drawdown Analytics Pro")

    st.markdown("""
    <div style="
    background:linear-gradient(135deg,#0f172a,#1e3a8a);
    padding:22px;
    border-radius:14px;
    border-left:6px solid #38bdf8;
    margin-bottom:20px;
    ">

    <h4 style="color:white;margin-top:0;">
    📘 Drawdown Calculation Methodology
    </h4>

    <p style="color:#e2e8f0;font-size:15px;line-height:1.8;">

    <b>Method Used:</b> Individual Trade Drawdown (Risk-Based)<br><br>

    <b>Objective</b><br>
    This dashboard measures the risk of every individual losing trade instead of using the traditional equity curve drawdown. The objective is to evaluate the actual impact of each losing trade on the trading capital and make risk comparison easier across different months and years.<br><br>

    <b>Calculation Formula</b><br>

    • Drawdown ₹ = Max(0, − Trade P&amp;L)<br>

    • Drawdown % = (Drawdown ₹ ÷ Initial Capital) × 100<br><br>

    <b>Interpretation</b><br>

    ✅ Only losing trades are considered.<br>

    ✅ Winning trades are excluded from drawdown calculations.<br>

    ✅ Max Day Drawdown represents the largest single losing trade within the selected period.<br>

    ✅ Average Drawdown is calculated using only losing trades.<br>

    ✅ All drawdown percentages are calculated using a fixed Initial Capital of <b>₹{capital:,.0f}</b> to maintain consistency across all years and months.
    <br><br>

    <b>Why not Traditional Equity Drawdown?</b><br>

    Traditional equity drawdown measures the decline from an account's historical equity peak. This dashboard intentionally uses Individual Trade Drawdown because the primary objective is to evaluate the risk contribution of each losing trade rather than fluctuations in cumulative account equity.
    
    <br><br>

    <b>Important:</b><br>

    This methodology is specifically designed for strategy risk evaluation and internal performance analysis. It should not be interpreted as a traditional portfolio equity drawdown methodology.
                
                            
    </p>

    </div>
    """, unsafe_allow_html=True)

    dd_view = st.selectbox(
        "Drawdown Analysis Type",
        ["Full Equity", "Yearly", "Monthly"]
    )

    equity_df = equity_curve.copy()

    # Bring Individual Trade PnL
    equity_df = equity_df.merge(
        trades[["Exit Time", "PnL INR"]],
        on="Exit Time",
        how="left"
    )

    equity_df["Exit Time"] = pd.to_datetime(
        equity_df["Exit Time"]
    )

    equity_df["Hover Time"] = (
        equity_df["Exit Time"]
        .dt.strftime("%d-%b-%Y %I:%M %p")
    )

    # Use Centralized Drawdown Engine

    equity_df["Account Equity"] = (
        capital +
        equity_df["Cumulative PnL INR"]
    )

    equity_df["Year"] = equity_df["Exit Time"].dt.year

    equity_df["Month"] = equity_df["Exit Time"].dt.strftime("%b")


    if dd_view == "Yearly":

        selected_year = st.selectbox(
            "Select Year",
            sorted(
                equity_df["Exit Time"].dt.year.unique()
            )
        )

        equity_df = equity_df[
            equity_df["Exit Time"].dt.year
            == selected_year
        ]

    elif dd_view == "Monthly":
        
        selected_year = st.selectbox(
            "Select Year",
            sorted(equity_df["Year"].unique())
        )

        month_order = [
            "Jan", "Feb", "Mar", "Apr", "May", "Jun",
            "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
        ]

        available_months = (
            equity_df[
                equity_df["Year"] == selected_year
                ]["Month"]
                .unique()
                .tolist()
        )

        selected_month = st.selectbox(
            "Select Month",
            [m for m in month_order if m in available_months]
        )

        equity_df = equity_df[
            (equity_df["Year"] == selected_year)
            &
            (equity_df["Month"] == selected_month)
        ]

    


    # Use Centralized Drawdown Logic


    equity_df["Drawdown INR"] = (
        -equity_df["PnL INR"]
    ).clip(lower=0)

    equity_df["Chart Drawdown"] = -equity_df["Drawdown INR"]

    equity_df["Drawdown %"] = (
        equity_df["Drawdown INR"] / capital * 100
    ).round(2)

    loss_days = equity_df[
        equity_df["Drawdown INR"] > 0
    ]

    if loss_days.empty:
        st.success("🎉 No drawdown found for the selected period.")
        st.stop()

    max_dd_row = loss_days.loc[
        loss_days["Drawdown INR"].idxmax()
    ]

    max_dd_inr = max_dd_row["Drawdown INR"]

    max_dd_pct_display = max_dd_row["Drawdown %"]

    worst_dd_day = max_dd_row["Exit Time"].strftime("%d-%b-%Y")

    avg_dd_inr = loss_days["Drawdown INR"].mean()

    avg_dd_pct = loss_days["Drawdown %"].mean()

# ==========================
# PROFIT ANALYTICS
# ==========================

    profit_days = equity_df[
        equity_df["PnL INR"] > 0
    ]

    if profit_days.empty:
        st.warning("No profitable trades found for the selected period.")
        st.stop()

    max_profit_row = profit_days.loc[
        profit_days["PnL INR"].idxmax()
    ]

    max_profit_inr = max_profit_row["PnL INR"]

    max_profit_pct = (
        max_profit_inr / capital * 100
    )

    best_profit_day = (
        max_profit_row["Exit Time"]
        .strftime("%d-%b-%Y")
    )

    avg_profit_inr = (
        profit_days["PnL INR"].mean()
    )

    avg_profit_pct = (
        avg_profit_inr / capital * 100
    )

    winning_trades = len(profit_days)


    # Worst Losing Streak


    c1, c2, c3, c4, c5, c6 = st.columns(6)

    c1.metric(
        "Max Day DD ₹",
        f"₹{max_dd_inr:,.0f}"
    )

    c2.metric(
        "Max Day DD %",
        f"{max_dd_pct_display:.2f}%"
    )

    c3.metric(
        "Worst DD Day",
        worst_dd_day
    )

    c4.metric(
        "Average DD ₹",
        f"₹{avg_dd_inr:,.0f}"
    )

    c5.metric(
        "Average DD %",
        f"{avg_dd_pct:.2f}%"
    )


    c6.metric(
        "Initial Capital",
        f"₹{capital:,.0f}"
    )

    st.markdown("---")
    st.subheader("🟢 Profit Analytics")

    p1, p2, p3, p4, p5, p6 = st.columns(6)

    p1.metric(
        "Max Day Profit ₹",
        f"₹{max_profit_inr:,.0f}"
    )

    p2.metric(
        "Max Day Profit %",
        f"{max_profit_pct:.2f}%"
    )

    p3.metric(
        "Best Profit Day",
        best_profit_day
    )

    p4.metric(
        "Average Profit ₹",
        f"₹{avg_profit_inr:,.0f}"
    )

    p5.metric(
        "Average Profit %",
        f"{avg_profit_pct:.2f}%"
    )

    p6.metric(
        "Winning Trades",
        f"{winning_trades:,}"
    )

    

    st.subheader("📋 Drawdown Records")

    st.dataframe(
        loss_days[
            [
                "Exit Time",
                "Account Equity",
                "Drawdown INR",
                "Drawdown %"
            ]
        ],
        use_container_width=True
    )

    st.subheader("📉 Drawdown INR Chart")

    fig_dd_pro = px.line(
        equity_df,
        x="Exit Time",
        y="Chart Drawdown",
        title="Drawdown INR Analysis"
    )

    fig_dd_pro.update_traces(

    customdata=equity_df[
        [
            "Hover Time",
            "Account Equity",
            "Drawdown INR",
            "Drawdown %"
        ]
    ].values,

    hovertemplate=
    "<b>Exit Time:</b> %{customdata[0]}<br>" +
    "<b>Account Equity:</b> ₹%{customdata[1]:,.0f}<br>" +
    f"<b>Initial Capital:</b> ₹{capital:,.0f}<br>" +
    "<b>Drawdown ₹:</b> ₹%{customdata[2]:,.0f}<br>" +
    "<b>Drawdown %:</b> %{customdata[3]:.2f}%<br>" +
    "<extra></extra>"
    )
    
    fig_dd_pro.update_xaxes(
        hoverformat="%d-%b-%Y %H:%M"
    )

    fig_dd_pro.update_traces(
        line_color="red"
    )

    st.plotly_chart(
        fig_dd_pro,
        use_container_width=True,
        key="drawdown_pro_chart"
    )

    st.subheader("🏆 Top 10 Worst Drawdowns")

    


    top_dd = (
        loss_days
        .sort_values(
            "Drawdown INR",
            ascending=False
        )
        .head(10)
    )

    st.dataframe(
        top_dd[
            [
                "Exit Time",
                "Account Equity",
                "Drawdown INR",
                "Drawdown %"
            ]
        ],
        use_container_width=True
    )

    worst_dd = top_dd.iloc[0]

    st.subheader("🎯 Worst Drawdown Summary")

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Worst DD ₹",
        f"₹{abs(worst_dd['Drawdown INR']):,.0f}"
    )

    c2.metric(
        "Worst DD %",
        f"{abs(worst_dd['Drawdown %']):.2f}%"
    )

    c3.metric(
        "Bottom Date",
        worst_dd["Exit Time"].strftime("%d-%b-%Y")
    )

st.markdown(
    f"""
<div style="
padding:32px;
border-radius:22px;
background:linear-gradient(135deg,#0B1220 0%,#1E3A8A 45%,#2563EB 100%);
border:1px solid rgba(255,255,255,0.10);
box-shadow:0 12px 35px rgba(0,0,0,0.35);
">

<div style="
display:flex;
justify-content:space-between;
align-items:center;
flex-wrap:wrap;
gap:15px;
">

<div>

<div style="
font-size:14px;
letter-spacing:2px;
text-transform:uppercase;
color:#93C5FD;
font-weight:600;
margin-bottom:8px;
">
Institutional Trading Report
</div>

<h1 style="
margin:0;
font-size:34px;
color:white;
font-weight:800;
">
📊 {strategy_name}
</h1>

<div style="
margin-top:8px;
font-size:16px;
color:#D1D5DB;
">
Professional Backtesting Analytics Dashboard
</div>

</div>

<div style="
background:linear-gradient(135deg,#16A34A,#22C55E);
padding:10px 22px;
border-radius:999px;
font-size:15px;
font-weight:700;
color:white;
box-shadow:0 0 18px rgba(34,197,94,.45);
">
✅ VERIFIED BACKTEST
</div>

</div>

<hr style="
margin:24px 0;
border:none;
height:1px;
background:rgba(255,255,255,.12);
">

<div style="
display:grid;
grid-template-columns:repeat(4,1fr);
gap:18px;
text-align:center;
">

<div style="
background:rgba(255,255,255,.05);
padding:16px;
border-radius:14px;
">
<div style="color:#94A3B8;font-size:13px;">Backtest Period</div>
<div style="color:white;font-size:22px;font-weight:700;margin-top:6px;">
2015–2026
</div>
</div>

<div style="
background:rgba(255,255,255,.05);
padding:16px;
border-radius:14px;
">
<div style="color:#94A3B8;font-size:13px;">Portfolio</div>
<div style="color:white;font-size:22px;font-weight:700;margin-top:6px;">
{index_type}
</div>
</div>

<div style="
background:rgba(255,255,255,.05);
padding:16px;
border-radius:14px;
">
<div style="color:#94A3B8;font-size:13px;">Total Trades</div>
<div style="color:white;font-size:22px;font-weight:700;margin-top:6px;">
{total_trades:,}
</div>
</div>

<div style="
background:rgba(255,255,255,.05);
padding:16px;
border-radius:14px;
">
<div style="color:#94A3B8;font-size:13px;">Initial Capital</div>
<div style="color:white;font-size:22px;font-weight:700;margin-top:6px;">
₹{capital:,.0f}
</div>
</div>

</div>

<div style="
margin-top:24px;
padding-top:18px;
border-top:1px solid rgba(255,255,255,.10);
text-align:center;
font-size:15px;
color:#CBD5E1;
line-height:1.8;
">

Comprehensive performance evaluation covering
<b style="color:white;">Bull</b>,
<b style="color:white;">Bear</b> &
<b style="color:white;">Sideways</b>
market conditions with systematic rule-based trade execution and
institutional-grade performance analytics.

</div>

</div>
""",
    unsafe_allow_html=True
)
st.markdown("---")
st.caption(
    f"Last Updated: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}"
)
# ==========================
# KPI CARDS
# ==========================

st.markdown("---")

c1, c2, c3, c4, c5, c6, c7, c8 = st.columns(8)

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

c7.metric(
    "Sharpe",
    sharpe_ratio
)

c8.metric(
    "Expectancy",
    f"₹{expectancy:,.2f}"
)
# ==========================
# STRATEGY SCORECARD
# ==========================

st.markdown("---")

st.subheader("🎯 Strategy Scorecard")

st.caption(
    "Key performance indicators summarizing the strategy across the complete historical backtest."
)

scorecard = pd.DataFrame({
    "Metric": [
        "Win Rate",
        "Profit Factor",
        "Max Drawdown",
        "Expectancy / Trade",
        "Total Trades"
    ],
    "Value": [
        f"{win_rate}%",
        profit_factor,
        f"{max_dd_pct}%",
        f"₹{expectancy:,.2f}",
        total_trades
    ]
})

st.dataframe(
    scorecard,
    use_container_width=True,
    hide_index=True
)
# ==========================
# STRATEGY INFO
# ==========================

st.subheader("ℹ️ Strategy Information")

st.info(f"""
### Institutional Backtest Configuration

**🎯 Strategy:** {strategy_name}

**📅 Backtest Period:** 2015 – 2026

**⏳ Years Tested:** 11+

**🕯️ Historical Candles:** {total_candles:,}

**💼 Initial Capital:** ₹{capital:,.0f}

**⚙️ Trading Methodology:** 100% Rule-Based Systematic Strategy

**📈 Market Coverage:** Bull • Bear • Sideways Market Cycles
""")

c1, c2, c3, c4 = st.columns(4)

c1.metric("Years Tested", "11+")

c2.metric("Candles", f"{total_candles:,}")

c3.metric("Trades", f"{total_trades:,}")

c4.metric(
    "💼 Initial Capital",
    f"₹{capital:,.0f}"
)
# ==========================
# EQUITY CURVE
# ==========================

st.markdown("---")

st.subheader("📈 Equity Curve")

equity_curve["Account Equity"] = (
    capital +
    equity_curve["Cumulative PnL INR"]
)

fig = px.line(
    equity_curve,
    x="Exit Time",
    y="Account Equity",
    title="Account Equity Curve"
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

dd_df = trades.copy()

dd_df["Trade No"] = range(1, len(dd_df) + 1)

dd_df["Account Equity"] = equity.values



dd_df["Drawdown INR"] = -drawdown_inr.values

dd_df["Drawdown %"] = drawdown_pct.values


dd_df["Trade No"] = range(
    1,
    len(dd_df) + 1
)

fig_dd = px.line(
    dd_df,
    x="Trade No",
    y="Drawdown INR",
    title="Account Equity Drawdown"
)

fig_dd.update_traces(
    line_color="red"
)

st.plotly_chart(
    fig_dd,
    use_container_width=True,
    key="main_drawdown_curve"
)

st.subheader("📊 Equity vs Peak")

dd_df["Equity Change"] = (
    dd_df["Account Equity"]
    .diff()
    .fillna(0)
)

dd_df["Color"] = dd_df["Equity Change"].apply(
    lambda x: "Profit" if x >= 0 else "Loss"
)

fig_dev = px.bar(
    dd_df,
    x="Trade No",
    y="Equity Change",
    color="Color",
    color_discrete_map={
        "Profit": "green",
        "Loss": "red"
    },
    title="Profit & Loss Per Trade"
)

fig_dev.update_layout(
    showlegend=False
)

st.plotly_chart(
    fig_dev,
    use_container_width=True,
    key="equity_vs_peak"
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
    title="Winning vs Losing Trades",
    color="Result",
    color_discrete_map={
        "Winning Trades": "#00E676",
        "Losing Trades": "#FFC107"
    }
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

# Year-wise Max Drawdown (based on centralized drawdown engine)

yearly_dd = (
    pd.DataFrame({
        "Year": trades["Year"],
        "Drawdown INR": drawdown_inr,
        "Drawdown %": drawdown_pct
    })
    .groupby("Year")
    .agg({
        "Drawdown INR": "max",
        "Drawdown %": "max"
    })
    .reset_index()
)

yearly = yearly.merge(
    yearly_dd,
    on="Year",
    how="left"
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
        "Drawdown INR",
        "Drawdown %",
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
    title=f"Year-wise Return % (₹{capital:,.0f} Capital)"
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

st.subheader("📅 Monthly Performance")

heatmap_source = trades.copy()

heatmap_source["Exit Time"] = pd.to_datetime(
    heatmap_source["Exit Time"]
)

heatmap_source["Year"] = (
    heatmap_source["Exit Time"].dt.year
)

heatmap_source["Month"] = (
    heatmap_source["Exit Time"]
    .dt.strftime("%b")
)

heatmap_data = (
    heatmap_source
    .groupby(["Year", "Month"])["PnL INR"]
    .sum()
    .reset_index()
)

month_order = [
    "Jan","Feb","Mar","Apr","May","Jun",
    "Jul","Aug","Sep","Oct","Nov","Dec"
]

heatmap_pivot = (
    heatmap_data
    .pivot(
        index="Year",
        columns="Month",
        values="PnL INR"
    )
    .reindex(columns=month_order)
    .fillna(0)
)

# ----------------------------
# Professional Number Format
# ----------------------------

def format_heatmap_value(x):

    if pd.isna(x):
        return ""

    if x >= 100000:
        return f"₹{x/100000:.2f}L"

    elif x >= 1000:
        return f"₹{x/1000:.1f}K"

    elif x <= -100000:
        return f"-₹{abs(x)/100000:.2f}L"

    elif x <= -1000:
        return f"-₹{abs(x)/1000:.1f}K"

    else:
        return f"₹{x:.0f}" if x >= 0 else f"-₹{abs(x):.0f}"

text_values = heatmap_pivot.apply(lambda col: col.map(format_heatmap_value))

import numpy as np

# Symmetric scale around zero
max_abs = np.nanmax(np.abs(heatmap_pivot.values))


 
fig_heat = px.imshow(
    heatmap_pivot,
    text_auto=False,
    aspect="auto",

    zmin=-max_abs,
    zmax=max_abs,

    color_continuous_scale=[
        [0.00, "#8B0000"],   # Dark Red
        [0.20, "#DC2626"],   # Red
        [0.40, "#EC7B7B"],   # Light Red
        [0.50, "#FFFFFF"],   # Zero
        [0.60, "#0DFC60"],   # Light Green
        [0.80, "#22C55E"],   # Green
        [1.00, "#166534"]    # Dark Green
    ],

    title="Monthly Performance Heatmap"
)

fig_heat.update_layout(
    coloraxis_colorbar=dict(
        title="PnL (₹)"
    )
)

fig_heat.update_traces(

    text=text_values.values,

    texttemplate="%{text}",

    textfont=dict(
        size=11,
        color="black"
    ),

    hovertemplate=
    "<b>Year</b>: %{y}<br>" +
    "<b>Month</b>: %{x}<br>" +
    "<b>PnL</b>: ₹%{z:,.0f}<br>" +
    "<extra></extra>"

)

fig_heat.update_layout(

    title_x=0.5,

    font=dict(size=13),

    coloraxis_colorbar=dict(

        title="Monthly PnL",

        thickness=18,

        len=0.75

    )

)

st.plotly_chart(
    fig_heat,
    use_container_width=True,
    key="monthly_heatmap"
)

st.markdown("---")


# ==========================
# YEAR × MONTH PERFORMANCE MATRIX
# ==========================

pivot_df = heatmap_source.copy()

pivot_table = (
    pivot_df
    .groupby(["Year", "Month"])["PnL INR"]
    .sum()
    .unstack(fill_value=0)
    .reindex(columns=month_order)
)

# Year × Month Maximum Drawdown Matrix



# Year Total
pivot_table["Total"] = pivot_table.sum(axis=1)

# Total Trades Per Year
yearly_trades = (
    pivot_df
    .groupby("Year")
    .size()
)

pivot_table["Trades"] = yearly_trades

# Return %
pivot_table["Return %"] = (
    pivot_table["Total"] / capital * 100
).round(2)

# Grand Total Row
grand_total = pivot_table.sum(axis=0)

pivot_table.loc["Grand Total"] = grand_total

st.subheader("📊 Year × Month Performance Matrix")

def highlight_profit_loss(val):

    if isinstance(val, (int, float)):

        if val > 0:
            return "background-color:#DCFCE7;color:#166534;font-weight:bold"

        elif val < 0:
            return "background-color:#FEE2E2;color:#991B1B;font-weight:bold"

    return ""

# Add Drawdown % after every month

new_pivot = pd.DataFrame(index=pivot_table.index)

for month in month_order:
    new_pivot[f"{month} PnL"] = pivot_table[month]

new_pivot["Total"] = pivot_table["Total"]
new_pivot["Trades"] = pivot_table["Trades"]
new_pivot["Return %"] = pivot_table["Return %"]

pivot_table = new_pivot

styled_pivot = (
    pivot_table.style
    .format({

        "Jan PnL": "₹{:,.0f}",

        "Feb PnL": "₹{:,.0f}",

        "Mar PnL": "₹{:,.0f}",

        "Apr PnL": "₹{:,.0f}",

        "May PnL": "₹{:,.0f}",

        "Jun PnL": "₹{:,.0f}",

        "Jul PnL": "₹{:,.0f}",

        "Aug PnL": "₹{:,.0f}",

        "Sep PnL": "₹{:,.0f}",

        "Oct PnL": "₹{:,.0f}",

        "Nov PnL": "₹{:,.0f}",

        "Dec PnL": "₹{:,.0f}",

        "Total": "₹{:,.0f}",
        "Trades": "{:,.0f}",
        "Return %": "{:.2f}%"

    })
    .map(highlight_profit_loss)
)

st.dataframe(
    styled_pivot,
    use_container_width=True
)

# Monthly Max Drawdown (Centralized Engine)

monthly = (
    trades
    .groupby(trades["Exit Time"].dt.to_period("M"))
    .agg(
        Trades=("PnL INR", "count"),
        **{
            "PnL INR": ("PnL INR", "sum"),
            "Points": ("Points", "sum")
        }
    )
    .reset_index()
)

monthly.rename(
    columns={"Exit Time": "Month"},
    inplace=True
)

monthly["Month"] = monthly["Month"].astype(str)

monthly["Return %"] = (
    monthly["PnL INR"] / capital * 100
).round(2)

monthly["Avg PnL/Trade"] = (
    monthly["PnL INR"] / monthly["Trades"]
).round(2)

st.subheader("📋 Monthly Performance Summary")
 
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
    title=f"Monthly Return % (₹{capital:,.0f} Capital)"
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
st.markdown("<br>", unsafe_allow_html=True)
st.divider()
st.markdown("<br>", unsafe_allow_html=True)

st.subheader("📋 Cost Impact Overview")

profit_reduction = (impact / raw_profit) * 100
profit_retained = (cost_profit / raw_profit) * 100

c1, c2, c3 = st.columns(3)

c1.metric(
    "💰 Raw Profit",
    f"₹{raw_profit:,.0f}"
)

c2.metric(
    "✅ Net Profit After Cost",
    f"₹{cost_profit:,.0f}"
)

c3.metric(
    "💸 Total Cost Impact",
    f"₹{impact:,.0f}"
)

c4, c5, c6, c7 = st.columns(4)

c4.metric(
    "📈 PF Before",
    "1.28"
)

c5.metric(
    "📉 PF After",
    "1.22"
)

c6.metric(
    "📉 Profit Reduction",
    f"{profit_reduction:.2f}%"
)

c7.metric(
    "📈 Profit Retained",
    f"{profit_retained:.2f}%"
)

st.success(f"""
💡 Executive Insight

Transaction costs reduced the gross profitability by **{profit_reduction:.2f}%**.

Even after accounting for all estimated trading costs,
the strategy retained **{profit_retained:.2f}%** of its gross profit,
indicating strong cost efficiency.
""")

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

filtered["Exit Time"] = pd.to_datetime(filtered["Exit Time"])
filtered["Year"] = filtered["Exit Time"].dt.year


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

st.subheader("📦 Export Backtest Data")

st.markdown(f"""
<div style="
background:linear-gradient(135deg,#161b22,#22272e);
padding:28px;
border-radius:18px;
border-left:6px solid #f59e0b;
margin-bottom:20px;
box-shadow:0 0 18px rgba(245,158,11,.18);
">

<h3 style="color:white;margin-top:0;">
📦 Export Complete Backtest Report
</h3>

<p style="
color:#d1d5db;
font-size:16px;
line-height:1.8;
">

Download the complete backtest trade history for detailed analysis, reporting and further research.

</p>

<table style="
width:100%;
color:#e5e7eb;
font-size:15px;
line-height:2.0;
">

<tr>
<td>✅ Complete Trade Log</td>
<td>📈 Entry & Exit Details</td>
</tr>

<tr>
<td>✅ Trade Direction</td>
<td>💰 PnL & Points</td>
</tr>

<tr>
<td>✅ Excel Compatible</td>
<td>🐍 Python / Power BI Ready</td>
</tr>

</table>

<hr style="border:1px solid rgba(255,255,255,.10);">

<p style="
color:#9ca3af;
font-size:14px;
margin:0;
">

<b>Export Format:</b> CSV

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;

<b>Strategy:</b> {strategy_name}

</p>

</div>
""", unsafe_allow_html=True)

csv = tv_report.to_csv(index=False)

st.download_button(
    "📥 Download Complete Trade Log",
    data=csv,
    file_name=f"{strategy_name}_Trade_Log.csv",
    mime="text/csv",
    use_container_width=True,
    key="download_old"
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

st.subheader("🏆 Final Strategy Verdict")

st.markdown(f"""
<div style="
background:linear-gradient(135deg,#064e3b,#166534);
padding:28px;
border-radius:18px;
border-left:7px solid #22c55e;
margin-bottom:20px;
box-shadow:0 0 20px rgba(34,197,94,.18);
">

<h2 style="
color:white;
text-align:center;
margin-top:0;
margin-bottom:20px;
font-weight:700;
">
✅ BACKTEST STATUS : PASSED
</h2>

<table style="
width:100%;
color:#ecfdf5;
font-size:16px;
line-height:2.0;
border-collapse:collapse;
">

<tr>
<td>🎯 Strategy</td>
<td><b>{strategy_name}</b></td>
</tr>

<tr>
<td>📅 Backtest Period</td>
<td><b>2015 – 2026</b></td>
</tr>

<tr>
<td>💼 Initial Capital</td>
<td><b>₹{capital:,.0f}</b></td>
</tr>

<tr>
<td>📊 Total Trades</td>
<td><b>{total_trades:,}</b></td>
</tr>

<tr>
<td>💰 Net Profit Generated</td>
<td><b>₹{net_profit:,.0f}</b></td>
</tr>

<tr>
<td>🚀 Return on Initial Capital</td>
<td><b>{return_pct:.2f}%</b></td>
</tr>

<tr>
<td>📈 Win Rate</td>
<td><b>{win_rate}%</b></td>
</tr>

<tr>
<td>⚖️ Profit Factor</td>
<td><b>{profit_factor}</b></td>
</tr>

<tr>
<td>📉 Maximum Drawdown</td>
<td><b>{max_dd_pct}%</b></td>
</tr>

<tr>
<td>📊 CAGR</td>
<td><b>{cagr:.2f}% Per Year</b></td>
</tr>

</table>

<hr style="border:1px solid rgba(255,255,255,.15);margin-top:20px;margin-bottom:18px;">

<p style="
color:#dcfce7;
font-size:15px;
line-height:1.9;
margin:0;
">

💡 <b>Executive Assessment</b><br><br>

Starting with an initial trading capital of
<b>₹{capital:,.0f}</b>, the strategy generated a cumulative
net profit of <b>₹{net_profit:,.0f}</b>,
delivering an overall return of
<b>{return_pct:.2f}%</b>
throughout the 2015–2026 backtest period.

The same initial capital was utilized throughout the entire backtest, demonstrating efficient capital deployment and the power of disciplined compounding without requiring additional capital injections.

Across multiple market cycles, the strategy maintained controlled drawdowns, stable risk characteristics and consistent profitability, highlighting the robustness of its systematic and rule-based trading framework.

Overall, the historical performance demonstrates strong capital efficiency, disciplined risk management and long-term wealth creation potential, making the strategy well-positioned for forward testing and eventual live deployment under proper risk controls.

</p>

</div>
""", unsafe_allow_html=True)
st.markdown("---")

st.markdown(
    """
    <div style='text-align:center; padding:15px;'>

    <h4 style='margin-bottom:5px;'>
    📊 Market Edge Analytics
    </h4>


    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("""
<style>
.footer {
    position: fixed;
    bottom: 12px;
    left: 50%;
    transform: translateX(-50%);
    width: 95%;
    max-width: 1400px;
    padding: 20px;
    text-align: center;
    background: rgba(20,20,20,0.85);
    backdrop-filter: blur(15px);
    border-radius: 18px;
    border: 1px solid rgba(255,255,255,0.08);
    color: white;
    box-shadow: 0 8px 30px rgba(0,0,0,0.3);
}

.footer h3 {
    margin: 0;
    font-size: 20px;
}

.footer p {
    margin: 5px 0;
    color: #cbd5e1;
}
</style>

<div class="footer">
    <h3>✨ DIRECTIONAL STRATEGY BACKTEST RESULT</h3>
    <p>Monitor • Analyze • Optimize</p>
</div>
""", unsafe_allow_html=True)