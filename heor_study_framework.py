import pandas as pd
import numpy as np
from typing import List, Dict, Tuple

class OncologyMarkovModel:
    def __init__(self, cycles: int, discount_rate: float = 0.03):
        self.states = ['Stable', 'Progressive', 'Death']
        self.cycles = cycles
        self.discount_rate = discount_rate
        self.transition_matrix = None
        self.costs = None
        self.utilities = None

    def set_transition_matrix(self, matrix: np.array):
        if matrix.shape != (3, 3):
            raise ValueError("Transition matrix must be 3x3")
        self.transition_matrix = matrix

    def set_costs(self, costs: Dict[str, float]):
        self.costs = {state: costs.get(state, 0) for state in self.states}

    def set_utilities(self, utilities: Dict[str, float]):
        self.utilities = {state: utilities.get(state, 0) for state in self.states}

    def run_model(self, initial_state: List[float]) -> Tuple[float, float]:
        if not all([self.transition_matrix is not None, self.costs, self.utilities]):
            raise ValueError("Transition matrix, costs, and utilities must be set before running the model")

        state_distribution = np.array(initial_state)
        total_qaly = 0
        total_cost = 0

        for cycle in range(self.cycles):
            discount_factor = 1 / ((1 + self.discount_rate) ** cycle)
            
            # Calculate QALYs and costs for this cycle
            cycle_qaly = sum(state_distribution * [self.utilities[state] for state in self.states]) * discount_factor
            cycle_cost = sum(state_distribution * [self.costs[state] for state in self.states]) * discount_factor
            
            total_qaly += cycle_qaly
            total_cost += cycle_cost

            # Progress to next cycle
            state_distribution = np.dot(state_distribution, self.transition_matrix)

        return total_qaly, total_cost

class HEORStudy:
    def __init__(self, patient_data: pd.DataFrame):
        self.patient_data = patient_data
        self.markov_model = OncologyMarkovModel(cycles=10)  # 10-year model

    def setup_markov_model(self):
        # Example transition probabilities
        transition_matrix = np.array([
            [0.7, 0.2, 0.1],  # Stable to Stable, Progressive, Death
            [0.0, 0.6, 0.4],  # Progressive to Stable, Progressive, Death
            [0.0, 0.0, 1.0]   # Death is absorbing state
        ])
        self.markov_model.set_transition_matrix(transition_matrix)

        # Example costs per cycle (e.g., in USD)
        costs = {
            'Stable': 5000,
            'Progressive': 10000,
            'Death': 0
        }
        self.markov_model.set_costs(costs)

        # Example utilities
        utilities = {
            'Stable': 0.8,
            'Progressive': 0.5,
            'Death': 0
        }
        self.markov_model.set_utilities(utilities)

    def run_markov_analysis(self, initial_state: List[float]) -> Tuple[float, float]:
        return self.markov_model.run_model(initial_state)

    def calculate_icer(self, intervention_cost: float, comparator_cost: float,
                       intervention_qaly: float, comparator_qaly: float) -> float:
        return (intervention_cost - comparator_cost) / (intervention_qaly - comparator_qaly)

# Example usage
def main():
    # Load your patient data (this is just a placeholder)
    data = pd.DataFrame({
        'patient_id': range(100),
        'age': np.random.uniform(50, 80, 100),
        'stage': np.random.choice(['I', 'II', 'III', 'IV'], 100)
    })

    study = HEORStudy(data)
    study.setup_markov_model()

    # Run the Markov model for the standard of care
    initial_state_soc = [0.9, 0.1, 0]  # 90% start in Stable, 10% in Progressive
    qaly_soc, cost_soc = study.run_markov_analysis(initial_state_soc)
    print(f"Standard of Care - QALYs: {qaly_soc:.2f}, Cost: ${cost_soc:.2f}")

    # Run the Markov model for the new intervention
    # Assume the new intervention improves initial state distribution
    initial_state_new = [0.95, 0.05, 0]  # 95% start in Stable, 5% in Progressive
    qaly_new, cost_new = study.run_markov_analysis(initial_state_new)
    print(f"New Intervention - QALYs: {qaly_new:.2f}, Cost: ${cost_new:.2f}")

    # Calculate ICER
    icer = study.calculate_icer(cost_new, cost_soc, qaly_new, qaly_soc)
    print(f"ICER: ${icer:.2f} per QALY gained")

if __name__ == "__main__":
    main()