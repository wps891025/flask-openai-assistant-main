from flask import Flask, render_template, request, redirect, url_for, jsonify
import openai
import os

app = Flask(__name__)

openai.api_key = os.getenv('OPENAI_API_KEY')

@app.route('/')
def index():
    return render_template('index2.html')

@app.route('/generate', methods=['POST'])
def generate():
    prompt = request.get_json()['prompt']
    response = openai.ChatCompletion.create(
        messages=[
            {"role": "user", "content": prompt}
        ],
        model="gpt-4o-mini-2024-07-18",
        temperature = 0.5,
    )
    generated_text = response['choices'][0]['message']['content'].strip()
    #return render_template('index.html', response=generated_text)
    return jsonify({"response": generated_text})
    # return jsonify({"response": prompt})
if __name__ == '__main__':
    app.run(debug=True)
