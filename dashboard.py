# dashboard.py
import streamlit as st
import pandas as pd
import os
import time

st.set_page_config(page_title="🎰 Slot Machine Analytics", layout="wide")

st.title("🎰 Slot Machine Live Analytics Dashboard")

# --- File path ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, "data", "spin_log.csv")

# --- Refresh interval (seconds) ---
REFRESH_INTERVAL = 5

# --- Try to import autorefresh in a version-safe way ---
try:
    # Modern Streamlit (>=1.28)
    from streamlit_autorefresh import st_autorefresh
except Exception:
    # Older versions fallback
    def st_autorefresh(interval=5000, limit=None, key=None):
        """Simple fallback: sleeps and reruns manually."""
        time.sleep(interval / 1000)
        st.experimental_rerun() if hasattr(st, "experimental_rerun") else None

# --- Trigger auto-refresh ---
st_autorefresh(interval=REFRESH_INTERVAL * 1000, limit=None, key="data_refresh")

# --- Main dashboard content ---
if not os.path.exists(file_path):
    st.warning("⚠️ No data yet — play the game to generate spins!")
else:
    try:
        df = pd.read_csv(file_path)

        if df.empty:
            st.warning("No spins logged yet.")
        else:
            # --- Compute Metrics ---
            total_spins = len(df)
            total_bets = df["bet_size"].sum()
            total_payouts = df["payout"].sum()
            rtp = (total_payouts / total_bets) if total_bets > 0 else 0
            win_rate = (df["payout"] > 0).mean()

            # --- Display Stats ---
            st.subheader("📈 Game Metrics")
            col1, col2, col3, col4 = st.columns(4)
            col1.metric("Total Spins", f"{total_spins}")
            col2.metric("Total Bets", f"{total_bets:.2f}")
            col3.metric("RTP (Return to Player)", f"{rtp:.2%}")
            col4.metric("Win Rate", f"{win_rate:.2%}")

            # --- Charts ---
            st.subheader("💰 Player Balance Over Time")
            st.line_chart(df["player_balance"])

            st.subheader("🎯 Payout Distribution")
            st.bar_chart(df["payout"])

            # --- Last Spin Info ---
            st.subheader("🧾 Last Spin Details")
            last_row = df.iloc[-1]
            st.write({
                "Timestamp": last_row["timestamp"],
                "Bet Size": last_row["bet_size"],
                "Payout": last_row["payout"],
                "Machine Balance": last_row["machine_balance"],
                "Player Balance": last_row["player_balance"],
            })

    except Exception as e:
        st.error(f"Error reading data: {e}")

st.info(f"⏳ Dashboard auto-refreshes every {REFRESH_INTERVAL} seconds.")
