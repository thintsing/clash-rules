#!/usr/bin/env python3
"""修复 ai.txt 和 steam.txt 为 YAML 格式（payload:）"""
import sys, os, re
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

files = [
    ("E:\\DEV\\clash-rules\\ai.txt", "AI 服务规则"),
    ("E:\\DEV\\clash-rules\\steam.txt", "Steam 游戏平台规则"),
]

for filepath, title in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # 提取所有数据行
    data_lines = []
    header_lines = []
    seen = set()
    
    for line in lines:
        stripped = line.strip()
        
        # 跳过空行
        if not stripped:
            continue
        
        # 跳过注释行
        if stripped.startswith('#'):
            continue
        
        # 跳过已存在的 payload: 头
        if stripped == 'payload:':
            continue
        
        # 处理 YAML 格式行:   - 'DOMAIN,xxx' 或   - 'DOMAIN-SUFFIX,xxx'
        yaml_match = re.match(r"-\s*'([^']+)'", stripped)
        if yaml_match:
            content = yaml_match.group(1)
            if content not in seen:
                seen.add(content)
                data_lines.append(content)
            continue
        
        # 处理纯 DOMAIN-SUFFIX 行: DOMAIN-SUFFIX,xxx
        if stripped.startswith('DOMAIN-SUFFIX,'):
            domain = stripped[len('DOMAIN-SUFFIX,'):]
            entry = f"DOMAIN-SUFFIX,{domain}"
            if entry not in seen:
                seen.add(entry)
                data_lines.append(entry)
            continue
        
        # 处理纯 DOMAIN 行: DOMAIN,xxx
        if stripped.startswith('DOMAIN,'):
            domain = stripped[len('DOMAIN,'):]
            entry = f"DOMAIN-SUFFIX,{domain}"  # DOMAIN → DOMAIN-SUFFIX 因为 behavior:domain
            if entry not in seen:
                seen.add(entry)
                data_lines.append(entry)
            continue
        
        # 处理 DOMAIN-KEYWORD 行
        if stripped.startswith('DOMAIN-KEYWORD,'):
            keyword = stripped[len('DOMAIN-KEYWORD,'):]
            entry = f"DOMAIN-KEYWORD,{keyword}"
            if entry not in seen:
                seen.add(entry)
                data_lines.append(entry)
            continue

    # 写入新文件
    with open(filepath, 'w', encoding='utf-8', newline='\n') as f:
        f.write(f"# {title}\n")
        f.write("payload:\n")
        for entry in data_lines:
            f.write(f"  - '{entry}'\n")

    print(f"✅ {os.path.basename(filepath)}: {len(data_lines)} 条规则已转换")

# 验证
for filepath in ["E:\\DEV\\clash-rules\\ai.txt", "E:\\DEV\\clash-rules\\steam.txt"]:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    first_line = content.split('\n')[0]
    has_payload = 'payload:' in content
    data_count = len([l for l in content.split('\n') if l.strip().startswith("- '")])
    print(f"  验证 {os.path.basename(filepath)}: payload={'✅' if has_payload else '❌'}, {data_count} 条数据")

# 清理备份
import glob
for bak in glob.glob("E:\\DEV\\clash-rules\\*.bak"):
    os.remove(bak)
    print(f"  清理备份: {os.path.basename(bak)}")