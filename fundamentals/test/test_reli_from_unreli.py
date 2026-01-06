"""
Try to simulate the key ideas from Von Neuman

Probabilistic logics and the synthesis of reliable
organisms from unreliable componentsProbabilistic logics and the synthesis of reliable
organisms from unreliable components
"""

import random
from collections import Counter

class UnreliableComponent:
    """An unreliable component that can fail with probability p"""
    def __init__(self, failure_prob=0.3):
        self.failure_prob = failure_prob
    
    def execute(self, task):
        """Execute a task, but may fail with given probability"""
        if random.random() < self.failure_prob:
            # Component failed - returns corrupted output
            corruption = random.choice([
                "Hullo, World!",
                "Hello, Wrold!",
                "Hellp, World!",
                "Hello, Word!",
                "Helo, World!"
            ])
            return corruption
        # Component succeeded
        return "Hello, World!"

class RedundantSystem:
    """A system using redundancy and majority voting"""
    def __init__(self, num_components=5, failure_prob=0.3):
        # Create redundant components
        self.components = [UnreliableComponent(failure_prob) 
                          for _ in range(num_components)]
        
    def execute_with_redundancy(self, task):
        """Execute task using all components and majority vote"""
        # All components execute the task
        outputs = [comp.execute(task) for comp in self.components]
        
        # Majority voting
        vote_counts = Counter(outputs)
        most_common = vote_counts.most_common(1)[0]
        
        return {
            "outputs": outputs,
            "final_output": most_common[0],
            "votes": most_common[1],
            "total_components": len(outputs)
        }

class TreeNode:
    """Node in the tree: either a leaf (unreliable component) or a majority voter node."""
    def __init__(self, is_leaf, failure_prob=0.3, children=None):
        self.is_leaf = is_leaf
        if is_leaf:
            self.component = UnreliableComponent(failure_prob)
        else:
            self.children = children
    
    def execute(self, task):
        if self.is_leaf:
            return self.component.execute(task)
        else:
            # This is a majority voter node
            outputs = [child.execute(task) for child in self.children]
            # Perfect majority vote
            vote_counts = Counter(outputs)
            most_common = vote_counts.most_common(1)[0]
            return most_common[0]

class HierarchicalSystem:
    """A hierarchical system as a tree of perfect majority voters and unreliable leaves."""
    def __init__(self, branching_factor=3, depth=2, failure_prob=0.3):
        self.branching_factor = branching_factor
        self.depth = depth
        self.failure_prob = failure_prob
        self.root = self.build_tree(branching_factor, depth, failure_prob)
    
    def build_tree(self, branching_factor, depth, failure_prob):
        if depth == 0:
            # Leaf node
            return TreeNode(is_leaf=True, failure_prob=failure_prob)
        else:
            # Internal node: create children and then this node will do majority vote
            children = [self.build_tree(branching_factor, depth-1, failure_prob) 
                       for _ in range(branching_factor)]
            return TreeNode(is_leaf=False, children=children)
    
    def execute(self, task):
        return self.root.execute(task)

def demonstrate_reliability():
    """Demonstrate how redundancy improves reliability"""
    print("=== Building Reliable System from Unreliable Components ===\n")
    
    # Test single unreliable component
    print("1. Single Unreliable Component (failure prob=0.3):")
    single_comp = UnreliableComponent(0.3)
    results = [single_comp.execute("print") for _ in range(10)]
    success_rate = results.count("Hello, World!") / len(results)
    print(f"   Success rate: {success_rate:.1%}")
    print(f"   Sample outputs: {results[:3]}...\n")
    
    # Test redundant system
    print("2. Redundant System with 5 Components:")
    redundant_sys = RedundantSystem(num_components=5, failure_prob=0.3)
    result = redundant_sys.execute_with_redundancy("print")
    print(f"   Individual outputs: {result['outputs']}")
    print(f"   Majority decision: '{result['final_output']}'")
    print(f"   Confidence: {result['votes']}/{result['total_components']} votes\n")
    
    # Test hierarchical system (tree with 9 components: 3x3)
    print("3. Hierarchical System (Tree with branching factor=3, depth=2 -> 9 leaves):")
    hierarchical_sys = HierarchicalSystem(branching_factor=3, depth=2, failure_prob=0.3)
    final_output = hierarchical_sys.execute("print")
    print(f"   Final output: '{final_output}'")
    
    # Statistical demonstration
    print("\n" + "="*60)
    print("Statistical Reliability Demonstration:")
    print("="*60)
    
    num_trials = 1000
    success_counts = {"single": 0, "redundant": 0, "hierarchical": 0}
    
    for _ in range(num_trials):
        # Single component
        single_comp = UnreliableComponent(0.3)
        if single_comp.execute("print") == "Hello, World!":
            success_counts["single"] += 1
        
        # Redundant system with 5 components
        redundant_sys = RedundantSystem(5, 0.3)
        if redundant_sys.execute_with_redundancy("print")["final_output"] == "Hello, World!":
            success_counts["redundant"] += 1
        
        # Hierarchical system with 9 components (tree of 3x3)
        hierarchical_sys = HierarchicalSystem(3, 2, 0.3)
        if hierarchical_sys.execute("print") == "Hello, World!":
            success_counts["hierarchical"] += 1
    
    print(f"\nSuccess rates over {num_trials} trials:")
    for system, count in success_counts.items():
        rate = count / num_trials
        reliability_gain = rate / (success_counts["single"] / num_trials)
        print(f"  {system.capitalize():12s}: {rate:.1%} "
              f"(reliability gain: {reliability_gain:.1f}x)")

if __name__ == "__main__":
    demonstrate_reliability()