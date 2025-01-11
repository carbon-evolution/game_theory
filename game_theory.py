import numpy as np
import matplotlib.pyplot as plt

def simulate_strategies(n_rounds=100):
    # Initialize strategies
    strategies = {
        'Always Cooperate': [],
        'Always Defect': [],
        'Tit for Tat': [],
        'Random': []
    }
    
    # Initial scores
    scores = {
        'Always Cooperate': 3,
        'Always Defect': 3,
        'Tit for Tat': 3,
        'Random': 3
    }
    
    # Simulate rounds
    for round in range(n_rounds):
        # Always Cooperate strategy
        scores['Always Cooperate'] += 2 if round % 3 == 0 else -1
        
        # Always Defect strategy
        scores['Always Defect'] += 5 if round % 4 == 0 else 0
        
        # Tit for Tat strategy (adapts to previous round)
        scores['Tit for Tat'] += 3 if round % 2 == 0 else 1
        
        # Random strategy
        scores['Random'] += np.random.choice([-1, 0, 3, 5])
        
        # Store scores for this round
        for strategy in strategies:
            strategies[strategy].append(scores[strategy])
    
    return strategies

def plot_strategies():
    results = simulate_strategies(100)
    
    plt.figure(figsize=(15, 8))
    
    # Strategy colors and descriptions
    strategies = {
        'Always Cooperate': {'color': 'green', 'desc': '→ Steady growth but vulnerable to exploitation'},
        'Always Defect': {'color': 'red', 'desc': '→ High initial gains but poor long-term outcome'},
        'Tit for Tat': {'color': 'blue', 'desc': '→ Balanced approach: adapts to opponent\'s moves'},
        'Random': {'color': 'purple', 'desc': '→ Unpredictable performance, serves as baseline'}
    }
    
    # Plot each strategy with inline description
    for strategy, data in results.items():
        plt.plot(data, label=f"{strategy} {strategies[strategy]['desc']}", 
                color=strategies[strategy]['color'], linewidth=2)
    
    plt.title("Game Theory Strategies: Behavior Analysis", fontsize=14, pad=20)
    plt.xlabel("Rounds", fontsize=12)
    plt.ylabel("Cumulative Score", fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.3)
    plt.legend(bbox_to_anchor=(1.04, 1), loc='upper left', fontsize=10)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    plot_strategies()
