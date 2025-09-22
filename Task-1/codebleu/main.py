#!/usr/bin/env python3
"""
CodeBLEU计算工具
用于计算Java代码之间的相似性分数
"""

import json
import os
import re
from typing import Dict, List, Tuple
import pandas as pd
from codebleu import calc_codebleu

class CodeBLEUCalculator:
    def __init__(self, base_path: str):
        """
        初始化CodeBLEU计算器
        
        Args:
            base_path: 项目根路径
        """
        self.base_path = base_path
        self.correct_path = os.path.join(base_path, "ARIN5305-25F/resource/correctJavaPrograms")
        self.faulty_path = os.path.join(base_path, "ARIN5305-25F/resource/faultyJavaProgramsToCompare")
        self.task1_path = os.path.join(base_path, "ARIN5305-Fall2025-Assignment/Task-1")
        
        # 问题列表
        self.problems = [
            "basic-calculator",
            "count-the-number-of-special-characters-ii",
            "minimum-cost-good-caption",
            "robot-collisions",
            "sum-of-largest-prime-substrings"
        ]
    
    def read_java_file(self, file_path: str) -> str:
        """读取Java文件内容"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return f.read().strip()
        except Exception as e:
            print(f"错误：无法读取文件 {file_path}: {e}")
            return ""
    
    def extract_llm_code_from_chat(self, chat_file: str) -> str:
        """从chat.json文件中提取LLM生成的Java代码"""
        try:
            with open(chat_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # 遍历消息找到assistant的代码回复
            for item in data:
                if 'chat' in item and 'messages' in item['chat']:
                    for msg in item['chat']['messages']:
                        if msg['role'] == 'assistant' and '```java' in msg['content']:
                            # 提取Java代码块
                            content = msg['content']
                            java_matches = re.findall(r'```java\s*(.*?)\s*```', content, re.DOTALL)
                            if java_matches:
                                return java_matches[0].strip()
        except Exception as e:
            print(f"错误：无法解析chat文件 {chat_file}: {e}")
        
        return ""
    
    def calculate_codebleu_score(self, reference: str, hypothesis: str) -> Dict:
        """计算两个代码片段之间的CodeBLEU分数"""
        if not reference or not hypothesis:
            return {"codebleu": 0.0, "ngram_match_score": 0.0, "weighted_ngram_match_score": 0.0, 
                   "syntax_match_score": 0.0, "dataflow_match_score": 0.0}
        
        try:
            result = calc_codebleu([reference], [hypothesis], lang='java')
            return result
        except Exception as e:
            print(f"错误：计算CodeBLEU时出错: {e}")
            return {"codebleu": 0.0, "ngram_match_score": 0.0, "weighted_ngram_match_score": 0.0, 
                   "syntax_match_score": 0.0, "dataflow_match_score": 0.0}
    
    def process_all_problems(self) -> pd.DataFrame:
        """处理所有问题并计算CodeBLEU分数"""
        results = []
        
        for problem in self.problems:
            print(f"\n处理问题: {problem}")
            
            # 读取正确代码
            correct_file = os.path.join(self.correct_path, problem, "Solution.java")
            correct_code = self.read_java_file(correct_file)
            
            # 读取LLM生成的代码
            llm_chat_file = os.path.join(self.task1_path, problem, "chat.json")
            llm_code = self.extract_llm_code_from_chat(llm_chat_file)
            
            # 读取有错误的代码
            faulty_file = os.path.join(self.faulty_path, problem, "Solution.java")
            faulty_code = self.read_java_file(faulty_file)
            
            if correct_code:
                # 计算正确代码 vs LLM代码的相似性
                llm_score = self.calculate_codebleu_score(correct_code, llm_code)
                
                # 计算正确代码 vs 错误代码的相似性
                faulty_score = self.calculate_codebleu_score(correct_code, faulty_code)
                
                results.append({
                    'problem': problem,
                    'correct_vs_llm_codebleu': llm_score['codebleu'],
                    'correct_vs_llm_ngram': llm_score['ngram_match_score'],
                    'correct_vs_llm_weighted_ngram': llm_score['weighted_ngram_match_score'],
                    'correct_vs_llm_syntax': llm_score['syntax_match_score'],
                    'correct_vs_llm_dataflow': llm_score['dataflow_match_score'],
                    'correct_vs_faulty_codebleu': faulty_score['codebleu'],
                    'correct_vs_faulty_ngram': faulty_score['ngram_match_score'],
                    'correct_vs_faulty_weighted_ngram': faulty_score['weighted_ngram_match_score'],
                    'correct_vs_faulty_syntax': faulty_score['syntax_match_score'],
                    'correct_vs_faulty_dataflow': faulty_score['dataflow_match_score'],
                })
                
                print(f"正确代码 vs LLM代码 CodeBLEU: {llm_score['codebleu']:.4f}")
                print(f"正确代码 vs 错误代码 CodeBLEU: {faulty_score['codebleu']:.4f}")
            else:
                print(f"警告：无法读取问题 {problem} 的正确代码")
        
        return pd.DataFrame(results)
    
    def save_results_to_csv(self, df: pd.DataFrame, output_file: str):
        """保存结果到CSV文件"""
        df.to_csv(output_file, index=False, encoding='utf-8')
        print(f"\n结果已保存到: {output_file}")
    
    def print_summary(self, df: pd.DataFrame):
        """打印结果摘要"""
        print("\n=== CodeBLEU分析结果摘要 ===")
        print(f"{'问题':<40} {'正确vs LLM':<12} {'正确vs错误':<12}")
        print("-" * 70)
        
        for _, row in df.iterrows():
            print(f"{row['problem']:<40} {row['correct_vs_llm_codebleu']:<12.4f} {row['correct_vs_faulty_codebleu']:<12.4f}")
        
        print("\n平均分数:")
        print(f"正确代码 vs LLM代码平均CodeBLEU: {df['correct_vs_llm_codebleu'].mean():.4f}")
        print(f"正确代码 vs 错误代码平均CodeBLEU: {df['correct_vs_faulty_codebleu'].mean():.4f}")


def main():
    """主函数"""
    # 设置项目路径
    base_path = "/Users/qigang/Downloads/software llm"
    
    # 创建计算器实例
    calculator = CodeBLEUCalculator(base_path)
    
    print("开始CodeBLEU分析...")
    
    # 处理所有问题
    results_df = calculator.process_all_problems()
    
    if not results_df.empty:
        # 保存结果
        output_file = os.path.join(base_path, "ARIN5305-Fall2025-Assignment/Task-1/codebleu/codebleu_results.csv")
        calculator.save_results_to_csv(results_df, output_file)
        
        # 打印摘要
        calculator.print_summary(results_df)
    else:
        print("错误：没有成功处理任何问题")


if __name__ == "__main__":
    main()
