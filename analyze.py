# analysis/analyze_data.py
import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv("data/spin_log.csv")

print("----- BASIC STATS -----")
print(df.head(), "\n")

# Compute key metrics
total_bets = df["bet_size"].sum()
total_payouts = df["payout"].sum()
rtp = total_payouts / total_bets if total_bets > 0 else 0
win_rate = (df["payout"] > 0).mean()

print(f"Total Spins: {len(df)}")
print(f"Total Bets: {total_bets:.2f}")
print(f"Total Payouts: {total_payouts:.2f}")
print(f"Return To Player (RTP): {rtp:.2%}")
print(f"Win Rate: {win_rate:.2%}")

# Plot player balance trend
plt.figure(figsize=(10,5))
plt.plot(df["player_balance"], label="Player Balance", linewidth=2)
plt.title("🎰 Player Balance Over Time")
plt.xlabel("Spin Number")
plt.ylabel("Balance")
plt.legend()
plt.grid()
plt.show()

# Plot payout distribution
plt.figure(figsize=(10,5))
df["payout"].plot(kind="hist", bins=20, color="skyblue", edgecolor="black")
plt.title("Distribution of Payouts")
plt.xlabel("Payout")
plt.show()
