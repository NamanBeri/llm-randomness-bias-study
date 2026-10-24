"""
Analysis & Figure Generation Script for LLM Pseudorandomness Study
Dataset: 900+ trials across Qwen2.5-0.5B, Qwen3.5-4B, Gemma4:e4b at Temperature T=0.8
"""
import glob
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main():
    csv_files = glob.glob("*.csv")
    print(f"Found {len(csv_files)} dataset files:")
    
    data_summary = {}
    for f in sorted(csv_files):
        df = pd.read_csv(f, header=None)
        # format: timestamp, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 (or invalid)
        counts = df.iloc[:, 1:11].to_numpy(dtype=float).sum(axis=0)
        total = counts.sum()
        pct = (counts / total) * 100 if total > 0 else counts
        data_summary[f] = pct
        print(f" - {f}: Total samples = {int(total)}, 7 frequency = {pct[6]:.1f}%")
        
    print("\nGenerating overview plot...")
    plt.figure(figsize=(10, 5), dpi=300)
    plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
    
    # Grand aggregate across all runs
    all_counts = np.zeros(10)
    total_samples = 0
    for f in csv_files:
        df = pd.read_csv(f, header=None)
        counts = df.iloc[:, 1:11].to_numpy(dtype=float).sum(axis=0)
        all_counts += counts
        total_samples += counts.sum()
        
    grand_pct = (all_counts / total_samples) * 100
    x = np.arange(1, 11)
    
    plt.plot(x, grand_pct, marker='o', color='#7c3aed', linewidth=3, markersize=8, label=f'Grand Average (N={int(total_samples)})')
    plt.axhline(10.0, color='#ef4444', linestyle='--', linewidth=1.5, label='Uniform Expectation (10%)')
    
    plt.title('Empirical Distribution of LLM Integer Selection (1 to 10)', fontsize=13, fontweight='bold', pad=15)
    plt.xlabel('Chosen Number (1 to 10)', fontsize=11, fontweight='bold')
    plt.ylabel('Selection Frequency (%)', fontsize=11, fontweight='bold')
    plt.xticks(x)
    plt.ylim(-2, 75)
    plt.legend(loc='upper left')
    plt.tight_layout()
    plt.savefig('distribution_summary.png')
    print("Saved distribution_summary.png")

if __name__ == "__main__":
    main()
