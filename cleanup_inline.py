import sys, os
sys.stdout.reconfigure(encoding='utf-8')

repo = "E:\\DEV\\clash-rules"

for sr_name in ["shadowrocket_full.conf", "shadowrocket_rules.conf"]:
    path = os.path.join(repo, "shadowrocket", sr_name)
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # 删除包含 ipify/ipinfo 的行，以及它们前面的注释行和空行
    new_lines = []
    skip_next_empty = False
    for i, line in enumerate(lines):
        stripped = line.strip()
        
        # 跳过内联兜底注释
        if stripped.startswith("# ===== 第1层：内联兜底"):
            skip_next_empty = True
            continue
        
        # 跳过 ipify/ipinfo 行
        if any(x in stripped for x in ['ipify.org', 'api.ipify.org', 'ipinfo.io']):
            skip_next_empty = True
            continue
        
        # 跳过内联兜底后的空行
        if skip_next_empty and stripped == "":
            skip_next_empty = False
            continue
        
        skip_next_empty = False
        new_lines.append(line)
    
    with open(path, 'w', encoding='utf-8', newline='\n') as f:
        f.writelines(new_lines)
    
    # 验证
    remaining = [l for l in new_lines if 'ipify' in l or 'ipinfo' in l]
    print(f"{sr_name}: {'✅ 已删除' if not remaining else '❌ 还有残留'}")
    if remaining:
        for r in remaining:
            print(f"  残留: {r.strip()}")

print("\n现在这些域名在 custom-direct.txt 的 RULE-SET 中，不重复了")