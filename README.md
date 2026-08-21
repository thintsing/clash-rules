# proxy-rules

Clash 规则配置，基于 Loyalsoldier 官方规则 + GEOSITE 内置数据库。

## 架构

```
┌─ 规则优先级 ───────────────────────────────────────────────────┐
│ 1. 自定义覆盖 (3 RULE-SET)  → AI/Steam/直连                   │
│ 2. Loyalsoldier 核心 (4 RULE-SET) → proxy/direct/reject/apps  │
│ 3. GEOSITE 补充 (8 条)      → 内置数据库，零网络开销          │
│ 4. GEOIP,CN                 → 国内 IP 直连                    │
│ 5. MATCH                    → 最终兜底                        │
└──────────────────────────────────────────────────────────────┘
```

## 文件说明

| 文件 | 用途 |
|------|------|
| `custom-ai.txt` | AI 服务域名覆盖（Clash 用 `behavior: classical`） |
| `custom-steam.txt` | Steam/Blizzard 游戏覆盖 |
| `custom-direct.txt` | 直连覆盖（Tailscale/msftncsi/VNC/国内游戏） |
| `clash-verge-merge.yaml` | Clash Verge Rev merge 模板 |
| `shadowrocket/shadowrocket_full.conf` | Shadowrocket 完整配置 |

## 依赖

- **Loyalsoldier/clash-rules**（4 个核心文件）
  - `proxy.txt` — 国外代理
  - `direct.txt` — 国内直连
  - `reject.txt` — 广告拦截
  - `applications.txt` — 进程规则
- **mihomo 内置数据库**
  - `geosite.dat` — GEOSITE 分类
  - `geoip.dat` — GEOIP 国家

## Clash Verge Rev 使用

1. 添加 merge 模板：
   ```
   https://raw.githubusercontent.com/thintsing/proxy-rules/main/clash-verge-merge.yaml
   ```
2. 重启 Clash 生效

## Shadowrocket 使用

1. 导入配置：
   ```
   https://raw.githubusercontent.com/thintsing/proxy-rules/main/shadowrocket/shadowrocket_full.conf
   ```
2. 在 `[Proxy]` 段落填入节点

## 更新

规则通过 RULE-SET 远程加载，每日自动更新，无需手动维护。