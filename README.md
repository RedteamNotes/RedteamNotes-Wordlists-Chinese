# 红队笔记中文密码字典

基于泄露和统计的中文密码字典，按命中概率、使用场景与风险效率平衡进行了分层，可以直接使用或作为种子。

## 🎯 使用场景

- **安全测试**: 用于测试系统密码策略的强度
- **渗透测试**: 红队测试中的密码破解
- **密码强度评估**: 评估用户密码的安全性
- **安全研究**: 分析中文密码的常见模式
- **教育目的**: 学习密码安全相关知识

## 📁 文件结构

```
├── redteamnotes-wordlists-chinese-100.txt          # 100个中文密码
├── redteamnotes-wordlists-chinese-365.txt          # 365个中文密码
├── redteamnotes-wordlists-chinese-500.txt          # 500个中文密码
├── redteamnotes-wordlists-chinese-1000.txt         # 1000个中文密码
├── redteamnotes-wordlists-chinese-10000.txt        # 10000个中文密码
├── redteamnotes-wordlists-chinese-100000.txt       # 100000个中文密码
├── redteamnotes-wordlists-chinese-1000000.txt      # 1000000个中文密码
├── redteamnotes-wordlists-chinese-5000000.txt      # 5000000个中文密码
├── redteamnotes-wordlists-chinese-pinyin.txt       # 拼音密码字典
└── redteamnotes-wordlists-100.txt                  # 通用密码字典
```

## 📊 字典统计

| 文件名 | 密码数量 | 文件大小 | 描述 |
|--------|----------|----------|------|
| redteamnotes-wordlists-chinese-100.txt | 100 | 1KB | 精选100个常见中文密码 |
| redteamnotes-wordlists-chinese-365.txt | 365 | 2.8KB | 365个中文密码 |
| redteamnotes-wordlists-chinese-500.txt | 500 | 3.9KB | 500个中文密码 |
| redteamnotes-wordlists-chinese-1000.txt | 1,000 | 10KB | 1000个中文密码 |
| redteamnotes-wordlists-chinese-10000.txt | 10,000 | 81KB | 10000个中文密码 |
| redteamnotes-wordlists-chinese-100000.txt | 100,000 | 818KB | 100000个中文密码 |
| redteamnotes-wordlists-chinese-1000000.txt | 1,000,000 | 8.6MB | 100万中文密码 |
| redteamnotes-wordlists-chinese-5000000.txt | 5,000,000 | 38MB | 500万中文密码 |
| redteamnotes-wordlists-chinese-pinyin.txt | 166,057 | 1.3MB | 拼音密码字典 |
| redteamnotes-wordlists-100.txt | 100 | 789B | 通用密码字典 |

## 🔍 密码类型

### 中文密码特点
- **数字组合**: 123456, 5201314, 147258369 等
- **拼音密码**: woaini, qq123456, aini1314 等
- **键盘走位**: qwerty, zxcvbnm, asdfghjkl 等
- **重复模式**: 111111, 000000, 123123 等

### 通用密码
- **常见弱密码**: password, admin, 123456 等
- **系统默认**: root, guest, admin 等
- **测试密码**: test, testing, changeme 等

## 🚀 使用方法

### 1. 下载字典文件
```bash
git clone https://github.com/RedteamNotes/RedteamNotes-Wordlists-Chinese.git
cd RedteamNotes-Wordlists-Chinese
```

### 2. 使用示例

#### 使用 Hydra 进行密码破解
```bash
# 使用小字典进行快速测试
hydra -l username -P redteamnotes-wordlists-chinese-100.txt target.com ssh

# 使用大字典进行全面测试
hydra -l username -P redteamnotes-wordlists-chinese-10000.txt target.com ssh
```

#### 使用 John the Ripper
```bash
# 使用中文密码字典
john --wordlist=redteamnotes-wordlists-chinese-1000.txt hashfile.txt
```

#### 使用 Hashcat
```bash
# 使用拼音密码字典
hashcat -m 0 -a 0 hash.txt redteamnotes-wordlists-chinese-pinyin.txt
```

## ⚠️ 免责声明

**重要提醒**: 本项目的密码字典仅用于以下合法目的：

- ✅ 安全测试和渗透测试（获得授权的情况下）
- ✅ 密码强度评估
- ✅ 安全研究和教育
- ✅ 系统安全审计

**禁止用于**:
- ❌ 未经授权的系统入侵
- ❌ 恶意攻击他人系统
- ❌ 任何非法活动

使用者需要确保在合法和授权的范围内使用这些工具。作者不对任何滥用行为承担责任。
