import urllib.request, json, sys
sys.stdout.reconfigure(encoding="utf-8")

url = "https://api.github.com/repos/GMOogway/shadowrocket-rules/contents/docs/"
with urllib.request.urlopen(url) as resp:
    for item in json.loads(resp.read().decode()):
        name = item["name"]
        dl = item["download_url"]
        print(f"{name} -> {dl}")