#!/usr/bin/env python3
"""
字典文件统计脚本
用于分析密码字典文件的详细信息
"""

import os
import sys
from pathlib import Path

def get_file_stats(file_path):
    """获取文件统计信息"""
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()
        
        # 去除空行和重复行
        unique_lines = set(line.strip() for line in lines if line.strip())
        
        stats = {
            'file_name': os.path.basename(file_path),
            'file_size': os.path.getsize(file_path),
            'total_lines': len(lines),
            'unique_passwords': len(unique_lines),
            'duplicate_lines': len(lines) - len(unique_lines),
            'empty_lines': len([line for line in lines if not line.strip()])
        }
        
        return stats
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None

def format_size(size_bytes):
    """格式化文件大小"""
    if size_bytes == 0:
        return "0B"
    
    size_names = ["B", "KB", "MB", "GB"]
    i = 0
    while size_bytes >= 1024 and i < len(size_names) - 1:
        size_bytes /= 1024.0
        i += 1
    
    return f"{size_bytes:.1f}{size_names[i]}"

def analyze_password_patterns(file_path, sample_size=100):
    """分析密码模式"""
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            lines = [line.strip() for line in f if line.strip()]
        
        if not lines:
            return {}
        
        # 取样本进行分析
        sample = lines[:min(sample_size, len(lines))]
        
        patterns = {
            'numeric_only': 0,
            'alpha_only': 0,
            'alphanumeric': 0,
            'with_special': 0,
            'common_lengths': {},
            'starts_with_digit': 0,
            'ends_with_digit': 0
        }
        
        for password in sample:
            if password.isdigit():
                patterns['numeric_only'] += 1
            elif password.isalpha():
                patterns['alpha_only'] += 1
            elif password.isalnum():
                patterns['alphanumeric'] += 1
            else:
                patterns['with_special'] += 1
            
            length = len(password)
            patterns['common_lengths'][length] = patterns['common_lengths'].get(length, 0) + 1
            
            if password[0].isdigit():
                patterns['starts_with_digit'] += 1
            if password[-1].isdigit():
                patterns['ends_with_digit'] += 1
        
        return patterns
    except Exception as e:
        print(f"Error analyzing patterns in {file_path}: {e}")
        return {}

def main():
    """主函数"""
    # 查找字典文件
    dict_files = []
    for file in os.listdir('.'):
        if file.endswith('.txt') and 'password' in file.lower():
            dict_files.append(file)
    
    if not dict_files:
        print("未找到密码字典文件")
        sys.exit(1)
    
    print("=" * 80)
    print("中文密码字典统计报告")
    print("=" * 80)
    print()
    
    total_stats = {
        'total_files': len(dict_files),
        'total_passwords': 0,
        'total_size': 0
    }
    
    # 统计每个文件
    for file_path in sorted(dict_files):
        stats = get_file_stats(file_path)
        if stats:
            print(f"📁 {stats['file_name']}")
            print(f"   文件大小: {format_size(stats['file_size'])}")
            print(f"   总行数: {stats['total_lines']:,}")
            print(f"   唯一密码: {stats['unique_passwords']:,}")
            print(f"   重复行: {stats['duplicate_lines']:,}")
            print(f"   空行: {stats['empty_lines']:,}")
            
            # 分析密码模式
            patterns = analyze_password_patterns(file_path)
            if patterns:
                print(f"   密码模式分析 (基于前100个样本):")
                print(f"     - 纯数字: {patterns['numeric_only']}%")
                print(f"     - 纯字母: {patterns['alpha_only']}%")
                print(f"     - 字母数字: {patterns['alphanumeric']}%")
                print(f"     - 包含特殊字符: {patterns['with_special']}%")
                print(f"     - 以数字开头: {patterns['starts_with_digit']}%")
                print(f"     - 以数字结尾: {patterns['ends_with_digit']}%")
                
                if patterns['common_lengths']:
                    most_common_length = max(patterns['common_lengths'], key=patterns['common_lengths'].get)
                    print(f"     - 最常见长度: {most_common_length} 字符")
            
            print()
            
            total_stats['total_passwords'] += stats['unique_passwords']
            total_stats['total_size'] += stats['file_size']
    
    # 总体统计
    print("=" * 80)
    print("📊 总体统计")
    print("=" * 80)
    print(f"总文件数: {total_stats['total_files']}")
    print(f"总密码数: {total_stats['total_passwords']:,}")
    print(f"总大小: {format_size(total_stats['total_size'])}")
    print()
    
    # 推荐使用建议
    print("💡 使用建议:")
    print("1. 快速测试: 使用 100-1000 密码的小字典")
    print("2. 标准测试: 使用 10000 密码的中等字典")
    print("3. 全面测试: 使用 100000+ 密码的大字典")
    print("4. 中文系统: 优先使用拼音密码字典")
    print()
    
    print("⚠️  免责声明:")
    print("本工具仅用于合法的安全测试和密码强度评估。")
    print("请确保在获得授权的情况下使用。")

if __name__ == "__main__":
    main() 