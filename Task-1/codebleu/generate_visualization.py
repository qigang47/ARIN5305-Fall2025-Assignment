#!/usr/bin/env python3
"""
CodeBLEU结果可视化脚本
生成分析结果的图表和图形
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'SimHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

def create_visualization():
    """创建CodeBLEU分析结果的可视化图表"""
    
    # 读取结果数据
    base_path = "/Users/qigang/Downloads/software llm/ARIN5305-Fall2025-Assignment/Task-1/codebleu"
    csv_file = os.path.join(base_path, "codebleu_results.csv")
    
    try:
        df = pd.read_csv(csv_file)
        print("成功读取结果数据")
        print(f"数据形状: {df.shape}")
        print(f"列名: {df.columns.tolist()}")
    except Exception as e:
        print(f"错误：无法读取CSV文件: {e}")
        return
    
    # 创建图表
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    fig.suptitle('CodeBLEU Analysis Results', fontsize=16, fontweight='bold')
    
    # 1. 整体CodeBLEU分数比较
    ax1 = axes[0, 0]
    x_pos = np.arange(len(df))
    width = 0.35
    
    bars1 = ax1.bar(x_pos - width/2, df['correct_vs_llm_codebleu'], width, 
                    label='Correct vs LLM', color='skyblue', alpha=0.8)
    bars2 = ax1.bar(x_pos + width/2, df['correct_vs_faulty_codebleu'], width,
                    label='Correct vs Faulty', color='lightcoral', alpha=0.8)
    
    ax1.set_xlabel('Problems')
    ax1.set_ylabel('CodeBLEU Score')
    ax1.set_title('CodeBLEU Scores Comparison')
    ax1.set_xticks(x_pos)
    ax1.set_xticklabels([name.replace('-', '-\n') for name in df['problem']], rotation=0, ha='center')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # 添加数值标签
    for bar in bars1:
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height + 0.01,
                f'{height:.3f}', ha='center', va='bottom', fontsize=8)
    
    for bar in bars2:
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height + 0.01,
                f'{height:.3f}', ha='center', va='bottom', fontsize=8)
    
    # 2. 各个指标的热力图
    ax2 = axes[0, 1]
    metrics_data = df[['correct_vs_llm_ngram', 'correct_vs_llm_weighted_ngram', 
                      'correct_vs_llm_syntax', 'correct_vs_llm_dataflow']].values
    
    im = ax2.imshow(metrics_data.T, cmap='Blues', aspect='auto')
    ax2.set_title('LLM Code Quality Metrics Heatmap')
    ax2.set_xlabel('Problems')
    ax2.set_ylabel('Metrics')
    ax2.set_xticks(range(len(df)))
    ax2.set_xticklabels([name.replace('-', '-\n') for name in df['problem']], rotation=0, ha='center')
    ax2.set_yticks(range(4))
    ax2.set_yticklabels(['N-gram', 'Weighted N-gram', 'Syntax', 'Dataflow'])
    
    # 添加数值标签到热力图
    for i in range(metrics_data.shape[1]):
        for j in range(metrics_data.shape[0]):
            text = ax2.text(j, i, f'{metrics_data[j, i]:.3f}',
                           ha="center", va="center", color="black", fontsize=8)
    
    # 添加颜色条
    cbar = plt.colorbar(im, ax=ax2)
    cbar.set_label('Score')
    
    # 3. 差异分析
    ax3 = axes[1, 0]
    differences = df['correct_vs_llm_codebleu'] - df['correct_vs_faulty_codebleu']
    colors = ['red' if diff < 0 else 'green' for diff in differences]
    
    bars3 = ax3.bar(df['problem'], differences, color=colors, alpha=0.7)
    ax3.set_xlabel('Problems')
    ax3.set_ylabel('Score Difference')
    ax3.set_title('Performance Gap (LLM vs Faulty Code)')
    ax3.set_xticklabels([name.replace('-', '-\n') for name in df['problem']], rotation=0, ha='center')
    ax3.axhline(y=0, color='black', linestyle='-', alpha=0.5)
    ax3.grid(True, alpha=0.3)
    
    # 添加数值标签
    for bar in bars3:
        height = bar.get_height()
        ax3.text(bar.get_x() + bar.get_width()/2., height + (0.01 if height >= 0 else -0.02),
                f'{height:.3f}', ha='center', va='bottom' if height >= 0 else 'top', fontsize=8)
    
    # 4. 雷达图 - 平均性能
    ax4 = axes[1, 1]
    
    # 计算平均分数
    llm_avg = [
        df['correct_vs_llm_ngram'].mean(),
        df['correct_vs_llm_weighted_ngram'].mean(),
        df['correct_vs_llm_syntax'].mean(),
        df['correct_vs_llm_dataflow'].mean(),
        df['correct_vs_llm_codebleu'].mean()
    ]
    
    faulty_avg = [
        df['correct_vs_faulty_ngram'].mean(),
        df['correct_vs_faulty_weighted_ngram'].mean(),
        df['correct_vs_faulty_syntax'].mean(),
        df['correct_vs_faulty_dataflow'].mean(),
        df['correct_vs_faulty_codebleu'].mean()
    ]
    
    labels = ['N-gram', 'Weighted\nN-gram', 'Syntax', 'Dataflow', 'Overall\nCodeBLEU']
    
    # 创建极坐标图
    ax4.remove()
    ax4 = fig.add_subplot(2, 2, 4, projection='polar')
    
    angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
    angles += angles[:1]  # 闭合图形
    
    llm_avg += llm_avg[:1]
    faulty_avg += faulty_avg[:1]
    
    ax4.plot(angles, llm_avg, 'o-', linewidth=2, label='LLM Code', color='blue')
    ax4.fill(angles, llm_avg, alpha=0.25, color='blue')
    ax4.plot(angles, faulty_avg, 'o-', linewidth=2, label='Faulty Code', color='red')
    ax4.fill(angles, faulty_avg, alpha=0.25, color='red')
    
    ax4.set_xticks(angles[:-1])
    ax4.set_xticklabels(labels)
    ax4.set_ylim(0, 1)
    ax4.set_title('Average Performance Comparison', pad=20)
    ax4.legend(loc='upper right', bbox_to_anchor=(1.3, 1.0))
    ax4.grid(True)
    
    plt.tight_layout()
    
    # 保存图表
    output_file = os.path.join(base_path, "codebleu_analysis.png")
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    print(f"可视化图表已保存到: {output_file}")
    
    # 显示统计信息
    print("\n=== 统计摘要 ===")
    print(f"LLM代码平均CodeBLEU分数: {df['correct_vs_llm_codebleu'].mean():.4f}")
    print(f"错误代码平均CodeBLEU分数: {df['correct_vs_faulty_codebleu'].mean():.4f}")
    print(f"性能差距: {df['correct_vs_llm_codebleu'].mean() - df['correct_vs_faulty_codebleu'].mean():.4f}")
    
    print(f"\nLLM代码最佳表现: {df.loc[df['correct_vs_llm_codebleu'].idxmax(), 'problem']} ({df['correct_vs_llm_codebleu'].max():.4f})")
    print(f"LLM代码最差表现: {df.loc[df['correct_vs_llm_codebleu'].idxmin(), 'problem']} ({df['correct_vs_llm_codebleu'].min():.4f})")
    
    return df

if __name__ == "__main__":
    create_visualization()
