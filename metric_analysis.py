import matplotlib.pyplot as plt
import numpy as np

benchmarks = ['Benchmark 1', 'Benchmark 2', 'Benchmark 3', 'Benchmark 4', 'Benchmark 5']

# Best Pre-Change Values
best_values = {
    'FireFly 30%': [4.326799, 0.000020, 1.949308, 0.009526, -307.245057],
    'ACOR 15%': [4.322080, 0.000003, 0.615696, 0.208088, -372.732798],
    'Genetic Diploid': [0.000000, 0.000000, 0.118543, 0.049361, -365.078117],
    'PSO Divide': [5.943962, 0.000070, 3.451031, 0.676358, -325.050923]
}

# Average Recovery Iterations
recovery_iterations = {
    'FireFly 30%': [6.00, 2.00, 7.00, 3.00, 9.00],
    'ACOR 15%': [4.00, 2.00, 5.00, 4.00, 12.00],
    'Genetic Diploid': [1.00, 1.00, 1.00, 1.00, 3.00],
    'PSO Divide': [3.00, 4.00, 8.00, 4.00, 7.00]
}

plt.style.use('default')
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

# GRAPH 1: Benchmark 2 (Very Small Values)
fig1, ax1 = plt.subplots(figsize=(10, 6))

algorithms = list(best_values.keys())
benchmark2_values = [best_values[alg][1] for alg in algorithms]

bars = ax1.bar(algorithms, benchmark2_values, color=colors, alpha=0.8)

for i, (bar, value) in enumerate(zip(bars, benchmark2_values)):
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2., height + max(benchmark2_values)*0.01,
             f'{value:.2e}', ha='center', va='bottom', fontsize=11, fontweight='bold')

ax1.set_ylabel('Best Value')
ax1.set_title('Comparison of Best Values - Benchmark 2 (Very Small Values)')
ax1.grid(axis='y', alpha=0.3)
ax1.set_ylim(0, max(benchmark2_values) * 1.2)

plt.tight_layout()
plt.show()

# GRAPH 2: Benchmarks 3 and 4 (Small Values)
fig2, (ax2, ax3) = plt.subplots(1, 2, figsize=(14, 6))

# Benchmark 3
benchmark3_values = [best_values[alg][2] for alg in algorithms]
bars3 = ax2.bar(algorithms, benchmark3_values, color=colors, alpha=0.8)

for i, (bar, value) in enumerate(zip(bars3, benchmark3_values)):
    height = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2., height + max(benchmark3_values)*0.02,
             f'{value:.3f}', ha='center', va='bottom', fontsize=11, fontweight='bold')

ax2.set_ylabel('Best Value')
ax2.set_title('Benchmark 3')
ax2.grid(axis='y', alpha=0.3)
ax2.set_ylim(0, max(benchmark3_values) * 1.2)

# Benchmark 4
benchmark4_values = [best_values[alg][3] for alg in algorithms]
bars4 = ax3.bar(algorithms, benchmark4_values, color=colors, alpha=0.8)

for i, (bar, value) in enumerate(zip(bars4, benchmark4_values)):
    height = bar.get_height()
    ax3.text(bar.get_x() + bar.get_width()/2., height + max(benchmark4_values)*0.02,
             f'{value:.3f}', ha='center', va='bottom', fontsize=11, fontweight='bold')

ax3.set_ylabel('Best Value')
ax3.set_title('Benchmark 4')
ax3.grid(axis='y', alpha=0.3)
ax3.set_ylim(0, max(benchmark4_values) * 1.2)

fig2.suptitle('Comparison of Best Values - Benchmarks 3 and 4', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()

# GRAPH 3: Benchmark 1 (Moderate Positive Values)
fig3, ax4 = plt.subplots(figsize=(10, 6))

benchmark1_values = [best_values[alg][0] for alg in algorithms]
bars1 = ax4.bar(algorithms, benchmark1_values, color=colors, alpha=0.8)

for i, (bar, value) in enumerate(zip(bars1, benchmark1_values)):
    height = bar.get_height()
    ax4.text(bar.get_x() + bar.get_width()/2., height + max(benchmark1_values)*0.02,
             f'{value:.3f}', ha='center', va='bottom', fontsize=11, fontweight='bold')

ax4.set_ylabel('Best Value')
ax4.set_title('Comparison of Best Values - Benchmark 1')
ax4.grid(axis='y', alpha=0.3)
ax4.set_ylim(0, max(benchmark1_values) * 1.2)

plt.tight_layout()
plt.show()

# GRAPH 4: Benchmark 5 (Large Negative Values)
fig4, ax5 = plt.subplots(figsize=(10, 6))

benchmark5_values = [best_values[alg][4] for alg in algorithms]
bars5 = ax5.bar(algorithms, benchmark5_values, color=colors, alpha=0.8)

for i, (bar, value) in enumerate(zip(bars5, benchmark5_values)):
    height = bar.get_height()
    ax5.text(bar.get_x() + bar.get_width()/2., height - abs(min(benchmark5_values))*0.05,
             f'{value:.1f}', ha='center', va='top', fontsize=11, fontweight='bold')

ax5.set_ylabel('Best Value')
ax5.set_title('Comparison of Best Values - Benchmark 5 (Large Negative Values)')
ax5.grid(axis='y', alpha=0.3)
ax5.set_ylim(min(benchmark5_values) * 1.1, 0)

plt.tight_layout()
plt.show()

# GRAPH 5: Average Recovery Iterations (All Benchmarks)
fig5, ax6 = plt.subplots(figsize=(12, 8))

x = np.arange(len(benchmarks))
width = 0.2
multiplier = 0

for i, (algorithm, values) in enumerate(recovery_iterations.items()):
    offset = width * multiplier
    rects = ax6.bar(x + offset, values, width, label=algorithm, color=colors[i], alpha=0.8)
    
    for j, value in enumerate(values):
        ax6.text(x[j] + offset, value + 0.1, f'{value:.1f}', 
                ha='center', va='bottom', fontsize=9, fontweight='bold')
    
    multiplier += 1

ax6.set_ylabel('Recovery Iterations')
ax6.set_title('Comparison of Recovery Iterations (Avg Recovery Iter) - All Benchmarks')
ax6.set_xticks(x + width * 1.5)
ax6.set_xticklabels(benchmarks)
ax6.legend(loc='upper right')
ax6.grid(axis='y', alpha=0.3)
ax6.set_ylim(0, max([max(vals) for vals in recovery_iterations.values()]) * 1.2)

plt.tight_layout()
plt.show()