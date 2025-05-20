# 中文AI大模型API调用示例集

一个集成了多家中国领先AI大模型API调用示例的项目，包括Coze、SiliconFlow、Moonshot Kimi和DeepSeek等平台，旨在帮助开发者快速了解和使用国内AI服务。

## 项目简介

本项目收集整理了多家中国领先AI公司的API调用方式，提供简洁清晰的代码示例，帮助开发者轻松集成各种AI能力，包括：

- **文本生成**：通过DeepSeek、SiliconFlow、Kimi等大模型生成高质量文本内容
- **图像创作**：使用Coze工作流API生成AI图像
- **对话聊天**：实现与各种大模型的多轮对话交互
- **流式输出**：展示实时生成内容的处理方法
- **函数调用**：展示调用模型能力完成特定任务
- **文件分析**：使用Kimi等模型处理和分析文档内容

项目特别注重代码可读性和易用性，每个示例都包含完整的错误处理和详细注释，适合作为AI应用开发的起点或参考。

## 已集成的API服务

### 1. Coze工作流API
- **功能**：AI图像生成
- **文件**：
  - `coze_workflow_api.py` - Flask服务封装
  - `coze_workflow_demo.py` - 简单调用示例

### 2. SiliconFlow API
- **功能**：文本生成、函数调用、流式输出
- **文件**：
  - `siliconflow-api-demo.py` - 完整功能示例

### 3. Moonshot Kimi API
- **功能**：文本生成、流式响应、文件问答
- **文件**：
  - `kimi-api-demo.py` - 多种能力调用示例

### 4. DeepSeek API
- **功能**：文本生成、流式输出
- **文件**：
  - `deepseek-api-demo.py` - 基本调用示例

## 技术栈

### 编程语言与基础库
- Python 3.x
- JSON (数据交换格式)
- 环境变量管理 (os模块)

### 网络请求
- Requests (HTTP请求库)
- OpenAI兼容客户端

### Web服务框架
- Flask (用于API服务封装)

### AI服务提供商
- Coze工作流 (图像生成)
- SiliconFlow (文本生成，函数调用)
- Moonshot Kimi (文本生成，文件问答)
- DeepSeek (文本生成)

### 高级功能
- 流式响应处理
- 函数调用 (Function Calling)
- 文件处理与分析
- 错误处理与重试机制

## 代码示例

### Coze图像生成

```python
def GenerateImage(self, prompt):
    headers = {
        "Authorization": f"Bearer {self.token}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "parameters": {
            "input": prompt
        },
        "workflow_id": self.workflow_id
    }
    
    response = requests.post(self.url, headers=headers, json=payload)
    # 处理响应...
```

### SiliconFlow函数调用

```python
# 定义工具
tools = [
    {
        "type": "function",
        "function": {
            "name": "获取天气",
            "description": "获取指定城市的天气信息",
            "parameters": {
                "type": "object",
                "properties": {
                    "城市": {
                        "type": "string",
                        "description": "城市名称"
                    },
                    "日期": {
                        "type": "string",
                        "description": "查询日期，格式为YYYY-MM-DD"
                    }
                },
                "required": ["城市"]
            }
        }
    }
]

# 发送请求...
```

### Kimi文件问答功能

```python
# 上传文件
file_object = client.files.create(file=file_path, purpose="file-extract")

# 获取文件内容
file_content = client.files.content(file_id=file_object.id).text

# 构建请求消息
messages = [
    {"role": "system", "content": "你是Kimi，由Moonshot AI提供的人工智能助手，你会提供安全，有帮助，准确的回答。"},
    {"role": "system", "content": file_content},  # 将文件内容作为系统消息传入
    {"role": "user", "content": "请简要总结这个文件的主要内容"}
]
```

## 使用说明

### 环境准备

1. **安装依赖**
```bash
pip install -r requirements.txt
```

2. **配置API密钥**

可以通过环境变量设置各平台API密钥:
```bash
# Windows
set DEEPSEEK_API_KEY=your_api_key_here
set MOONSHOT_API_KEY=your_api_key_here

# Linux/Mac
export DEEPSEEK_API_KEY=your_api_key_here
export MOONSHOT_API_KEY=your_api_key_here
```

也可以在代码中直接设置(仅用于测试)。

### 运行示例

#### Coze工作流示例
```bash
# 单次请求示例
python coze_workflow_demo.py

# 启动Web服务
python coze_workflow_api.py
```

API服务调用示例:
```bash
curl -X POST http://localhost:5000/generate \
-H "Content-Type: application/json" \
-d '{"prompt": "一只拟人化的橘猫"}'
```

#### SiliconFlow示例
```bash
python siliconflow-api-demo.py
```

#### Kimi示例
```bash
python kimi-api-demo.py
```

#### DeepSeek示例
```bash
python deepseek-api-demo.py
```

## 注意事项

1. 本项目中的API密钥仅供示例使用，实际应用中请使用自己的API密钥
2. 请遵循各API提供商的使用条款和限制
3. 部分示例可能需要稳定的网络环境
4. 建议在实际项目中更安全地管理API密钥

## 贡献指南

欢迎贡献更多中国AI大模型的API调用示例！请通过Pull Request提交您的代码，并确保:

1. 代码结构清晰，包含适当的注释
2. 实现错误处理和异常捕获
3. 避免在代码中硬编码API密钥
4. 添加使用说明和示例输出

## 许可证

MIT

---

**项目名称**: ChineseAI-API-Kit