import scipy.stats as st
import numpy as np

def calculate_confidence_interval(a):
    confidence_interval = st.t.interval(
    alpha=0.95,
    df = len(a) - 1,
    loc = np.mean(a),
    scale = st.sem(a))
    return confidence_interval

if __name__ == '__main__':
    a = [1,234,142,24,134]
    print(calculate_confidence_interval(a))
