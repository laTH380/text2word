import config
import requests
import json

URL = config.OLLAMA_API_PORT + "generate"

def text2word(instruction, content):
    prompt = instruction + " " + config.INNSTRUCTION + "\n\"" + content + "\""
    senddata = {
        "model": config.LLM_MODEL,
        "prompt": prompt,
        "stream": False  # ストリーミングを無効にするオプション
    }
    response = requests.post(URL, json=senddata)
    print(f'Sent POST request to {URL} with data: {json.dumps(senddata, ensure_ascii=False)}')
    # 返り値を取得
    if response.status_code == 200:
        # 正常にリクエストが成功した場合
        result = response.json()  # JSON形式のレスポンスを取得
        # JSONの内容を行ごとにパースして配列にまとめる
        print(f'Response: {json.dumps(result, ensure_ascii=False)}')
        if 'response' in result:  # 'result'キーが存在するか確認
            # 行ごとに分割し、配列にまとめる
            lines = result['response'].split('\n')  # 改行で分割
            lines_array = [line for line in lines if line.strip()]  # 空行を除外
            lines_array = [line[1:] for line in lines_array]  # 空行を除外
            return lines_array
    else:
        # エラーが発生した場合
        print(f'Error: {response.status_code} - {response.text}')
        return []

if __name__ == "__main__":
    instruction = "今から与える文章はどのような声であるかを説明しているものです。声を説明している部分を情報ごとに抜き出して過不足なく箇条書きにしてください。"
    content = "女性が明るい声で楽しそうに友達と話している。"
    result = text2word(instruction, content)
    print(result)