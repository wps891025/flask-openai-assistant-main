from flask import Flask, render_template, request, redirect, url_for
import openai
import os

app = Flask(__name__)

openai.api_key = os.getenv('OPENAI_API_KEY')

@app.route('/')
def index():
    return render_template('index2.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()  # 取得 JSON 格式的請求資料
    prompt = data.get('prompt', '')  # 獲取 prompt 內容

    response = openai.ChatCompletion.create(
        messages=[{"role": "user", "content": prompt}],
        model="gpt-4o-mini-2024-07-18",
        temperature=0.5,
    )

    generated_text = response['choices'][0]['message']['content'].strip()
    return jsonify({"response": generated_text})  # 回傳 JSON 格式的回應

if __name__ == '__main__':
    app.run(debug=True)
