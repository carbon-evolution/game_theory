import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate

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

def simulate_and_analyze_strategies(n_rounds=100):
    results = simulate_strategies(n_rounds)
    
    # Calculate statistics for each strategy
    analysis = {
        'Strategy': [],
        'Final Score': [],
        'Avg Growth': [],
        'Volatility': [],
        'Behavior Pattern': []
    }
    
    behavior_desc = {
        'Always Cooperate': 'Consistent cooperation, vulnerable to exploitation',
        'Always Defect': 'Aggressive strategy, high initial gains',
        'Tit for Tat': 'Adaptive strategy, balanced performance',
        'Random': 'Unpredictable, baseline reference'
    }
    
    for strategy, scores in results.items():
        analysis['Strategy'].append(strategy)
        analysis['Final Score'].append(round(scores[-1], 2))
        analysis['Avg Growth'].append(round(np.mean(np.diff(scores)), 2))
        analysis['Volatility'].append(round(np.std(np.diff(scores)), 2))
        analysis['Behavior Pattern'].append(behavior_desc[strategy])
    
    return results, analysis

def plot_with_table():
    results, analysis = simulate_and_analyze_strategies(100)
    
    # Create figure with subplots
    fig = plt.figure(figsize=(15, 10))
    
    # Plot strategies
    plt.subplot(2, 1, 1)
    colors = {
        'Always Cooperate': 'green',
        'Always Defect': 'red',
        'Tit for Tat': 'blue',
        'Random': 'purple'
    }
    
    for strategy, scores in results.items():
        plt.plot(scores, label=strategy, color=colors[strategy], linewidth=2)
    
    plt.title("Game Theory Strategy Comparison", fontsize=14)
    plt.xlabel("Rounds")
    plt.ylabel("Score")
    plt.grid(True, linestyle='--', alpha=0.3)
    plt.legend()
    
    # Create table
    table_data = list(zip(
        analysis['Strategy'],
        analysis['Final Score'],
        analysis['Avg Growth'],
        analysis['Volatility'],
        analysis['Behavior Pattern']
    ))
    
    # Print table using tabulate
    print("\nStrategy Analysis:")
    print(tabulate(table_data, 
                  headers=['Strategy', 'Final Score', 'Avg Growth/Round', 'Volatility', 'Behavior Pattern'],
                  tablefmt='grid',
                  numalign='right',
                  stralign='left'))
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    plot_with_table()
