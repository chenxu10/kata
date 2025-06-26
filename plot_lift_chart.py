import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
from sklearn.metrics import mean_tweedie_deviance

def plot_tweedie_lift_chart(y_true, y_pred, n_bins=10, figsize=(10, 6)):
    """
    Plot a lift chart for Tweedie regression model predictions
    
    Parameters:
    y_true (array-like): Actual claim amounts
    y_pred (array-like): Predicted claim amounts
    n_bins (int): Number of bins to create for lift calculation
    figsize (tuple): Figure size for the plot
    
    Returns:
    matplotlib.figure.Figure: Figure object
    matplotlib.axes.Axes: Axes object
    """
    # Create DataFrame with actual and predicted values
    df = pd.DataFrame({
        'actual': y_true,
        'predicted': y_pred
    })
    
    # Sort by predicted values in descending order
    df = df.sort_values('predicted', ascending=False).reset_index(drop=True)
    
    # Create bins based on ordered predictions
    df['bin'] = pd.qcut(df['predicted'], q=n_bins, duplicates='drop')
    
    # Calculate mean actual and predicted values per bin
    bin_stats = df.groupby('bin').agg({
        'actual': 'mean',
        'predicted': 'mean'
    }).reset_index()
    
    # Calculate overall mean for baseline
    overall_mean = df['actual'].mean()
    
    # Create plot
    plt.style.use('seaborn')
    fig, ax = plt.subplots(figsize=figsize)
    
    # Plot actual vs predicted
    sns.lineplot(data=bin_stats, x=bin_stats.index, y='actual', 
                 label='Actual', marker='o', ax=ax)
    sns.lineplot(data=bin_stats, x=bin_stats.index, y='predicted',
                 label='Predicted', marker='o', ax=ax)
    
    # Add baseline reference
    ax.axhline(overall_mean, color='red', linestyle='--', 
               label='Overall Mean')
    
    # Format plot
    ax.set_title(f'Tweedie Model Lift Chart ({n_bins} Bins)')
    ax.set_xlabel('Prediction Bin (Sorted by Predicted Value)')
    ax.set_ylabel('Mean Claim Amount')
    ax.set_xticks(range(len(bin_stats)))
    ax.set_xticklabels([f'Bin {i+1}' for i in range(len(bin_stats))])
    ax.legend()
    ax.grid(True)
    
    return fig, ax
 