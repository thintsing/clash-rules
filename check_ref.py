import urllib.request, json, sys
sys.stdout.reconfigure(encoding='utf-8')

# 查看 docs/ 目录
url = "https://api.github.com/repos/GMOogway/shadowrocket-rules/contents/docs/"
try:
    with urllib.request.urlopen(url) as resp:
        for item in json.loads(resp.read().decode()):
            print(f"  docs/{item['name']} ({item['size']}B)")
except Exception as e:
    print(f"docs/: {e}")

# 查看 factory/ 目录
url2 = "https://api.github.com/repos/GMOogway/shadowrocket-rules/contents/factory/"
try:
    with urllib.request.urlopen(url2) as resp:
        for item in json.loads(resp.read().decode()):
            print(f"  factory/{item['name']} ({item['size']}B)")
except Exception as e:
    print(f"factory/: {e}")

# 查看 module 文件格式
print("\n=== sr_direct_list.module 前15行 ===")
url3 = "https://raw.githubusercontent.com/GMOogway/shadowrocket-rules/main/sr_direct_list.module"
with urllib.request.urlopen(url3) as resp:
    content = resp.read().decode("utf-8")
    lines = content.split("\n")
    for line in lines[:15]:
        print(f"  {line}")
    print(f"  ... (共 {len(lines)} 行, {len(content)//1024}KB)")

# 查看 sr_proxy_list.module 前10行
print("\n=== sr_proxy_list.module 前10行 ===")
url4 = "https://raw.githubusercontent.com/GMOogway/shadowrocket-rules/main/sr_proxy_list.module"
with urllib.request.urlopen(url4) as resp:
    content = resp.read().decode("utf-8")
    lines = content.split("\n")
    for line in lines[:10]:
        print(f"  {line}")
    print(f"  ... (共 {len(lines)} 行, {len(content)//1024}KB)")