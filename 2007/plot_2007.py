import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
import pandas as pd

# Data
scores = np.array([719, 710, 700, 690, 680, 670, 660, 650, 640, 630, 620, 610, 600, 590, 580])
cum_counts = np.array([1, 2, 15, 84, 225, 510, 942, 1598, 2594, 3947, 5798, 8172, 10941, 14267, 18072])

# Reverse to be ascending
scores = scores[::-1]
cum_counts = cum_counts[::-1]

# Calculate PDF (counts per bin)
# The cum_counts are "number of people >= score"
# So people in [score[i], score[i+1]) = cum_counts[i] - cum_counts[i+1]
pdf_counts = []
for i in range(len(scores)-1):
    pdf_counts.append(cum_counts[i] - cum_counts[i+1])
# For the last bin (>=719), the count is just cum_counts[-1]
pdf_counts.append(cum_counts[-1])

pdf_counts = np.array(pdf_counts)

# For plotting CDF, usually it's P(X <= x), but here we have the right tail. 
# Let's plot the given Cumulative Counts (which is basically a reversed CDF or Survival function)
# and the PDF.

fig, ax1 = plt.subplots(figsize=(10, 6))

# Plot PDF (Bar chart)
# Use the scores as bin edges (roughly). We will plot bars at the scores.
ax1.bar(scores, pdf_counts, width=8, color='skyblue', alpha=0.7, label='区间人数 (PDF)')
ax1.set_xlabel('分数 (Score)', fontsize=12)
ax1.set_ylabel('区间人数 (人数)', color='tab:blue', fontsize=12)
ax1.tick_params(axis='y', labelcolor='tab:blue')

# Plot CDF (Line chart)
ax2 = ax1.twinx()
ax2.plot(scores, cum_counts, color='tab:red', marker='o', linewidth=2, label='累计人数 (>= 该分数)')
ax2.set_ylabel('累计人数 (Cumulative Count)', color='tab:red', fontsize=12)
ax2.tick_params(axis='y', labelcolor='tab:red')

plt.title('分数分布图 (PDF & Cumulative)', fontsize=14)
fig.tight_layout()

# Let's see if it fits a normal distribution tail
# We will just print the result and output the plot
plt.savefig('distribution.png')
plt.show()

# Quick test for normal distribution fit on the tail
# We only have the right tail (scores >= 580). 
# We can estimate mean and std if we assume it's normal.
print("Scores:", scores)
print("PDF counts:", pdf_counts)