#!/usr/bin/env python
# -*- coding: utf-8 -*-

from openai import OpenAI
import os

def 调用KimiChat():
    """
    调用Kimi大模型的示例函数
    """
    # 配置API密钥，推荐使用环境变量
    api_key = os.environ.get("MOONSHOT_API_KEY", "your_api_key_here")
    
    # 初始化客户端
    client = OpenAI(
        base_url="https://api.moonshot.cn/v1",
        api_key="sk-grrgJA0iASpFrF6G6kAHswAqkm***********"
    )
    
    # 构建请求消息
    messages = [
        {"role": "system", "content": "你是Kimi，由Moonshot AI提供的人工智能助手，你更擅长中文和英文的对话。你会为用户提供安全，有帮助，准确的回答。"},
        {"role": "user", "content": "请介绍一下中国的四大发明及其历史意义。"}
    ]
    
    # 调用API
    try:
        response = client.chat.completions.create(
            model="moonshot-v1-32k",  # 使用Kimi提供的模型
            messages=messages,
            temperature=0.3,  # Kimi推荐的温度值
            max_tokens=2000   # 控制回复的最大长度
        )
        
        # 提取并返回回复内容
        return response.choices[0].message.content
    except Exception as e:
        return f"调用API时发生错误: {str(e)}"

def 流式响应示例():
    """
    使用流式响应模式调用Kimi大模型的示例函数
    """
    # 配置API密钥
    api_key = os.environ.get("MOONSHOT_API_KEY", "your_api_key_here")
    
    # 初始化客户端
    client = OpenAI(
        base_url="https://api.moonshot.cn/v1",
        api_key=api_key
    )
    
    # 构建请求消息
    messages = [
        {"role": "system", "content": "你是Kimi，由Moonshot AI提供的人工智能助手，你更擅长中文和英文的对话。你会为用户提供安全，有帮助，准确的回答。"},
        {"role": "user", "content": "请用简短的段落介绍一下人工智能在医疗领域的应用。"}
    ]
    
    # 流式调用API
    try:
        stream = client.chat.completions.create(
            model="moonshot-v1-32k",
            messages=messages,
            temperature=0.3,
            max_tokens=2000,
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

def 文件问答示例():
    """
    使用Kimi API进行文件问答的示例
    注意：需要准备一个名为example.pdf的文件在当前目录
    """
    from pathlib import Path
    
    # 配置API密钥
    api_key = os.environ.get("MOONSHOT_API_KEY", "your_api_key_here")
    
    # 初始化客户端
    client = OpenAI(
        base_url="https://api.moonshot.cn/v1",
        api_key=api_key
    )
    
    # 检查文件是否存在
    file_path = Path("example.pdf")
    if not file_path.exists():
        return "错误：示例文件'example.pdf'不存在，请先准备该文件。"
    
    try:
        # 上传文件
        print("正在上传文件...")
        file_object = client.files.create(file=file_path, purpose="file-extract")
        
        # 获取文件内容
        print("正在提取文件内容...")
        file_content = client.files.content(file_id=file_object.id).text
        
        # 构建请求消息
        messages = [
            {"role": "system", "content": "你是Kimi，由Moonshot AI提供的人工智能助手，你会提供安全，有帮助，准确的回答。"},
            {"role": "system", "content": file_content},  # 将文件内容作为系统消息传入
            {"role": "user", "content": "请简要总结这个文件的主要内容"}
        ]
        
        # 调用API
        response = client.chat.completions.create(
            model="moonshot-v1-32k",
            messages=messages,
            temperature=0.3
        )
        
        return response.choices[0].message.content
    except Exception as e:
        return f"文件问答时发生错误: {str(e)}"

if __name__ == "__main__":
    print("===== Kimi API 标准调用示例 =====")
    result = 调用KimiChat()
    print(result)
    
    print("\n===== Kimi API 流式响应示例 =====")
    流式响应示例()
    
    print("\n===== Kimi API 文件问答示例 =====")
    print("注意：此示例需要在当前目录存在名为'example.pdf'的文件")
    print("如果您没有准备该文件，这部分将显示错误信息")
    file_qa_result = 文件问答示例()
    print(file_qa_result)
    
    print("\n注意: 请确保在运行前设置了MOONSHOT_API_KEY环境变量，或者直接在代码中替换'your_api_key_here'为您的实际API密钥") 