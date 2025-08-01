# 贡献指南

感谢您对中文密码字典项目的关注！我们欢迎所有形式的贡献。

## 🤝 如何贡献

### 1. Fork 项目
1. 访问 [项目主页](https://github.com/your-username/redteamnotes-chinese-passwords)
2. 点击右上角的 "Fork" 按钮
3. 这将创建项目的一个副本到您的账户下

### 2. 克隆您的 Fork
```bash
git clone https://github.com/your-username/redteamnotes-chinese-passwords.git
cd redteamnotes-chinese-passwords
```

### 3. 创建特性分支
```bash
git checkout -b feature/your-feature-name
```

### 4. 进行更改
- 添加新的密码字典
- 改进现有字典
- 修复文档错误
- 添加新功能
- 优化代码

### 5. 提交更改
```bash
git add .
git commit -m "Add: 描述您的更改"
```

### 6. 推送更改
```bash
git push origin feature/your-feature-name
```

### 7. 创建 Pull Request
1. 访问您的 Fork 页面
2. 点击 "New Pull Request"
3. 选择您的特性分支
4. 填写详细的描述
5. 提交 PR

## 📋 贡献类型

### 🆕 添加新字典
- 确保密码格式正确（每行一个密码）
- 移除重复项和空行
- 添加适当的文件命名
- 更新文档和统计信息

### 🔧 改进现有字典
- 移除重复密码
- 添加新的常见密码
- 优化文件大小
- 改进密码分类

### 📚 文档改进
- 修复拼写错误
- 添加使用示例
- 改进说明文档
- 翻译文档

### 🐛 Bug 修复
- 修复脚本错误
- 解决兼容性问题
- 优化性能问题

## 📝 提交规范

### 提交信息格式
```
类型: 简短描述

详细描述（可选）

相关问题: #123
```

### 类型说明
- `Add`: 添加新功能或文件
- `Fix`: 修复 bug
- `Update`: 更新现有功能
- `Remove`: 删除功能或文件
- `Docs`: 文档更新
- `Style`: 代码格式调整
- `Refactor`: 代码重构
- `Test`: 测试相关
- `Chore`: 构建过程或辅助工具的变动

### 示例
```
Add: 新增1000个中文密码字典

- 添加常见的中文拼音密码
- 包含数字和字母组合
- 更新统计脚本

相关问题: #45
```

## 🧪 测试指南

### 运行统计脚本
```bash
python3 scripts/stats.py
```

### 验证字典格式
```bash
# 检查重复项
sort redteamnotes-chinese-passwords-1000.txt | uniq -d

# 检查空行
grep -n "^$" redteamnotes-chinese-passwords-1000.txt

# 检查文件大小
ls -lh redteamnotes-chinese-passwords-1000.txt
```

### 测试工具兼容性
```bash
# 测试 Hydra
hydra -l test -P redteamnotes-chinese-passwords-100.txt ssh://localhost

# 测试 John the Ripper
john --wordlist=redteamnotes-chinese-passwords-100.txt test_hash.txt
```

## 📋 检查清单

在提交 PR 之前，请确保：

- [ ] 代码符合项目规范
- [ ] 添加了必要的文档
- [ ] 更新了相关统计信息
- [ ] 测试了所有更改
- [ ] 提交信息清晰明确
- [ ] 没有引入新的 bug

## 🏷️ 标签说明

### Issue 标签
- `bug`: 错误报告
- `enhancement`: 功能请求
- `documentation`: 文档改进
- `good first issue`: 适合新手的任务
- `help wanted`: 需要帮助的任务

### PR 标签
- `ready for review`: 准备审查
- `work in progress`: 工作中
- `needs review`: 需要审查
- `approved`: 已批准

## 📞 获取帮助

如果您在贡献过程中遇到问题：

1. 查看 [Issues](https://github.com/your-username/redteamnotes-chinese-passwords/issues)
2. 搜索现有的讨论
3. 创建新的 Issue 描述问题
4. 联系维护者

## 🙏 致谢

所有贡献者都将被列在项目的贡献者列表中。感谢您为开源社区做出的贡献！

## 📄 行为准则

我们致力于为每个人提供友好、安全和欢迎的环境。请阅读我们的 [行为准则](CODE_OF_CONDUCT.md)。

---

**感谢您的贡献！** 🎉 