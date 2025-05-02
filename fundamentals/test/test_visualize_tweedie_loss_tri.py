import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

def plot_loss_triangle_comparison(actual_triangle, predicted_triangle):
    """
    Plot comparison of actual vs predicted loss development triangles
    
    Parameters:
    actual_triangle (pd.DataFrame): Actual loss triangle with accident period as index
    predicted_triangle (pd.DataFrame): Model predicted loss triangle
    
    Returns:
    matplotlib.figure.Figure: Figure object with comparison plot
    """
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8), sharey=True)
    
    # Plot actual triangle
    sns.heatmap(actual_triangle, annot=True, fmt=".0f", cmap="Blues",
                cbar_kws={'label': 'Loss Amount'}, ax=ax1)
    ax1.set_title("Actual Loss Development")
    ax1.set_xlabel("Development Period")
    ax1.set_ylabel("Accident Period")
    
    # Plot predicted triangle
    sns.heatmap(predicted_triangle, annot=True, fmt=".0f", cmap="Oranges",
                cbar_kws={'label': 'Loss Amount'}, ax=ax2)
    ax2.set_title("Predicted Loss Development")
    ax2.set_xlabel("Development Period")
    
    plt.tight_layout()
    return fig

# Example usage
if __name__ == "__main__":
    # Generate sample data
    periods = 10
    accident_periods = np.arange(2013, 2023)
    dev_periods = [f"Dev {p+1}" for p in range(periods)]
    
    # Create actual triangle with dummy data
    actual = pd.DataFrame(
        np.tril(np.random.lognormal(8, 0.5, (periods, periods)).cumsum(axis=1)),
        index=accident_periods,
        columns=dev_periods
    )
    
    # Create predicted triangle with some noise
    predicted = actual * np.random.uniform(0.95, 1.05, (periods, periods))
    predicted = pd.DataFrame(np.tril(predicted), 
                           index=accident_periods,
                           columns=dev_periods)
    
    # Plot comparison
    fig = plot_loss_triangle_comparison(actual, predicted)
    plt.savefig("triangle_comparison.png")
    plt.show()
