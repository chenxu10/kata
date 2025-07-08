import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import TweedieRegressor
from plot_lift_chart import plot_tweedie_lift_chart
import matplotlib.pyplot as plt

# Generate sample insurance claim data
np.random.seed(42)
n_samples = 1000
X = np.random.normal(size=(n_samples, 5))
true_coef = np.array([0.2, -0.1, 0.3, 0.05, -0.15])
exposure = np.random.lognormal(mean=0.5, sigma=0.2, size=n_samples)
mu = np.exp(X @ true_coef + 0.5 * exposure)
y = np.random.poisson(lam=mu * exposure)

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Tweedie regression model
model = TweedieRegressor(power=1.5, alpha=0.1, max_iter=1000)
model.fit(X_train, y_train)

# Get predictions
y_pred = model.predict(X_test)

# Generate and display lift chart
fig, ax = plot_tweedie_lift_chart(y_test, y_pred, n_bins=10)
plt.show() 