import requests
import json

def CallCozeWorkflow():
    # API配置
    url = "https://api.coze.cn/v1/workflow/run"
    token = "pat_R1EBfPj58YYrvmPYDefQTcjT7d0Rqi3Yo1aWktDL**********"
    workflow_id = "750611864544732*****"
    
    # 请求头
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    
    # 请求体
    payload = {
        "parameters": {
            "input": "一只拟人化的橘猫"
        },
        "workflow_id": workflow_id
    }
    
    try:
        # 发送POST请求
        response = requests.post(url, headers=headers, json=payload)
        
        # 检查响应状态
        response.raise_for_status()
        
        # 解析响应
        result = response.json()
        print("API调用成功！")
        print("响应数据:", json.dumps(result, ensure_ascii=False, indent=2))
        
        # 如果响应成功，提取图片URL
        if result.get("code") == 0:
            data = json.loads(result.get("data", "{}"))
            image_url = data.get("output")
            if image_url:
                print(f"生成的图片URL: {image_url}")
        
        return result
        
    except requests.exceptions.RequestException as e:
        print(f"API调用失败: {str(e)}")
        return None

if __name__ == "__main__":
    CallCozeWorkflow() 