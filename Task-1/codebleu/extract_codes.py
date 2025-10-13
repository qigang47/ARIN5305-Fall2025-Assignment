#!/usr/bin/env python3
"""
代码提取工具
用于从chat.json文件中提取LLM生成的代码并保存为单独的Java文件
"""

import json
import os
import re
from main import CodeBLEUCalculator

def extract_and_save_llm_codes():
    """提取并保存所有LLM生成的代码"""
    base_path = "/Users/qigang/Downloads/software llm"
    calculator = CodeBLEUCalculator(base_path)
    
    # 创建输出目录
    output_dir = os.path.join(base_path, "ARIN5305-Fall2025-Assignment/Task-1/codebleu/extracted_llm_codes")
    os.makedirs(output_dir, exist_ok=True)
    
    print("开始提取LLM生成的代码...")
    
    for problem in calculator.problems:
        print(f"\n处理问题: {problem}")
        
        # 读取chat.json文件
        chat_file = os.path.join(calculator.task1_path, problem, "chat.json")
        llm_code = calculator.extract_llm_code_from_chat(chat_file)
        
        if llm_code:
            # 保存到文件
            output_file = os.path.join(output_dir, f"{problem}_llm_solution.java")
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(llm_code)
            print(f"已保存: {output_file}")
            print(f"代码预览（前3行）:")
            lines = llm_code.split('\n')
            for i, line in enumerate(lines[:3]):
                print(f"  {i+1}: {line}")
        else:
            print(f"警告: 无法从 {problem} 中提取代码")
    
    print(f"\n所有代码已提取并保存到: {output_dir}")

if __name__ == "__main__":
    extract_and_save_llm_codes()
