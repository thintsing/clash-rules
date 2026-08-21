import urllib.request, json, sys
sys.stdout.reconfigure(encoding='utf-8')

# 获取仓库结构
url = "https://api.github.com/repos/GMOogway/shadowrocket-rules/contents/"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
with urllib.request.urlopen(req, timeout=15) as resp:
    data = json.loads(resp.read().decode())

for item in data:
    name = item["name"]
    size = item.get("size", 0)
    if item["type"] == "file":
        size_kb = size / 1024
        print(f"  {name} ({size_kb:.1f}KB)")
    elif item["type"] == "dir":
        print(f"  [{name}/]")

# 获取 README
print("\n=== README ===")
url2 = "https://raw.githubusercontent.com/GMOogway/shadowrocket-rules/main/README.md"
req2 = urllib.request.Request(url2, headers={"User-Agent": "Mozilla/5.0"})
try:
    with urllib.request.urlopen(req2, timeout=15) as resp:
        readme = resp.read().decode('utf-8')
        print(readme[:2000])
except Exception as e:
    print(f"无法获取: {e}")