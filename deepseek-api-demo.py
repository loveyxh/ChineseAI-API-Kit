#!/usr/bin/env python
# -*- coding: utf-8 -*-

from openai import OpenAI
import os

def 调用DeepseekChat():
    """
    调用DeepSeek-V3模型的示例函数
    """
    # 配置API密钥，推荐使用环境变量
    api_key = os.environ.get("DEEPSEEK_API_KEY", "your_api_key_here")
    
    # 初始化客户端
    client = OpenAI(
        base_url="https://api.deepseek.com/v1",
       # api_key=api_key
         api_key="sk-5a18f1195f3d484d8***********"
    )
    
    # 构建请求消息
    messages = [
        {"role": "system", "content": "你是一个专业、有帮助的AI助手。"},
        {"role": "user", "content": "请简要介绍一下Python的主要特点和应用场景。"}
    ]
    
    # 调用API
    try:
        response = client.chat.completions.create(
            model="deepseek-chat",  # 使用DeepSeek-V3模型
            messages=messages,
            temperature=0.7,  # 控制输出的随机性
            max_tokens=1000   # 控制回复的最大长度
        )
        
        # 提取并返回回复内容
        return response.choices[0].message.content
    except Exception as e:
        return f"调用API时发生错误: {str(e)}"

def 流式响应示例():
    """
    使用流式响应模式调用DeepSeek-V3模型的示例函数
    """
    # 配置API密钥
    api_key = os.environ.get("DEEPSEEK_API_KEY", "your_api_key_here")
    
    # 初始化客户端
    client = OpenAI(
        base_url="https://api.deepseek.com/v1",
        api_key="sk-5a18f1195f3d484d8c13119bcf2247f7"
    )
    
    # 构建请求消息
    messages = [
        {"role": "system", "content": "你是一个专业、有帮助的AI助手。"},
        {"role": "user", "content": "请用简短的段落说明人工智能的发展历程。"}
    ]
    
    # 流式调用API
    try:
        stream = client.chat.completions.create(
            model="deepseek-chat",
            messages=messages,
            temperature=0.7,
            max_tokens=1000,
            stream=True  # 启用流式响应
        )
        
        print("开始接收流式响应...")
        # 实时处理流式响应
        for chunk in stream:
            if chunk.choices[0].delta.content is not None:
                print(chunk.choices[0].delta.content, end="")
        print("\n流式响应结束")
    except Exception as e:
        print(f"流式调用API时发生错误: {str(e)}")

if __name__ == "__main__":
    print("===== 标准API调用示例 =====")
    result = 调用DeepseekChat()
    print(result)
    
    print("\n===== 流式API调用示例 =====")
    流式响应示例()
    
    print("\n注意: 请确保在运行前设置了DEEPSEEK_API_KEY环境变量，或者直接在代码中替换'your_api_key_here'为您的实际API密钥") 