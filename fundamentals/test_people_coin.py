import random
import matplotlib.pyplot as plt

num_trials = 5000

A_heads = []
B_heads = []

for i in range(num_trials):
    # Flip coins for A
    A_flips = [random.randint(0,1) for j in range(3)]  
    A_heads.append(sum(A_flips))
    
    # Flip coins for B
    B_flips = [random.randint(0,1) for j in range(3)] 
    B_heads.append(sum(B_flips))
    
# Plot histograms    
plt.hist(A_heads, bins=4, alpha=0.5, label='A')
plt.hist(B_heads, bins=4, alpha=0.5, label='B')
plt.legend()
plt.title("Coin Flip Counts")
plt.xlabel("Heads")
plt.ylabel("Count")
plt.show()

# Calculate empircal probability
same_count = sum(i==j for i,j in zip(A_heads, B_heads))  
empirical_prob = same_count / num_trials
print(empirical_prob)