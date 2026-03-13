import os
from openai import OpenAI

def chat_with_deepseek():
    # --- 配置部分 ---
    # 如果使用火山引擎，base_url 通常为: https://ark.cn-beijing.volces.com/api/v3
    # 如果直接使用 DeepSeek 官方，base_url 为: https://api.deepseek.com
    client = OpenAI(
        api_key="7eb6f9dc-e28e-4c4b-90e2-d2ec992cf93e", 
        base_url="https://ark.cn-beijing.volces.com/api/v3" 
    )

    print("Chatbot 已启动 (输入 'quit' 退出)")

    while True:
        # 1. 发送一段文本问题
        user_input = input("\n用户: ")
        if user_input.lower() in ['quit', 'exit', '退出']:
            break

        try:
            # 2. 调用模型 (DeepSeek-V3 或 R1)
            response = client.chat.completions.create(
                model="ep-20260313175806-4gfdz",  # 火山引擎此处需填写具体的 Endpoint ID (如: ep-xxx)
                messages=[
                    {"role": "system", "content": "你是一个有用的助手"},
                    {"role": "user", "content": user_input},
                ],
                stream=False
            )

            # 3. 获取并打印模型回复
            answer = response.choices[0].message.content
            print(f"\nChatbot: {answer}")

        except Exception as e:
            print(f"发生错误: {e}")

if __name__ == "__main__":
    chat_with_deepseek()
