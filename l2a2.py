import scipy.stats as stats

p = stats.poisson.pmf(6, 10)
print("Probability of raining for exactly 6 days : ", p)

p2 = stats.poisson.pmf(12, 10) + stats.poisson.pmf(13, 10) + stats.poisson.pmf(14, 10)
print("Probabilty of raining for 12-14 days : ", p2)
