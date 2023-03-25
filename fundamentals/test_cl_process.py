import numpy as np
import scipy.stats as sp
import matplotlib.pyplot as plt

def ruin_probability(initial_capital, premium_rate, claims_distribution, claims_threshold):
    time = np.arange(0, 100, 0.1)
    claim_sizes = claims_distribution.rvs(len(time))
    cum_claims = np.cumsum(claim_sizes)
    surplus = initial_capital + premium_rate * time - cum_claims
    ruin_time = np.argmax(surplus < claims_threshold)
    if ruin_time == 0:
        return 0
    else:
        return 1 - sp.norm.cdf((ruin_time - np.mean(time)) / np.std(time))

claims_distribution = sp.expon(loc=0, scale=1000)
claims_threshold = 2000

initial_capitals = np.linspace(0, 2000, 100)
premium_rates = np.linspace(0, 1, 100)

ruin_probabilities = np.zeros((len(initial_capitals), len(premium_rates)))
for i in range(len(initial_capitals)):
    for j in range(len(premium_rates)):
        ruin_probabilities[i, j] = ruin_probability(initial_capitals[i], premium_rates[j], claims_distribution, claims_threshold)

fig, ax = plt.subplots()
im = ax.imshow(ruin_probabilities, origin='lower', extent=[0, 1, 0, 2000], aspect='auto', cmap='viridis')
ax.set_xlabel('Premium rate')
ax.set_ylabel('Initial capital')
cbar = fig.colorbar(im)
cbar.set_label('Ruin probability')
plt.show()