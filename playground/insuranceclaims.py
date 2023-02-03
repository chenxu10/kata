from scipy.stats import poisson

claim_rate = 5

probability = poisson.pmf(k=3, mu=claim_rate)
print(probability)
probability = poisson.cdf(k=3, mu=claim_rate)
print(probability)