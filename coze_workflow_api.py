from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)

class CozeWorkflowAPI:
    def __init__(self):
        self.url = "https://api.coze.cn/v1/workflow/run"
        self.token = "pat_R1EBfPj58YYrvmPYDefQTcjT7d0Rqi3Yo1aWk************"
        self.workflow_id = "7506118645*******"
        
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
        
        try:
            response = requests.post(self.url, headers=headers, json=payload)
            response.raise_for_status()
            result = response.json()
            
            if result.get("code") == 0:
                data = json.loads(result.get("data", "{}"))
                return {
                    "success": True,
                    "image_url": data.get("output"),
                    "debug_url": result.get("debug_url")
                }
            else:
                return {
                    "success": False,
                    "error": result.get("msg", "未知错误")
                }
                
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }

# 创建API实例
coze_api = CozeWorkflowAPI()

@app.route('/generate', methods=['POST'])
def Generate():
    data = request.get_json()
    
    if not data or 'prompt' not in data:
        return jsonify({
            "success": False,
            "error": "缺少必要的prompt参数"
        }), 400
        
    result = coze_api.GenerateImage(data['prompt'])
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) 