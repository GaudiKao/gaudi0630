from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import os

# 載入環境變數
load_dotenv()

# 創建 Flask 應用實例
app = Flask(__name__)

# 配置設定
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default-secret-key')

# 基本路由
@app.route('/')
def home():
    return render_template('index.html', title='首頁')

# API 路由
@app.route('/api/hello', methods=['GET'])
def hello_api():
    name = request.args.get('name', '訪客')
    return jsonify({
        'message': f'你好，{name}！',
        'status': 'success'
    })

# POST 請求示例
@app.route('/api/submit', methods=['POST'])
def submit_data():
    data = request.get_json()
    if not data:
        return jsonify({
            'message': '無效的數據',
            'status': 'error'
        }), 400
    
    return jsonify({
        'message': '數據提交成功',
        'data': data,
        'status': 'success'
    })

# 錯誤處理
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

# 啟動應用
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)