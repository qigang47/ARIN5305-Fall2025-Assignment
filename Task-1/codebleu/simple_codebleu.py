#!/usr/bin/env python3
"""
简化的CodeBLEU计算工具
实现基本的代码相似性度量，包括n-gram BLEU和语法相似性分析
"""

import json
import os
import re
import math
from typing import Dict, List, Tuple
from collections import Counter
import pandas as pd

class SimpleCodeBLEU:
    def __init__(self, base_path: str):
        """
        初始化简化的CodeBLEU计算器
        """
        self.base_path = base_path
        self.correct_path = os.path.join(base_path, "ARIN5305-25F/resource/correctJavaPrograms")
        self.faulty_path = os.path.join(base_path, "ARIN5305-25F/resource/faultyJavaProgramsToCompare")
        self.task1_path = os.path.join(base_path, "ARIN5305-Fall2025-Assignment/Task-1")
        
        self.problems = [
            "basic-calculator",
            "count-the-number-of-special-characters-ii", 
            "minimum-cost-good-caption",
            "robot-collisions",
            "sum-of-largest-prime-substrings"
        ]
    
    def normalize_code(self, code: str) -> str:
        """标准化代码：去除注释、多余空格等"""
        # 去除单行注释
        code = re.sub(r'//.*', '', code)
        # 去除多行注释
        code = re.sub(r'/\*.*?\*/', '', code, flags=re.DOTALL)
        # 标准化空白字符
        code = re.sub(r'\s+', ' ', code)
        # 去除首尾空格
        code = code.strip()
        return code
    
    def extract_tokens(self, code: str) -> List[str]:
        """将代码分解为标记"""
        normalized_code = self.normalize_code(code)
        # 使用正则表达式提取Java标记
        tokens = re.findall(r'\w+|[{}();,\[\]<>=!+\-*/&|^%]', normalized_code)
        return tokens
    
    def extract_keywords(self, code: str) -> List[str]:
        """提取Java关键字和标识符"""
        java_keywords = {
            'public', 'private', 'protected', 'static', 'final', 'class', 'interface',
            'int', 'float', 'double', 'boolean', 'char', 'String', 'void', 'return',
            'if', 'else', 'for', 'while', 'do', 'switch', 'case', 'break', 'continue',
            'try', 'catch', 'finally', 'throw', 'throws', 'new', 'this', 'super',
            'import', 'package', 'extends', 'implements', 'abstract', 'synchronized'
        }
        
        tokens = self.extract_tokens(code)
        keywords = [token for token in tokens if token in java_keywords]
        return keywords
    
    def calculate_ngram_bleu(self, reference: str, hypothesis: str, n: int = 4) -> float:
        """计算n-gram BLEU分数"""
        ref_tokens = self.extract_tokens(reference)
        hyp_tokens = self.extract_tokens(hypothesis)
        
        if len(hyp_tokens) == 0:
            return 0.0
        
        bleu_scores = []
        
        for i in range(1, n + 1):
            ref_ngrams = Counter()
            hyp_ngrams = Counter()
            
            # 生成reference的n-grams
            for j in range(len(ref_tokens) - i + 1):
                ngram = tuple(ref_tokens[j:j+i])
                ref_ngrams[ngram] += 1
            
            # 生成hypothesis的n-grams
            for j in range(len(hyp_tokens) - i + 1):
                ngram = tuple(hyp_tokens[j:j+i])
                hyp_ngrams[ngram] += 1
            
            if len(hyp_ngrams) == 0:
                bleu_scores.append(0.0)
                continue
            
            # 计算精度
            matches = 0
            total = sum(hyp_ngrams.values())
            
            for ngram, count in hyp_ngrams.items():
                matches += min(count, ref_ngrams.get(ngram, 0))
            
            precision = matches / total if total > 0 else 0.0
            bleu_scores.append(precision)
        
        # 计算几何平均
        if all(score > 0 for score in bleu_scores):
            geo_mean = math.exp(sum(math.log(score) for score in bleu_scores) / len(bleu_scores))
        else:
            geo_mean = 0.0
        
        # 计算长度惩罚
        bp = 1.0
        if len(hyp_tokens) < len(ref_tokens):
            bp = math.exp(1 - len(ref_tokens) / len(hyp_tokens))
        
        return bp * geo_mean
    
    def calculate_syntax_similarity(self, reference: str, hypothesis: str) -> float:
        """计算语法结构相似性"""
        # 提取语法结构元素
        ref_structure = self.extract_syntax_elements(reference)
        hyp_structure = self.extract_syntax_elements(hypothesis)
        
        if len(ref_structure) == 0 and len(hyp_structure) == 0:
            return 1.0
        if len(ref_structure) == 0 or len(hyp_structure) == 0:
            return 0.0
        
        # 计算结构元素的交集
        ref_counter = Counter(ref_structure)
        hyp_counter = Counter(hyp_structure)
        
        intersection = sum(min(ref_counter[item], hyp_counter[item]) 
                          for item in ref_counter if item in hyp_counter)
        union = sum(ref_counter.values()) + sum(hyp_counter.values()) - intersection
        
        return intersection / union if union > 0 else 0.0
    
    def extract_syntax_elements(self, code: str) -> List[str]:
        """提取语法结构元素"""
        elements = []
        
        # 方法调用
        method_calls = re.findall(r'(\w+)\s*\(', code)
        elements.extend(['METHOD_CALL_' + call for call in method_calls])
        
        # 控制结构
        control_structures = re.findall(r'\b(if|for|while|switch|try)\b', code)
        elements.extend(['CONTROL_' + struct for struct in control_structures])
        
        # 括号配对
        brackets = re.findall(r'[{}\[\]()]', code)
        elements.extend(['BRACKET_' + bracket for bracket in brackets])
        
        # 操作符
        operators = re.findall(r'[+\-*/=<>!&|^%]', code)
        elements.extend(['OP_' + op for op in operators])
        
        return elements
    
    def calculate_keyword_similarity(self, reference: str, hypothesis: str) -> float:
        """计算关键字相似性"""
        ref_keywords = Counter(self.extract_keywords(reference))
        hyp_keywords = Counter(self.extract_keywords(hypothesis))
        
        if len(ref_keywords) == 0 and len(hyp_keywords) == 0:
            return 1.0
        if len(ref_keywords) == 0 or len(hyp_keywords) == 0:
            return 0.0
        
        intersection = sum(min(ref_keywords[word], hyp_keywords[word]) 
                          for word in ref_keywords if word in hyp_keywords)
        union = sum(ref_keywords.values()) + sum(hyp_keywords.values()) - intersection
        
        return intersection / union if union > 0 else 0.0
    
    def calculate_codebleu_score(self, reference: str, hypothesis: str) -> Dict[str, float]:
        """计算综合的CodeBLEU分数"""
        if not reference or not hypothesis:
            return {
                "codebleu": 0.0,
                "ngram_match_score": 0.0,
                "weighted_ngram_match_score": 0.0,
                "syntax_match_score": 0.0,
                "dataflow_match_score": 0.0
            }
        
        try:
            # 计算各个组件分数
            ngram_score = self.calculate_ngram_bleu(reference, hypothesis, n=4)
            weighted_ngram_score = self.calculate_ngram_bleu(reference, hypothesis, n=2)
            syntax_score = self.calculate_syntax_similarity(reference, hypothesis)
            keyword_score = self.calculate_keyword_similarity(reference, hypothesis)
            
            # 使用关键字相似性作为数据流相似性的近似
            dataflow_score = keyword_score
            
            # 计算加权平均CodeBLEU分数
            alpha, beta, gamma, delta = 0.25, 0.25, 0.25, 0.25
            codebleu = (alpha * ngram_score + 
                       beta * weighted_ngram_score + 
                       gamma * syntax_score + 
                       delta * dataflow_score)
            
            return {
                "codebleu": codebleu,
                "ngram_match_score": ngram_score,
                "weighted_ngram_match_score": weighted_ngram_score,
                "syntax_match_score": syntax_score,
                "dataflow_match_score": dataflow_score
            }
        except Exception as e:
            print(f"错误：计算CodeBLEU时出错: {e}")
            return {
                "codebleu": 0.0,
                "ngram_match_score": 0.0,
                "weighted_ngram_match_score": 0.0,
                "syntax_match_score": 0.0,
                "dataflow_match_score": 0.0
            }
    
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
            
            for item in data:
                if 'chat' in item and 'messages' in item['chat']:
                    for msg in item['chat']['messages']:
                        if msg['role'] == 'assistant' and '```java' in msg['content']:
                            content = msg['content']
                            java_matches = re.findall(r'```java\s*(.*?)\s*```', content, re.DOTALL)
                            if java_matches:
                                return java_matches[0].strip()
        except Exception as e:
            print(f"错误：无法解析chat文件 {chat_file}: {e}")
        
        return ""
    
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
                print(f"  - N-gram: {llm_score['ngram_match_score']:.4f}")
                print(f"  - 语法: {llm_score['syntax_match_score']:.4f}")
                print(f"正确代码 vs 错误代码 CodeBLEU: {faulty_score['codebleu']:.4f}")
                print(f"  - N-gram: {faulty_score['ngram_match_score']:.4f}")
                print(f"  - 语法: {faulty_score['syntax_match_score']:.4f}")
            else:
                print(f"警告：无法读取问题 {problem} 的正确代码")
        
        return pd.DataFrame(results)
    
    def save_results_to_csv(self, df: pd.DataFrame, output_file: str):
        """保存结果到CSV文件"""
        df.to_csv(output_file, index=False, encoding='utf-8')
        print(f"\n结果已保存到: {output_file}")
    
    def print_summary(self, df: pd.DataFrame):
        """打印结果摘要"""
        print("\n" + "="*80)
        print("CodeBLEU分析结果摘要".center(80))
        print("="*80)
        print(f"{'问题':<40} {'正确vs LLM':<12} {'正确vs错误':<12} {'差异':<12}")
        print("-" * 80)
        
        for _, row in df.iterrows():
            diff = row['correct_vs_llm_codebleu'] - row['correct_vs_faulty_codebleu']
            print(f"{row['problem']:<40} {row['correct_vs_llm_codebleu']:<12.4f} {row['correct_vs_faulty_codebleu']:<12.4f} {diff:<12.4f}")
        
        print("-" * 80)
        avg_llm = df['correct_vs_llm_codebleu'].mean()
        avg_faulty = df['correct_vs_faulty_codebleu'].mean()
        print(f"{'平均分数':<40} {avg_llm:<12.4f} {avg_faulty:<12.4f} {avg_llm-avg_faulty:<12.4f}")
        print("="*80)

def main():
    """主函数"""
    base_path = "/Users/qigang/Downloads/software llm"
    
    calculator = SimpleCodeBLEU(base_path)
    
    print("开始简化CodeBLEU分析...")
    
    results_df = calculator.process_all_problems()
    
    if not results_df.empty:
        output_file = os.path.join(base_path, "ARIN5305-Fall2025-Assignment/Task-1/codebleu/codebleu_results.csv")
        calculator.save_results_to_csv(results_df, output_file)
        calculator.print_summary(results_df)
    else:
        print("错误：没有成功处理任何问题")

if __name__ == "__main__":
    main()
