from flask import Flask, jsonify, request
import random
import string
from flask_cors import CORS  # Để xử lý CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # Cho phép tất cả nguồn truy cập

# Giả lập cơ sở dữ liệu lưu trữ các key
valid_keys = set()

# Hàm tạo key ngẫu nhiên với chữ "CAPYBARA_KEY"
def generate_key():
    random_part = ''.join(random.choices(string.ascii_uppercase + string.digits, k=20))  # Tạo phần ngẫu nhiên dài 20 ký tự
    return f"CAPYBARA_{random_part}"  # Kết hợp "CAPYBARA_KEY" với phần ngẫu nhiên

# API tạo key
@app.route('/api/generate-key', methods=['GET'])
def generate_key_api():
    new_key = generate_key()
    valid_keys.add(new_key)  # Lưu key vào danh sách hợp lệ
    return jsonify({"key": new_key})

# API kiểm tra key
@app.route('/api/check-key', methods=['POST'])
def check_key_api():
    key = request.json.get('key')
    if key in valid_keys:
        return jsonify({"status": "valid", "message": "Key is valid!"})
    else:
        return jsonify({"status": "invalid", "message": "Key is invalid!"})

# Don't use app.run() for Vercel deployment
