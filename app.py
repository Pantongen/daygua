# app.py

from flask import Flask, render_template, jsonify
import json
import random

app = Flask(__name__)

# 读取 JSON 文件并保存到变量中，确保使用 utf-8 编码
with open('gua_data.json', 'r', encoding='UTF-8') as f:
    gua_data = json.load(f)

@app.route('/',methods = ['GET'])
def index():
    return render_template('index.html')

@app.route('/get_gua',methods=["POST"])
def get_gua():
    # 获取所有卦的名称列表
    gua_names = list(gua_data.keys())
    # 随机选择一个卦的名称
    gua_name = random.choice(gua_names)
    # 使用选择的卦名称获取对应的卦信息
    gua_info = gua_data[gua_name]
    return jsonify(gua_info)

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port= '3000')
