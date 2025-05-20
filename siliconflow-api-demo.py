import requests
import json
import os
from typing import List, Dict, Any, Optional

class SiliconflowAPI:
    def __init__(self, api_key: str):
        """
        初始化SiliconflowAPI客户端
        
        参数:
            api_key: 硅基流动平台的API密钥
        """
        self.api_key = api_key  # 使用传入的api_key而不是硬编码
        self.base_url = "https://api.siliconflow.cn/v1"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
    
    def ChatCompletion(
        self,
        messages: List[Dict[str, str]],
        model: str = "deepseek-ai/DeepSeek-V3",
        max_tokens: int = 512,
        temperature: float = 0.7,
        top_p: float = 0.7,
        top_k: int = 50,
        stream: bool = False,
        tools: Optional[List[Dict[str, Any]]] = None
    ) -> Dict[str, Any]:
        """
        创建文本对话请求
        
        参数:
            messages: 对话历史消息列表
            model: 模型名称
            max_tokens: 最大生成token数
            temperature: 采样温度
            top_p: 核采样概率阈值
            top_k: 保留的最高概率token数量
            stream: 是否流式输出
            tools: 工具列表
            
        返回:
            API响应结果
        """
        url = f"{self.base_url}/chat/completions"
        
        payload = {
            "model": model,
            "messages": messages,
            "max_tokens": max_tokens,
            "temperature": temperature,
            "top_p": top_p,
            "top_k": top_k,
            "stream": stream
        }
        
        if tools:
            payload["tools"] = tools
            
        try:
            response = requests.post(
                url,
                headers=self.headers,
                data=json.dumps(payload)
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"请求错误: {e}")
            if hasattr(e, 'response') and e.response:
                print(f"错误详情: {e.response.text}")
            return {"error": str(e)}

def 简单示例():
    """运行一个简单的对话示例"""
    # 从环境变量获取API密钥或使用默认值
    api_key = os.environ.get("SILICONFLOW_API_KEY")
    
    
    # 检查API密钥是否存在
    if not api_key:
        print("错误: 未设置SILICONFLOW_API_KEY环境变量")
        print("请设置环境变量或在代码中直接指定API密钥")
        print("示例: export SILICONFLOW_API_KEY='你的API密钥'")
        return
    
    # 创建API客户端
    client = SiliconflowAPI(api_key)
    
    # 准备对话消息
    messages = [
        {
            "role": "user",
            "content": "请用通俗易懂的语言解释一下什么是大语言模型？"
        }
    ]
    
    # 发送请求
    response = client.ChatCompletion(messages)
    
    # 打印响应
    print("\n=== 简单示例响应 ===")
    if "choices" in response and len(response["choices"]) > 0:
        print(response["choices"][0]["message"]["content"])
    else:
        print(f"返回错误: {response}")
    print("====================\n")

def 函数调用示例():
    """运行一个函数调用示例"""
    # 从环境变量获取API密钥或使用默认值
    api_key = os.environ.get("SILICONFLOW_API_KEY")
    
    # 检查API密钥是否存在
    if not api_key:
        print("错误: 未设置SILICONFLOW_API_KEY环境变量")
        return
    
    # 创建API客户端
    client = SiliconflowAPI(api_key)
    
    # 准备对话消息
    messages = [
        {
            "role": "user",
            "content": "北京明天的天气怎么样？"
        }
    ]
    
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
    
    # 发送请求
    response = client.ChatCompletion(messages, tools=tools)
    
    # 打印响应
    print("\n=== 函数调用示例响应 ===")
    if "tool_calls" in response and len(response["tool_calls"]) > 0:
        tool_call = response["tool_calls"][0]
        print(f"函数名: {tool_call['function']['name']}")
        print(f"函数参数: {tool_call['function']['arguments']}")
    else:
        print(f"没有工具调用或返回错误: {response}")
    print("====================\n")

def 流式输出示例():
    """运行一个流式输出示例"""
    # 从环境变量获取API密钥
    api_key = os.environ.get("SILICONFLOW_API_KEY")
    
    # 检查API密钥是否存在
    if not api_key:
        print("\n=== 流式输出示例 ===")
        print("错误: 未设置SILICONFLOW_API_KEY环境变量")
        print("====================\n")
        return
    
    print("\n=== 流式输出示例 ===")
    
    # 准备请求参数
    url = "https://api.siliconflow.cn/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": "deepseek-ai/DeepSeek-V3",
        "messages": [
            {
                "role": "user",
                "content": "请写一首关于春天的诗"
            }
        ],
        "stream": True,
        "max_tokens": 512
    }
    
    try:
        # 流式请求
        with requests.post(url, headers=headers, json=payload, stream=True) as response:
            response.raise_for_status()
            for line in response.iter_lines():
                if line:
                    line_text = line.decode('utf-8')
                    # 过滤掉非数据行
                    if line_text.startswith('data: ') and line_text != 'data: [DONE]':
                        json_str = line_text[6:]  # 去掉 'data: ' 前缀
                        try:
                            chunk = json.loads(json_str)
                            if 'choices' in chunk and len(chunk['choices']) > 0:
                                delta = chunk['choices'][0].get('delta', {})
                                if 'content' in delta and delta['content']:
                                    print(delta['content'], end='', flush=True)
                        except json.JSONDecodeError:
                            print(f"无法解析JSON: {json_str}")
            print()  # 打印换行
    except requests.exceptions.RequestException as e:
        print(f"请求错误: {e}")
        if hasattr(e, 'response') and e.response:
            print(f"错误详情: {e.response.text}")
    
    print("====================\n")

def 主函数():
    """主函数，运行各种示例"""
    print("硅基流动 API 示例程序")
    print("请确保设置了环境变量 SILICONFLOW_API_KEY")
    
    if not os.environ.get("SILICONFLOW_API_KEY"):
        print("\n警告: 未设置SILICONFLOW_API_KEY环境变量")
        print("请使用以下命令设置环境变量:")
        print("Windows (PowerShell): $env:SILICONFLOW_API_KEY='你的API密钥'")
        print("Windows (CMD): set SILICONFLOW_API_KEY=你的API密钥")
        print("Linux/Mac: export SILICONFLOW_API_KEY='你的API密钥'")
        return
    
    # 运行简单示例
    简单示例()
    
    # 运行函数调用示例
    函数调用示例()
    
    # 运行流式输出示例
    流式输出示例()

if __name__ == "__main__":
    主函数() 