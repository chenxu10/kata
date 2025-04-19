import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

def calculate_risk_neutral_prob(r, dt, u, d):
    """
    Calculate the risk-neutral probability
    
    Parameters:
    r: Risk-free interest rate
    dt: Time step
    u: Up factor
    d: Down factor
    
    Returns:
    p: Risk-neutral probability
    """
    return (np.exp(r * dt) - d) / (u - d)

def initialize_stock_tree(S0, N, u, d):
    """
    Initialize the stock price tree
    
    Parameters:
    S0: Initial stock price
    N: Number of periods
    u: Up factor
    d: Down factor
    
    Returns:
    stock_tree: Tree of stock prices
    """
    stock_tree = np.zeros((N+1, N+1))
    for i in range(N+1):
        for j in range(i+1):
            stock_tree[j, i] = S0 * (u ** (i-j)) * (d ** j)
    return stock_tree

def calculate_expiration_values(stock_tree, K, N, option_type):
    """
    Calculate option values at expiration
    
    Parameters:
    stock_tree: Tree of stock prices
    K: Strike price
    N: Number of periods
    option_type: 'c' for call, 'p' for put
    
    Returns:
    option_tree: Tree of option values at expiration
    """
    option_tree = np.zeros((N+1, N+1))
    for j in range(N+1):
        if option_type.lower() == 'c':  # Call option
            option_tree[j, N] = max(0, stock_tree[j, N] - K)
        else:  # Put option
            option_tree[j, N] = max(0, K - stock_tree[j, N])
    return option_tree

def backward_induction(option_tree, r, dt, p, N):
    """
    Work backwards through the tree
    
    Parameters:
    option_tree: Tree of option values
    r: Risk-free interest rate
    dt: Time step
    p: Risk-neutral probability
    N: Number of periods
    
    Returns:
    option_tree: Updated tree of option values
    """
    for i in range(N-1, -1, -1):
        for j in range(i+1):
            option_tree[j, i] = np.exp(-r * dt) * (p * option_tree[j, i+1] + (1-p) * option_tree[j+1, i+1])
    return option_tree

def binomial_option_price(S0, K, r, N, u, d, option_type='c'):
    """
    Calculate option price using binomial model
    
    Parameters:
    S0: Initial stock price
    K: Strike price
    r: Risk-free interest rate (annual)
    N: Number of periods
    u: Up factor
    d: Down factor
    option_type: 'c' for call, 'p' for put
    
    Returns:
    option_price: Price of the option
    stock_tree: Tree of stock prices
    option_tree: Tree of option values
    """
    # Calculate risk-neutral probability
    dt = 1/N  # Time step (assuming 1 year total time)
    p = calculate_risk_neutral_prob(r, dt, u, d)
    
    # Initialize stock price tree
    stock_tree = initialize_stock_tree(S0, N, u, d)
    
    # Calculate option values at expiration
    option_tree = calculate_expiration_values(stock_tree, K, N, option_type)
    print(option_tree)
    
    # Work backwards through the tree
    option_tree = backward_induction(option_tree, r, dt, p, N)
    
    return option_tree[0, 0], stock_tree, option_tree

def visualize_binomial_tree(stock_tree, option_tree, N):
    """
    Visualize the binomial tree
    """
    # Create a directed graph
    G = nx.DiGraph()
    
    # Add nodes with position information
    pos = {}
    node_labels = {}
    for i in range(N+1):
        for j in range(i+1):
            node_id = f"{j},{i}"
            G.add_node(node_id)
            pos[node_id] = (i, N-j)  # Position nodes in a triangular layout
            node_labels[node_id] = f"S: {stock_tree[j, i]:.2f}\nO: {option_tree[j, i]:.2f}"
            
            # Add edges
            if i < N:
                G.add_edge(node_id, f"{j},{i+1}")  # Up movement
                G.add_edge(node_id, f"{j+1},{i+1}")  # Down movement
    
    plt.figure(figsize=(12, 8))
    nx.draw(G, pos, with_labels=False, node_size=2000, node_color="lightblue", arrows=True)
    nx.draw_networkx_labels(G, pos, labels=node_labels, font_size=8)
    plt.title("Binomial Option Pricing Tree")
    plt.axis('off')
    plt.tight_layout()
    plt.savefig('binomial_tree.png', dpi=300)
    plt.show()
    
# Example usage with the given parameters
if __name__ == "__main__":
    # Parameters
    S0 = 100          # Initial stock price
    K = 100           # Strike price
    r = 0.03          # Annual interest rate
    N = 3             # Number of periods
    u = 1.1           # Up factor
    d = 1/u           # Down factor
    option_type = 'p' # Put option
    
    # Calculate option price
    option_price, stock_tree, option_tree = binomial_option_price(S0, K, r, N, u, d, option_type)
    
    # Display results
    print(f"Initial Stock Price: ${S0}")
    print(f"Strike Price: ${K}")
    print(f"Risk-free Rate: {r*100}%")
    print(f"Number of Periods: {N}")
    print(f"Up Factor: {u}")
    print(f"Down Factor: {d:.4f}")
    print(f"Option Type: {'Put' if option_type=='p' else 'Call'}")
    print(f"Option Price: ${option_price:.4f}")
    
    # Visualize the tree
    visualize_binomial_tree(stock_tree, option_tree, N) 