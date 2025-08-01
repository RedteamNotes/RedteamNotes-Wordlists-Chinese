#!/bin/bash

# 中文密码字典安装脚本
# 用于设置项目环境和依赖

set -e

echo "🔧 中文密码字典项目安装脚本"
echo "================================"
echo

# 检查操作系统
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    OS="Linux"
elif [[ "$OSTYPE" == "darwin"* ]]; then
    OS="macOS"
elif [[ "$OSTYPE" == "msys" ]] || [[ "$OSTYPE" == "cygwin" ]]; then
    OS="Windows"
else
    OS="Unknown"
fi

echo "📋 系统信息:"
echo "  操作系统: $OS"
echo "  当前目录: $(pwd)"
echo

# 创建必要的目录
echo "📁 创建目录结构..."
mkdir -p examples
mkdir -p scripts
mkdir -p docs
echo "✅ 目录创建完成"
echo

# 检查Python环境
echo "🐍 检查Python环境..."
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version)
    echo "✅ Python3 已安装: $PYTHON_VERSION"
else
    echo "❌ Python3 未安装"
    echo "请先安装Python3: https://www.python.org/downloads/"
    exit 1
fi
echo

# 检查常用工具
echo "🔍 检查常用安全工具..."
TOOLS=("hydra" "john" "hashcat" "aircrack-ng" "medusa" "ncrack")

for tool in "${TOOLS[@]}"; do
    if command -v $tool &> /dev/null; then
        echo "✅ $tool 已安装"
    else
        echo "⚠️  $tool 未安装 (可选)"
    fi
done
echo

# 设置文件权限
echo "🔐 设置文件权限..."
chmod +x scripts/stats.py
chmod +x scripts/install.sh
echo "✅ 权限设置完成"
echo

# 验证字典文件
echo "📊 验证字典文件..."
DICT_FILES=(
    "redteamnotes-chinese-passwords-100.txt"
    "redteamnotes-chinese-passwords-365.txt"
    "redteamnotes-chinese-passwords-500.txt"
    "redteamnotes-chinese-passwords-1000.txt"
    "redteamnotes-chinese-passwords-10000.txt"
    "redteamnotes-chinese-passwords-100000.txt"
    "redteamnotes-chinese-passwords-1000000.txt"
    "redteamnotes-chinese-passwords-5000000.txt"
    "redteamnotes-chinese-passwords-pinyin.txt"
    "redteamnotes-passwords-100.txt"
)

for file in "${DICT_FILES[@]}"; do
    if [[ -f "$file" ]]; then
        size=$(du -h "$file" | cut -f1)
        echo "✅ $file ($size)"
    else
        echo "❌ $file (缺失)"
    fi
done
echo

# 运行统计脚本
echo "📈 生成字典统计报告..."
if [[ -f "scripts/stats.py" ]]; then
    python3 scripts/stats.py
else
    echo "⚠️  统计脚本未找到"
fi
echo

# 创建快速开始指南
echo "📝 创建快速开始指南..."
cat > QUICKSTART.md << 'EOF'
# 快速开始指南

## 1. 克隆项目
```bash
git clone https://github.com/your-username/redteamnotes-chinese-passwords.git
cd redteamnotes-chinese-passwords
```

## 2. 运行安装脚本
```bash
chmod +x scripts/install.sh
./scripts/install.sh
```

## 3. 查看字典统计
```bash
python3 scripts/stats.py
```

## 4. 使用示例
```bash
# 使用Hydra进行SSH测试
hydra -l admin -P redteamnotes-chinese-passwords-100.txt ssh://target.com

# 使用John the Ripper
john --wordlist=redteamnotes-chinese-passwords-1000.txt hashfile.txt
```

## 5. 查看详细文档
- [README.md](README.md) - 项目说明
- [examples/usage_examples.md](examples/usage_examples.md) - 使用示例
- [LICENSE](LICENSE) - 许可证信息

## 注意事项
- 仅在获得授权的系统上使用
- 遵守当地法律法规
- 负责任地使用安全工具
EOF

echo "✅ 快速开始指南已创建"
echo

echo "🎉 安装完成！"
echo "=================="
echo
echo "📚 下一步:"
echo "1. 阅读 README.md 了解项目详情"
echo "2. 查看 examples/usage_examples.md 学习使用方法"
echo "3. 运行 python3 scripts/stats.py 查看字典统计"
echo "4. 在获得授权的情况下进行安全测试"
echo
echo "⚠️  重要提醒:"
echo "- 仅在合法授权的环境中使用"
echo "- 遵守相关法律法规"
echo "- 负责任地使用安全工具"
echo
echo "感谢使用中文密码字典项目！" 