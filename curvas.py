import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.style.use('default')
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']
algorithms = ['FireFly 30%', 'ACOR 15%', 'Genetic Diploid', 'PSO Divide']

# Recovery data (Avg Recovery Iter)
recovery_iterations = {
    'FireFly 30%': [6.00, 2.00, 7.00, 3.00, 9.00],
    'ACOR 15%': [4.00, 2.00, 5.00, 4.00, 12.00],
    'Genetic Diploid': [1.00, 1.00, 1.00, 1.00, 3.00],
    'PSO Divide': [3.00, 4.00, 8.00, 4.00, 7.00]
}

# Final fitness values (Avg Best Pre-Change as optimal reference)
final_fitness = {
    'FireFly 30%': [4.326799, 0.000020, 1.949308, 0.009526, -307.245057],
    'ACOR 15%': [4.322080, 0.000003, 0.615696, 0.208088, -372.732798],
    'Genetic Diploid': [0.000000, 0.000000, 0.118543, 0.049361, -365.078117],
    'PSO Divide': [5.943962, 0.000070, 3.451031, 0.676358, -325.050923]
}

# Function to simulate realistic recovery curves
def generate_recovery_curve(initial_fitness, final_fitness, recovery_iters, curve_type='exponential'):
    iterations = int(recovery_iters) + 1
    x = np.arange(iterations)
    
    if curve_type == 'exponential':
        progress = 1 - np.exp(-x / (recovery_iters * 0.6))
    elif curve_type == 'linear':
        progress = x / recovery_iters
    else:
        progress = 1 / (1 + np.exp(-(x - recovery_iters/2) / (recovery_iters/4)))
    
    progress[-1] = 1.0
    progress = np.clip(progress, 0, 1)
    
    fitness_values = initial_fitness + progress * (final_fitness - initial_fitness)
    return x, fitness_values

# Simulated initial values after the change (worse than the final ones)
initial_fitness_simulation = {
    'Benchmark 1': [8.0, 7.5, 0.5, 9.0],
    'Benchmark 2': [0.1, 0.08, 0.05, 0.15],
    'Benchmark 3': [15.0, 12.0, 1.0, 18.0],
    'Benchmark 4': [2.5, 3.0, 0.3, 4.0],
    'Benchmark 5': [-150.0, -180.0, -200.0, -120.0]
}

# PLOT 1: Recovery curves for Benchmark 1
fig1, ax1 = plt.subplots(figsize=(12, 8))
benchmark_idx = 0
for i, algorithm in enumerate(algorithms):
    recovery_iter = recovery_iterations[algorithm][benchmark_idx]
    initial_fitness = initial_fitness_simulation['Benchmark 1'][i]
    final_fit = final_fitness[algorithm][benchmark_idx]
    x, y = generate_recovery_curve(initial_fitness, final_fit, recovery_iter, 'exponential')
    
    ax1.plot(x, y, marker='o', markersize=4, linewidth=2, 
             label=f'{algorithm} ({recovery_iter} iter)', color=colors[i])
    ax1.axvline(x=recovery_iter, color=colors[i], linestyle='--', alpha=0.3)

ax1.set_xlabel('Iterations after the change')
ax1.set_ylabel('Fitness')
ax1.set_title('Recovery Curves - Benchmark 1\n(Fitness vs Iteration after change)')
ax1.legend()
ax1.grid(True, alpha=0.3)
ax1.set_ylim(3, 10)
plt.tight_layout()
plt.show()

# PLOT 2: Recovery curves for Benchmark 2
fig2, ax2 = plt.subplots(figsize=(12, 8))
benchmark_idx = 1
for i, algorithm in enumerate(algorithms):
    recovery_iter = recovery_iterations[algorithm][benchmark_idx]
    initial_fitness = initial_fitness_simulation['Benchmark 2'][i]
    final_fit = final_fitness[algorithm][benchmark_idx]
    x, y = generate_recovery_curve(initial_fitness, final_fit, recovery_iter, 'exponential')
    
    ax2.plot(x, y, marker='s', markersize=4, linewidth=2, 
             label=f'{algorithm} ({recovery_iter} iter)', color=colors[i])
    ax2.axvline(x=recovery_iter, color=colors[i], linestyle='--', alpha=0.3)

ax2.set_xlabel('Iterations after the change')
ax2.set_ylabel('Fitness (log scale)')
ax2.set_title('Recovery Curves - Benchmark 2\n(Fitness vs Iteration after change)')
ax2.legend()
ax2.grid(True, alpha=0.3)
ax2.set_yscale('log')
plt.tight_layout()
plt.show()

# PLOT 3: Recovery curves for Benchmarks 3 and 4
fig3, (ax3, ax4) = plt.subplots(1, 2, figsize=(16, 6))

# Benchmark 3
benchmark_idx = 2
for i, algorithm in enumerate(algorithms):
    recovery_iter = recovery_iterations[algorithm][benchmark_idx]
    initial_fitness = initial_fitness_simulation['Benchmark 3'][i]
    final_fit = final_fitness[algorithm][benchmark_idx]
    x, y = generate_recovery_curve(initial_fitness, final_fit, recovery_iter, 'exponential')
    
    ax3.plot(x, y, marker='^', markersize=4, linewidth=2, 
             label=f'{algorithm} ({recovery_iter} iter)', color=colors[i])
    ax3.axvline(x=recovery_iter, color=colors[i], linestyle='--', alpha=0.3)

ax3.set_xlabel('Iterations after the change')
ax3.set_ylabel('Fitness')
ax3.set_title('Benchmark 3 - Recovery Curves')
ax3.legend()
ax3.grid(True, alpha=0.3)

# Benchmark 4
benchmark_idx = 3
for i, algorithm in enumerate(algorithms):
    recovery_iter = recovery_iterations[algorithm][benchmark_idx]
    initial_fitness = initial_fitness_simulation['Benchmark 4'][i]
    final_fit = final_fitness[algorithm][benchmark_idx]
    x, y = generate_recovery_curve(initial_fitness, final_fit, recovery_iter, 'exponential')
    
    ax4.plot(x, y, marker='d', markersize=4, linewidth=2, 
             label=f'{algorithm} ({recovery_iter} iter)', color=colors[i])
    ax4.axvline(x=recovery_iter, color=colors[i], linestyle='--', alpha=0.3)

ax4.set_xlabel('Iterations after the change')
ax4.set_ylabel('Fitness')
ax4.set_title('Benchmark 4 - Recovery Curves')
ax4.legend()
ax4.grid(True, alpha=0.3)

fig3.suptitle('Recovery Curves - Benchmarks 3 and 4', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()

# PLOT 4: Recovery curves for Benchmark 5
fig4, ax5 = plt.subplots(figsize=(12, 8))
benchmark_idx = 4
for i, algorithm in enumerate(algorithms):
    recovery_iter = recovery_iterations[algorithm][benchmark_idx]
    initial_fitness = initial_fitness_simulation['Benchmark 5'][i]
    final_fit = final_fitness[algorithm][benchmark_idx]
    x, y = generate_recovery_curve(initial_fitness, final_fit, recovery_iter, 'exponential')
    
    ax5.plot(x, y, marker='*', markersize=6, linewidth=2, 
             label=f'{algorithm} ({recovery_iter} iter)', color=colors[i])
    ax5.axvline(x=recovery_iter, color=colors[i], linestyle='--', alpha=0.3)

ax5.set_xlabel('Iterations after the change')
ax5.set_ylabel('Fitness (negative values)')
ax5.set_title('Recovery Curves - Benchmark 5\n(Fitness vs Iteration after change)')
ax5.legend()
ax5.grid(True, alpha=0.3)
ax5.invert_yaxis()
plt.tight_layout()
plt.show()

# PLOT 5: Comparison of recovery speed across algorithms
fig5, ax6 = plt.subplots(figsize=(12, 8))

# Create a heatmap for recovery speed
recovery_data = np.array([recovery_iterations[alg] for alg in algorithms])
benchmarks = ['Bench 1', 'Bench 2', 'Bench 3', 'Bench 4', 'Bench 5']

im = ax6.imshow(recovery_data, cmap='RdYlGn_r', aspect='auto')

# Show values in each cell
for i in range(len(algorithms)):
    for j in range(len(benchmarks)):
        text = ax6.text(j, i, f'{recovery_data[i, j]:.1f}',
                       ha="center", va="center", color="black", fontweight='bold')

ax6.set_xticks(np.arange(len(benchmarks)))
ax6.set_yticks(np.arange(len(algorithms)))
ax6.set_xticklabels(benchmarks)
ax6.set_yticklabels(algorithms)
ax6.set_xlabel('Benchmarks')
ax6.set_ylabel('Algorithms')
ax6.set_title('Heatmap - Recovery Iterations\n(Fewer iterations = Better)')

# Add color bar
cbar = plt.colorbar(im, ax=ax6)
cbar.set_label('Recovery Iterations', rotation=270, labelpad=15)

plt.tight_layout()
plt.show()

print("Recovery Curve Analysis:")
print("========================")
for i, algorithm in enumerate(algorithms):
    avg_recovery = np.mean(recovery_iterations[algorithm])
    print(f"{algorithm}:")
    print(f"  - Average recovery iterations: {avg_recovery:.2f}")
    print(f"  - Iteration range: {min(recovery_iterations[algorithm])} - {max(recovery_iterations[algorithm])}")
    print()